#!/usr/bin/python3

def command_helper():
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Magic number change")
    #parser.print_help()
    
    parser.add_argument("file", help="input file, ex: tmp.zip")
    #parser.add_argument("-mc", "--magic", default="0000",help="input magic number, ex: 504b")
    parser.add_argument("-m", "--method", default="switch",help="pack or unpack, defult is pack")
    parser.add_argument("-c", "--change-filename", default="False", help="change filename")
    
    return parser.parse_args()


if __name__ == '__main__':
    args = command_helper()
    
    #print(args)
    
    if args.method == "switch":
    #    import re
    #
        fileName = args.file
    #    newMagic = bytes.fromhex(args.magic)
    #    length = len(newMagic)
        length = 16
    #
        with open(fileName, "rb") as f:
            fileBytes = f.read()
            fileBytes = b"".join(
                [
                    fileBytes[length:length*2],
                    fileBytes[:length],
                    fileBytes[length*2:]
                ]
            )
    #
    #    fileName = re.sub("\.", "_", fileName) + "_" + oldMagic.hex()
        with open(fileName, "wb") as f:
            f.write(fileBytes)
    