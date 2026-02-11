#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
COMMENTS_FILE = ROOT / "comments.json"
MAX_COMMENTS = 100


def read_comments():
    if not COMMENTS_FILE.exists():
        return []

    try:
        data = json.loads(COMMENTS_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except json.JSONDecodeError:
        pass

    return []


def write_comments(comments):
    COMMENTS_FILE.write_text(
        json.dumps(comments, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


class Handler(BaseHTTPRequestHandler):
    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/api/comments":
            comments = read_comments()
            self.send_json({"comments": comments})
            return

        if path in ["/", "/index.html"]:
            target = ROOT / "index.html"
        elif path == "/README.md":
            target = ROOT / "README.md"
        else:
            self.send_json({"error": "Ruta no encontrada"}, status=404)
            return

        if not target.exists():
            self.send_json({"error": "Archivo no encontrado"}, status=404)
            return

        content = target.read_bytes()
        ctype = "text/html; charset=utf-8" if target.suffix == ".html" else "text/markdown; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/comments":
            self.send_json({"error": "Ruta no encontrada"}, status=404)
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)

        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_json({"error": "JSON inválido"}, status=400)
            return

        name = str(payload.get("name", "")).strip()
        text = str(payload.get("text", "")).strip()

        if not name or not text:
            self.send_json({"error": "Nombre y comentario son obligatorios"}, status=400)
            return

        comment = {
            "name": name[:60],
            "text": text[:300],
            "createdAt": datetime.now(timezone.utc).isoformat(),
        }

        comments = read_comments()
        comments.insert(0, comment)
        comments = comments[:MAX_COMMENTS]
        write_comments(comments)

        self.send_json({"ok": True, "comments": comments}, status=201)


if __name__ == "__main__":
    port = 8000
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Servidor activo en http://0.0.0.0:{port}")
    server.serve_forever()
