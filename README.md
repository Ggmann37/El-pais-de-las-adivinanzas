# El país de las adivinanzas

Landing web en HTML con diseño moderno y animaciones.

## ¿Cómo funciona?

1. Al abrir la página aparece la pantalla **Empezar juego**.
2. Al pulsar ese botón, se muestra la pantalla para introducir el código secreto.
3. En una esquina aparece un temporizador que cuenta el tiempo de la partida.
4. Si el código es incorrecto, aparece el mensaje **Incorrecto**.
5. Si el código es correcto, aparece el mensaje **Correcto**, se muestra el panel de victoria y el temporizador se detiene.
6. Desde ese panel puedes descargar un diploma en PDF: al pulsar, te pedirá tu nombre y generará el texto **“Felicidades <tu nombre>, lo has conseguido.”**, incluyendo también el tiempo final.
7. Incluye un icono de GitHub en la esquina superior derecha para abrir la búsqueda del repositorio en modo visualización (solo lectura).

> Nota: el valor del código secreto no se muestra en el README ni en la interfaz.

## Uso en local

Abre el archivo `index.html` directamente en tu navegador, o levanta un servidor local:

```bash
python3 -m http.server 8000
```

Luego visita:

- `http://localhost:8000/index.html`
