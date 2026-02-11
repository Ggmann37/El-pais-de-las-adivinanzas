# El país de las adivinanzas

Landing web en HTML con diseño moderno y animaciones.

## ¿Cómo funciona?

1. Al abrir la página, se solicita un código secreto.
2. Si el código es incorrecto, aparece el mensaje **Incorrecto**.
3. Si el código es correcto, aparece el mensaje **Correcto** y se muestra un panel de victoria con animación.
4. Desde ese panel puedes descargar un diploma en PDF: al pulsar, te pedirá tu nombre y generará el texto **“Felicidades <tu nombre>, lo has conseguido.”**
5. Incluye un icono de GitHub en la esquina superior derecha para abrir el repositorio en modo visualización.

> Nota: el valor del código secreto no se muestra en el README ni en la interfaz.

## Uso en local

Abre el archivo `index.html` directamente en tu navegador, o levanta un servidor local:

```bash
python3 -m http.server 8000
```

Luego visita:

- `http://localhost:8000/index.html`
