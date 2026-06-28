import argparse
import os

ENDFILE: int = -1
NEWLINE: int = 10 # ASCII value

def file_or_string(arg: str):
    if os.path.isfile(arg):
        with open(arg, 'r', encoding='utf-8') as f:
            return f.read()
    return arg

def getc(ch: str):
    try:
        if ch == "\n":
            c = NEWLINE
        else:
            c = ord(ch)
    except EOFError:    # Should never occur
        c = ENDFILE

    return c

def putc(ch: int):
    if ch == NEWLINE:
        c = "\n"
    else:
        c = chr(ch)

    print(c, sep="", end="")

def copy(s: str):
    for c in s:         # Can't really go thru file until EOF detected in
        putc(getc(c))   # Python, unlike Pascal

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy a file's contents or a string")

    parser.add_argument(
            "input_data",
            type=file_or_string,
            help="Provide either a path to a file or a string to copy."
            )

    args = parser.parse_args()

    copy(args.input_data)
    print() # flushes weird percentage sign from the shell

