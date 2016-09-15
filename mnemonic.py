#!/usr/bin/python
# -*- encoding: utf-8 -*-
# por Djones A. Boni <djboni gmail com>

M2B = {}; B2M = {}; M = "\
0123456789ABCDEFGHIJKLMNOPQRSTUV\
WXYZ!!!!!:;<=>?@#$%&()*+,-./!!~_"
for i in range (0,0x40):
    M2B[M[i]],B2M[i] = i,M[i]

def mne2bin(mnemonic):
    """Convert mnemonic to binary."""
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

def bin2mne(val):
    """Convert binary to mnemonic."""
    if type(val) == str:
        r = 0
        i = 0
        for ch in val:
            r = r | (ord(ch) << (8 * i))
            i += 1
        val = r
    r = ''
    while val > 0:
        r += B2M[val & 0x3F]
        val >>= 6
    return r[::-1]

if __name__ == "__main__":
    """Basic test."""
    mnelist = [
            "OVSPD",
            "OVREV",
            "HRACC",
            "HRBRK",
            "EXIDL",
            "DRVID",
            "IGNON",
            "FM_MD",
            "TRP_M",
            "TIMES",
            "ODO_M",
            "SPDKH",
            "REVPM",
            "VEHID",
    ]

    print "MNEMONICS = {"
    for mnemonic in mnelist:
        binvalue = mne2bin(mnemonic)
        mnevalue = bin2mne(eval(binvalue))
        if mnevalue != mnemonic:
            print "    # ERROR: mnevalue != mnemonic (%s != %s)" % (
                    mnevalue, mnemonic)
        print "    '%s' : %s," % (mnemonic, binvalue)
    print "}"

# Converted mnemonics (script output)
#
# MNEMONICS = {
#     'OVSPD' : '\x4D\xC6\x7D\x18',
#     'OVREV' : '\x9F\xB3\x7D\x18',
#     'HRACC' : '\x0C\xA3\x6C\x11',
#     'HRBRK' : '\xD4\xB6\x6C\x11',
#     'EXIDL' : '\x55\x23\x85\x0E',
#     'DRVID' : '\x8D\xF4\x6D\x0D',
#     'IGNON' : '\x17\x76\x41\x12',
#     'FM_MD' : '\x8D\xF5\x5B\x0F',
#     'TRP_M' : '\xD6\x9F\x6D\x1D',
#     'TIMES' : '\x9C\x63\x49\x1D',
#     'ODO_M' : '\xD6\x8F\x35\x18',
#     'SPDKH' : '\x11\xD5\x64\x1C',
#     'REVPM' : '\x56\xF6\x39\x1B',
#     'VEHID' : '\x8D\x14\x39\x1F',
# }
