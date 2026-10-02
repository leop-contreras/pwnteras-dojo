Base64 convierte cualquier dato en texto usando solo letras, números, `+` y `/`. A veces termina en `=` o `==`, y eso casi siempre lo delata.

Nuestra herramienta `codecs.py` está en `/challenge/codecs.py`, y decodifica Base64 con `b64d`:

```console
hacker@dojo:~$ python3 /challenge/codecs.py b64d "dGV4dG8="
```

Para pasarle el contenido de un archivo en vez de escribirlo a mano, usa `"$(cat archivo)"`.

Decodifica `~/flag` con `b64d` para encontrar la flag.
