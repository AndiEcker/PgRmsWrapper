#!/bin/bash
# 32 bit compile for Windows
# more info at: http://sparkandshine.net/en/build-a-windows-executable-from-python-scripts-on-linux/
# .. or at: http://stackoverflow.com/questions/2950971/cross-compiling-a-python-script-on-linux-into-a-windows-executable#comment11890276_2951046
wine ~/.wine/drive_c/Python34/Scripts/pyinstaller.exe --onefile PgRmsWrapper.py