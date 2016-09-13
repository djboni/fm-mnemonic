#!/usr/bin/python
# -*- encoding: utf-8 -*-
# por Djones A. Boni <djboni gmail com>
M2B = {}; B2M = {}; M = "\
0123456789ABCDEFGHIJKLMNOPQRSTUV\
WXYZ!!!!!:;<=>?@#$%&()*+,-./!!~_"
for i in range (0,0x40):
    M2B[M[i]],B2M[i] = i,M[i]

def mne2bin(mnemonic):
    val = 0
    for ch in mnemonic:
        val = (val << 6) | M2B[ch]
    s = ""
    while val > 0:
        s += chr(val & 0xFF)
        val >>= 8
    r = "'"
    for ch in s:
        r += "\\x%02X" % ord(ch)
    r += "'"
    return r

if __name__ == "__main__":
    mnemonic = "OVSPD"
    binvalue = mne2bin(mnemonic)
    print "%s = %s" % (mnemonic, binvalue)
