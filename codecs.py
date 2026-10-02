#!/usr/bin/env python3
# Hecho por: 0Kron

"""
codecs.py — Toolkit básico de codificaciones para retos.

Uso:
    python3 codecs.py list
    python3 codecs.py b64e   "texto"
    python3 codecs.py b64d   "dGV4dG8="
    python3 codecs.py xore   "texto" TxG
    python3 codecs.py xord   "hex"   TxG
    python3 codecs.py rot13  "texto"
    python3 codecs.py hexe   "texto"
    python3 codecs.py hexd   "68656c6c6f"
    python3 codecs.py rev    "texto"
    python3 codecs.py caesar "texto" 3

El segundo argumento (para xor/caesar) es la llave o el desplazamiento.
"""

import sys
import base64
import codecs
import binascii


# ---------- Base64 ----------

def b64_encode(texto: str) -> str:
    """Texto plano -> string Base64."""
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


def b64_decode(texto: str) -> str:
    """String Base64 -> texto plano.
    Acepta input sin padding (lo agrega automáticamente)."""
    s = texto.strip()
    faltante = (-len(s)) % 4
    s += "=" * faltante
    return base64.b64decode(s).decode("utf-8", errors="replace")


# ---------- XOR ----------

def xor(texto: str, llave: str) -> str:
    """
    XOR simétrico: la misma función cifra y descifra.
    Entrada ASCII -> bytes -> XOR con la llave (repetida) -> ASCII.

    Se usa 'latin-1' al reconstruir el string para garantizar que
    CUALQUIER byte (0x00-0xFF) tenga una representación 1:1 y el
    round-trip texto -> xor -> texto sea perfecto.
    """
    datos = texto.encode("latin-1")            # ASCII -> bytes
    clave = llave.encode("latin-1")            # ASCII -> bytes
    salida = bytes(b ^ clave[i % len(clave)]   # XOR con la llave repetida
                   for i, b in enumerate(datos))
    return salida.decode("latin-1")            # bytes -> ASCII


# ---------- ROT13 ----------

def rot13(texto: str) -> str:
    """ROT13 es su propia inversa (aplica dos veces y vuelves al original)."""
    return codecs.encode(texto, "rot_13")


# ---------- Hex ----------

def hex_encode(texto: str) -> str:
    return texto.encode("utf-8").hex()


def hex_decode(texto: str) -> str:
    return bytes.fromhex(texto.strip()).decode("utf-8", errors="replace")


# ---------- Reversa ----------

def reverse(texto: str) -> str:
    return texto[::-1]


# ---------- César ----------

def caesar(texto: str, shift: int) -> str:
    """Desplaza letras por 'shift' posiciones (solo A-Z / a-z)."""
    out = []
    for c in texto:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - ord("A") + shift) % 26 + ord("A")))
        else:
            out.append(c)
    return "".join(out)


# ---------- CLI ----------

AYUDA = """codecs.py — toolkit de codificaciones

  list                       muestra los métodos disponibles
  b64e   <texto>             Base64 encode
  b64d   <b64>               Base64 decode
  xor    <texto> <llave>     XOR (cifra o descifra, es simétrico)
  rot13  <texto>             ROT13 (aplica dos veces y vuelve)
  hexe   <texto>             Hex encode
  hexd   <hex>               Hex decode
  rev    <texto>             Invertir string
  caesar <texto> <n>         César con desplazamiento n

Ejemplos:
  python3 codecs.py xor "M1_4M0RC1T0" leo    -> !T0X(_>&^8U
  python3 codecs.py b64e "S1XS3V3N"              -> UzFYUzNWM04=
  python reto/codecs.py b64d "UzFYUzNWM04="      -> S1XS3V3N

"""


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help", "help"):
        print(AYUDA)
        return 0

    cmd = argv[1].lower()

    try:
        if cmd == "list":
            print("Metodos disponibles:")
            for m in ("b64e", "b64d", "xor", "rot13",
                      "hexe", "hexd", "rev", "caesar"):
                print(f"  - {m}")
            return 0

        if cmd in ("b64e", "b64d"):
            texto = argv[2]
            print(b64_encode(texto) if cmd == "b64e" else b64_decode(texto))
            return 0

        if cmd == "xor":
            texto, llave = argv[2], argv[3]
            print(xor(texto, llave))
            return 0

        if cmd == "rot13":
            print(rot13(argv[2]))
            return 0

        if cmd == "hexe":
            print(hex_encode(argv[2]))
            return 0
        if cmd == "hexd":
            print(hex_decode(argv[2]))
            return 0

        if cmd == "rev":
            print(reverse(argv[2]))
            return 0

        if cmd == "caesar":
            print(caesar(argv[2], int(argv[3])))
            return 0

        print(f"Comando desconocido: {cmd}", file=sys.stderr)
        print(AYUDA, file=sys.stderr)
        return 1

    except IndexError:
        print(f"Faltan argumentos para '{cmd}'.\n", file=sys.stderr)
        print(AYUDA, file=sys.stderr)
        return 1
    except (binascii.Error, ValueError) as e:
        print(f"Error de formato: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
