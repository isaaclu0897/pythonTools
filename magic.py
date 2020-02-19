#!/usr/bin/python3

def command_helper():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Magic number change")
    parser.print_help()
    
    parser.add_argument("file", help="input file, ex: tmp.zip")
    parser.add_argument("magic", help="input magic number, ex: 504b")
    #parser.add_argument("--method", "-m", help="pack or unpack, defult is pack", default="pack")
    
    return parser.parse_args()


if __name__ == '__main__':
    args = command_helper()
    
    import re

    fileName = args.file
    newMagic = bytes.fromhex(args.magic)
    length = len(newMagic)

    with open(fileName, "rb") as f:
        fileBytes = f.read()
        oldMagic = fileBytes[:length]
        fileBytes = newMagic + fileBytes[length:]

    fileName = re.sub("\.", "_", fileName) + "_" + oldMagic.hex()
    with open(fileName, "wb") as f:
        f.write(fileBytes)
    