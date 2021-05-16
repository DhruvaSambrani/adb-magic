#!/usr/bin/env python3

import adb_config
import emoji
import sys
import subprocess
import os
import base64

# Unicode support needs https://github.com/senzhk/ADBKeyBoard

def _preprocess(text, uni):
    if uni:
        text = emoji.emojize(text, use_aliases=True)
        return base64.b64encode(text.encode()).decode()
    else:
        text = text.translate(str.maketrans({"`": r"\`"}))
        return text

def send_text(adbpath, text, uni=True):
    if uni:
        subprocess.run([adbpath, "shell", "am", "broadcast", "-a", "ADB_INPUT_B64", "--es", "msg", "\""+_preprocess(text, uni)+"\""], capture_output=True)
        send_text(adbpath, "\n", False)
    else:
        subprocess.run([adbpath, "shell", "input","keyboard", "text", "\""+_preprocess(text, uni)+"\n\""])
#eewf
if __name__ == "__main__":
    adbpath = adb_config.getpath()
    if len(sys.argv) > 1:
        send_text(adbpath, " ".join(sys.argv[1:]))
    else:
        while True:
            _in = input("[In]: ")
            send_text(adbpath, _in)
