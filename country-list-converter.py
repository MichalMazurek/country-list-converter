#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import argparse
import glob
import shutil

__author__ = "Michal Mazurek <mazurek.michal@gmail.com>"
"""
country-list-convert.py
:author: Michal Mazurek

This script is intended to use with files from https://github.com/umpirsky/country-list
"""

def error(*args):
    print("Error: ", *args, file=sys.stderr)


def main():

    description = """Moves all the json files from directories, to one directory with proper names:
    en/country.json -> out_dir/en.json

    Source directory have to point to /country-list/country/icu/ from https://github.com/umpirsky/country-list

    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-s", "--source-dir", help="Source directory", required=True)
    parser.add_argument("-o", "--out-dir", help="Output directory", required=True)
    parser.add_argument("-d", "--debug", action="store_true")
    arguments = parser.parse_args()

    if os.path.exists(arguments.source_dir):
        if not os.path.exists(arguments.out_dir):
            os.makedirs(arguments.out_dir)
        elif not os.path.isdir(arguments.out_dir):
            error("File %s is not a directory" % arguments.out_dir)
            sys.exit(1)

        i = 0
        for lang_path in glob.glob(os.path.join(arguments.source_dir, "*")):
            lang = os.path.basename(lang_path)
            if os.path.isdir(lang_path):
                # this is the language directory
                source_file = os.path.join(lang_path, "country.json")
                out_file = os.path.join(arguments.out_dir, "%s.json" % lang.lower())
                if arguments.debug:
                    print("copying %s" % source_file, "to %s" % out_file)
                shutil.copyfile(source_file, out_file)
                i += 1

        print("Done. Copied %d files" % i)

    else:
        error("Directory: %s does not exist." % arguments.source_dir)
        parser.print_help()


if __name__ == "__main__":
    main()