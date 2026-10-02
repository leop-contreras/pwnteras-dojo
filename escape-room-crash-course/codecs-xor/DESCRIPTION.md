XOR mezcla cada caracter del texto con un caracter de una llave. Lo bueno: si aplicas XOR otra vez con la misma llave, regresas al texto original.

`~/flag` está cifrada con XOR, y la llave está en `~/llave`. Si haces `cat ~/flag` vas a ver caracteres raros, es normal.

`codecs.py` hace XOR con `xor`, pasándole el texto y la llave:

```console
hacker@dojo:~$ python3 /challenge/codecs.py xor "texto" LLAVE
```

Usa `xor` con el contenido de `~/flag` y `~/llave` para encontrar la flag.
