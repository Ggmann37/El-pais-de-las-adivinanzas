# El país de las adivinanzas

Landing web en HTML con diseño moderno y animaciones.

## ¿Cómo funciona?

1. Al abrir la página, se solicita un código secreto.
2. Si el código es incorrecto, aparece el mensaje **Incorrecto**.
3. Si el código es correcto, aparece el mensaje **Correcto** y se muestra un panel de victoria con animación.
4. Desde ese panel puedes descargar un diploma en PDF: al pulsar, te pedirá tu nombre y generará el texto **“Felicidades <tu nombre>, lo has conseguido.”**
5. Incluye un apartado de **Comentarios** que pide nombre y comentario.
6. Los comentarios se guardan en servidor (`comments.json`) para que se vean desde otros ordenadores.

> Nota: el valor del código secreto no se muestra en el README ni en la interfaz.

## Uso en local

Para que los comentarios sean compartidos entre dispositivos, inicia el servidor incluido:

```bash
python3 server.py
```

Luego visita:

- `http://localhost:8000`

## Archivos clave

- `index.html`: interfaz y lógica del juego/comentarios.
- `server.py`: API `GET/POST /api/comments` y servido de la web.
- `comments.json`: almacenamiento persistente de comentarios.
