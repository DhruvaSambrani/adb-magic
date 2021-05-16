# ADB Scripts

An experiment to see if an android phone can be used completely from ADB.

## Files and what they do

1. adb-key - Send a specific special key, like home, back etc. See the code for all keys
2. adb-swipe - Swipe! u, d, l, r
3. adb-ui - Click anything (literally anything!) which has text
4. adb-text - Constant streaming of text. Requires Enter to send enabled :(. No Unicode or emoji support, yet.
5. adb-notify - Pull all notifications, and open appropriate application if necessary.

## Best Served with

- KISS Launcher
- ADBKeyBoard
- SoundWire
- spotify-tui

## ToDo

- all 
    - [x] make them importable [easy]
    - [ ] document things :joy:
- [ ] add a single point for all scripts. Either [discuss]
    - make a pakka UI with curses, which'll be super cool but hard
    - Discord way, where each command be preceded by a delimiter, like `/` for key, `;` for swipe etc
    - Vim way, with "modes", this seems unnecessarily complex
- [ ] add clipboard sharing - SHOULD be easy and you'll find multiple SO posts [med]
- [ ] adb-swipe - add speeds [easy]
- adb-ui 
    - [ ] ignore case [easy(regex change)]
    - [ ] allow user to put their own regex [hard, may collide with our regex]
- adb-text
    - [x] run the adb command async, to allow better UI. Emoji via discord-like names `:joy:`
         - Requires https://github.com/senzhk/ADBKeyBoard instead
    - [x] accept cli args. If none, then go into loop. [EZ-PZ]
- adb-notify 
    - [ ] Add some ignores? It shows too many notifications. [med]
    - [ ] Group notifications [med]
