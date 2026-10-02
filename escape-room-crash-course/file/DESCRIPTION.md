No todos los archivos son lo que dice su extensión. Un `.png` no siempre es una imagen.

El comando `file` revisa el contenido de un archivo y te dice qué tipo de archivo es en realidad:

```console
hacker@dojo:~$ file /path/to/some/file
```

Para cambiarle el nombre (y la extensión) a un archivo se usa `mv`:

```console
hacker@dojo:~$ mv viejo.png nuevo.txt
```

Ejecuta `file` en `~/flag.png`, cámbiale la extensión a `.txt` y léelo para encontrar la flag.
