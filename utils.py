import os

def file_or_string(arg: str):
    if os.path.isfile(arg):
        with open(arg, 'r', encoding='utf-8') as f:
            return f.read()
    return arg

