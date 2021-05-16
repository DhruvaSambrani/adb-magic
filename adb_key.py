#!/usr/bin/env python3

import adb_config
import sys
import subprocess
import os

name_key_map={
        "home": "KEYCODE_HOME", 
        "back": "KEYCODE_BACK",
        "clear": "KEYCODE_CLEAR",
        "call": "KEYCODE_CALL",
        "ecall": "KEYCODE_ENDCALL",
        "up":  "KEYCODE_DPAD_UP",
        "down": "KEYCODE_DPAD_DOWN",
        "left": "KEYCODE_DPAD_LEFT",
        "right": "KEYCODE_DPAD_RIGHT",
        "enter": "KEYCODE_ENTER",
        "power": "KEYCODE_POWER",
        "vold": "KEYCODE_VOLUME_DOWN",
        "mute": "KEYCODE_VOLUME_MUTE",
        "volu": "KEYCODE_VOLUME_UP",
        "wake": "KEYCODE_WAKEUP"
    }

def key(adbpath, keyname):
    useless_cat_call = subprocess.Popen([adbpath, "shell"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, errors = useless_cat_call.communicate(input="input keyevent "+name_key_map[keyname])

if __name__ == "__main__":
    key(adb_config.getpath(), sys.argv[1])
