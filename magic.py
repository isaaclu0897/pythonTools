#!/usr/bin/python3
import sys
import re

fileName = sys.argv[1]
newMagic = bytes.fromhex(sys.argv[2])
length = len(newMagic)

with open(fileName, "rb") as f:
    fileBytes = f.read()
    oldMagic = fileBytes[:length]
    fileBytes = newMagic + fileBytes[length:]

fileName = re.sub("\.", "_", sys.argv[1]) + "_" + oldMagic.hex()
with open(fileName, "wb") as f:
    f.write(fileBytes)