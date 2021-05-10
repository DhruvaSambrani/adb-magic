#! /usr/bin/env python3

import os.path
import re

def _getconfig(key):
    with open(os.path.expanduser("~/.adb-magic-config")) as f:
        while True:
            s = re.search(key+"=(.*)", f.readline())
            if s != None:
                return s.groups()[0]

def getpath():
    return _getconfig("PATH")
