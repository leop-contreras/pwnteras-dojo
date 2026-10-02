ROT13 recorre cada letra 13 posiciones en el abecedario (`a` → `n`, `b` → `o`...). Como el abecedario tiene 26 letras, aplicarlo dos veces te regresa al texto original.

`codecs.py` aplica ROT13 con `rot13`:

```console
hacker@dojo:~$ python3 /challenge/codecs.py rot13 "texto"
```

Aplica `rot13` al contenido de `~/flag` para encontrar la flag.
