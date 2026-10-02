El cifrado César recorre cada letra `n` posiciones en el abecedario. ROT13 es solo un César con `n = 13`.

Esta vez no sabemos `n`. Pero sabemos que la flag empieza con `pwn.college{`, así que puedes probar desplazamientos hasta que el texto tenga sentido. Para deshacer un desplazamiento de `n`, usa `-n`:

```console
hacker@dojo:~$ python3 /challenge/codecs.py caesar "texto" -3
```

Encuentra el desplazamiento correcto y descifra `~/flag` para encontrar la flag.
