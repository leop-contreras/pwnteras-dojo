You wake up in a locked room. The only thing in it is a strange file in your home directory: `~/flag`.

Try to `cat` it and you'll get a screen full of garbage, because it's a binary blob.
Somewhere in that noise there's readable text, though, and one piece of it is the flag.

The `strings` command finds and prints every run of printable characters in a file:

```console
hacker@dojo:~$ strings /path/to/some/file
```

Run `strings` on `~/flag` to find the flag and escape the room!
