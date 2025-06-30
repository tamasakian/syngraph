#!/usr/bin/env python3

import argparse
import sys

from syngraph import functions

def main():
    args = parse_args()
    function = functions[args.function]
    try:
        function(*args.args)
    except TypeError as e:
        print(e)
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("function", choices=functions)
    parser.add_argument("args", type=str, nargs="*")
    args = parser.parse_args()
    return args

functions = {
    "mso": functions.mso,
    "mso_p": functions.mso_p,
}

if __name__ == "__main__":
    main()