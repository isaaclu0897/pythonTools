import sys

fileName = sys.argv[1]
byte = bytes.fromhex(sys.argv[2])

with open(fileName, "rb") as f:
    fileBytes = f.read()
    fileBytes = byte + fileBytes[len(byte):]

with open(fileName, "wb") as f:
    f.write(fileBytes)
    