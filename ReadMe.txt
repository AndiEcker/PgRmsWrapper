Installation
------------

Place PgRmsWrapper.exe into the PGRMS installation directory (where PGRMS.EXE and PGRMS.INI are situated).


Usage
-----

PgRmsWrapper can be used in the same way like the PGRMS.EXE application, The difference to PGRMS.EXE is that
PgRmsWrapper removes extra command line parameters (for to be written into the INI file PGRMS.INI) and then executes
the application PGRMS.EXE with remaining command line parameters.

All the command line parameters that are starting with the string "RMS" will be written into the
file PGRMS.INI. The same happens additionally also for the command line parameter "LOG=path\file".

All the other command line parameters of PgRmsWrapper will be passed onto the execution of PGRMS.EXE (like e.g. Mode).

Please note that the ini variables within the file PGRMS.INI will not be restored to their old/previous values!
Therefore if you want to execute PGRMS.EXE from your installation directory without PgRmsWrapper then you have to
make sure that all the INI variables are having their correct values.




PgRmsWrapper Exit Codes
-----------------------

1 == The executable file PGRMS.EXE is not in the current working directory. Please move PgRmsWrapper.exe into the
     installation folder of the PGRMS application and start it from there.

2 == The configuration file PGRMS.INI is not in the current working directory. Please move PgRmsWrapper.exe into the
     installation folder of the PGRMS application and start it from there.

3 == The execution of PGRMS.EXE failed. For the determine the problem please check the printout by running PgRmsWrapper
     with the same command line parameters in a command shell (e.g. CMD.EXE under Windows).
