from copy import getc, putc, copy
from utils import file_or_string
import argparse

NEWLINE = 10
SPACE = 32
TAB = 9
MAXLINE = 100000

def settabs(tab_length: int = 4):
    return [i for i in range(0, MAXLINE + 1) if i % tab_length == 0]


def tabpos(col, tabstops):
    if col > MAXLINE:
        return True
    else:
        return col in tabstops

def detab(to_detab: str, tabstops: list):
    col = 1

    for c in to_detab:
        c_num = getc(c)
        if c_num == TAB:
            while True:
                putc(SPACE)
                col += 1
                if tabpos(col, tabstops):
                    break
        elif c_num == NEWLINE:
            putc(NEWLINE)
            col = 1
        else:
            putc(c_num)
            col += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                description="Remove tabs from a doc and replace them with spaces."
            )

    parser.add_argument(
        "input_data",
        type=file_or_string,
        help="Provide either a path to a file or a string."
    )

    parser.add_argument(
        "tab_spaces",
        type=int,
        help="Provide the number of spaces replacing each tab."
    )

    args = parser.parse_args()

    tabstops = settabs(args.tab_spaces)
    detab(args.input_data, tabstops)
    print() # flushes terminal
