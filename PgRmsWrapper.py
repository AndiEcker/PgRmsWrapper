"""
PgRmsWrapper is providing extra parameters for to be written into the INI file PGRMS.INI before it is executing
the old application PGRMS.EXE (unfortunately the code base for PGRMS.EXE is no longer available).
"""
import os
import sys
import subprocess
# noinspection PyCompatibility
from configparser import ConfigParser

__version__ = '1.0'
EXE_FILE = 'PGRMS.EXE'
INI_FILE = 'PGRMS.INI'
INI_SECTION = 'PGRMS'
print()
print("PgRmsWrapper V" + __version__ + " (C) 2018 ACE Software")
print()


# check environment
if not os.path.isfile(EXE_FILE):
    print("The application " + EXE_FILE + " has to be situated in the same directory.")
    sys.exit(1)
print(EXE_FILE + " found")

if not os.path.isfile(INI_FILE):
    print("The configuration file " + INI_FILE + " has to be situated in the same directory.")
    sys.exit(2)
print(INI_FILE + " found")


# process application arguments
ini_values = list()
app_params = list(('PGRMS.EXE',))
for arg in sys.argv[1:]:
    if arg.upper().startswith('RMS') or arg.upper().startswith('LOG='):
        ini_values.append(arg)
    else:
        app_params.append(arg)


# change INI file variables
cfg_parser = ConfigParser()
cfg_parser.optionxform = str    # or use 'lambda option: option' to have case sensitive var names
cfg_parser.read(INI_FILE)
print("Read INI file content")
for ini_val in ini_values:
    name, val = ini_val.split('=')
    cfg_parser.set(INI_SECTION, name, val)
    print("Changed INI variable {} to {}".format(name, val))

with open(INI_FILE, 'w') as configfile:
    cfg_parser.write(configfile)
print("Saved INI file")

# execute EXE
print("Executing '" + " ".join(app_params) + "'")
err_msg = ""
try:
    subprocess.check_call(app_params, timeout=369)   # timeout in seconds -> 6 minutes
except subprocess.CalledProcessError as cpe:
    err_msg = EXE_FILE + " returned non-zero exit code " + str(cpe.returncode)
except subprocess.TimeoutExpired as toe:
    err_msg = EXE_FILE + " execution timed out"
except KeyboardInterrupt:
    err_msg = "User pressed Ctrl+C"
except Exception as ex:
    err_msg = EXE_FILE + " raised unspecified exception: " + str(ex)

if err_msg:
    print(err_msg)
    sys.exit(3)

print(EXE_FILE + " successfully executed")
sys.exit(0)
