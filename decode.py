# decode.py
# Author: Ruben Barahona (rabaraho@ncsu.edu)
# HackPack Team
# For SwampCTF - Orb of Light 1: Secret
import sys

msg = input("INPUT> ")
print("=== Decoded ===")
# Known dictionary
dict = {'2':'m', '9':'r', 'a':'c', 'A':'i', 'd':'x', 'E':'l', 'f':'a', 'g':'d', 'G':'k', 'h':'o', 'i':'p', 'l':'b', 'L':'w', 'n':'q', 'N':'j', 'o':'u', 'r':'v', 'R':'h', 'S':'f', 'T':'g', 't':'n', 'W':'t', 'z':'s', 'Z':'y'}
for ch in msg:
    if ch in dict:
        sys.stdout.write(dict[ch])
    else:
        sys.stdout.write(ch)
sys.stdout.flush()