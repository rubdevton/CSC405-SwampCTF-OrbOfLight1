# encode.py
# Author: Ruben Barahona (rabaraho@ncsu.edu)
# HackPack Team
# For SwampCTF - Orb of Light 1: Secret
import sys

msg = input("INPUT> ")
print("=== Encoded ===")
# Known dictionary
dict = {'m':'2', 'r':'9', 'c':'a', 'i':'A', 'x':'d', 'l':'E', 'a':'f', 'd':'g', 'k':'G', 'o':'h', 'p':'i', 'b':'l', 'w':'L', 'q':'n', 'j':'N', 'u':'o', 'v':'r', 'h':'R', 'f':'S', 'g':'T', 'n':'t', 't':'W', 's':'z', 'y':'Z'}
for ch in msg:
    if ch in dict:
        sys.stdout.write(dict[ch])
    else:
        sys.stdout.write(ch)
sys.stdout.flush()