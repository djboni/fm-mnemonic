# [FM Mnemonics](https://github.com/djboni/fm-mnemonic)

by [Djones A. Boni](https://twitter.com/djonesboni)

Convert FM Mnemonic string to binary format.

# Example 1

Print mnemonic in binary.

```python
>>> import mnemonic
>>> print mnemonic.mne2bin('OVSPD')
'\x4D\xC6\x7D\x18'
```

# Example 2

Running the script you get the following output, which is a Python dictionary
that maps the mnemonics to its corresponding string with the binary data.

```python
MNEMONICS = {
     'OVSPD' : '\x4D\xC6\x7D\x18',
     'OVREV' : '\x9F\xB3\x7D\x18',
     'HRACC' : '\x0C\xA3\x6C\x11',
     'HRBRK' : '\xD4\xB6\x6C\x11',
     'EXIDL' : '\x55\x23\x85\x0E',
     'DRVID' : '\x8D\xF4\x6D\x0D',
     'IGNON' : '\x17\x76\x41\x12',
     'FM_MD' : '\x8D\xF5\x5B\x0F',
     'TRP_M' : '\xD6\x9F\x6D\x1D',
     'TIMES' : '\x9C\x63\x49\x1D',
     'ODO_M' : '\xD6\x8F\x35\x18',
     'SPDKH' : '\x11\xD5\x64\x1C',
     'REVPM' : '\x56\xF6\x39\x1B',
     'VEHID' : '\x8D\x14\x39\x1F',
}
```

# TODO

Some characters are not present in the conversion table. There is a exclamation
mark `!` as a placeholder in the table.
