import argparse
from copy import getc, putc, copy
from utils import file_or_string

BLANK = 32
NEWLINE = 10
TAB = 9

def count_characters(s: str):
    cc = 0
    for c in s:
        cc += 1

    return cc

def count_lines(s: str):
    if not s:
        return 0 # early exit to avoid counting empty strings as 1 line long
  
    lc = 0

    for c in s:
        if ord(c) == NEWLINE:
            lc += 1

    return max(lc, 1) # For the edge case of a single string with no new line char

def count_words(s: str):
    wc = 0

    in_a_word = False

    for c in s:
        c_ord = getc(c)

        if c_ord == BLANK or c_ord == NEWLINE or c_ord == TAB:
            in_a_word = False
        elif not in_a_word:
            in_a_word = True
            wc += 1 

    return wc

def count(to_count: str, chars: bool, lines: bool, words: bool):
    cc = count_characters(to_count) if chars else -1

    lc = count_lines(to_count) if lines else -1

    wc = count_words(to_count) if words else -1

    display_count(cc, lc, wc)

def display_count(cc: int, lc: int, wc: int):
    if cc + lc + wc == -3:
        copy("No count options included!")

    if cc > -1:
        copy("Character Count: " + str(cc))
        copy("\n")

    if lc > -1:
        copy("Line Count: " + str(lc))
        copy("\n")

    if wc > -1:
        copy("Word Count: " + str(wc))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Count characters, lines, and/or words in a string or file"
        )
    parser.add_argument(
            "input_data",
            type=file_or_string,
            help="Provide either a path to a file or a string."
        )

    parser.add_argument("-c", "--characters", action="store_true")
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")

    args = parser.parse_args()

    count(args.input_data, args.characters, args.lines, args.words)
    print() # flushes weird percentage sign from the shell

