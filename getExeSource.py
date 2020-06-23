import argparse
import re

__author__ = "mustafauzun0"


"""
getExeSource
"""

def main():
    parser = argparse.ArgumentParser(description="Get Exe Creation Source Path")

    parser.add_argument("-f", "--file", dest="file", help="Target .exe", required=True)
    
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf8", errors="ignore") as file:

            exeFile = file.readlines()

            for line in exeFile:
                match = re.search(r"[A-Z]:\\(.*).pdb", line)
                if match:
                    print("Exe Creation Source Path: " + match.group())

if __name__ == "__main__":
    main()
