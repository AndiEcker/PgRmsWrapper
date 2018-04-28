Installation
------------

Place PgRmsWrapper.exe into the PGRMS installation directory (where PGRMS.EXE and PGRMS.INI are situated).


Usage
-----

PgRmsWrapper can be used in the same way like the PGRMS.EXE application, The difference to PGRMS.EXE is that
PgRmsWrapper removes extra command line parameters (for to be written into the INI file PGRMS.INI) and then
executes the application PGRMS.EXE with remaining command line parameters. Please note that the RMS*- and LOG-
parameter names are case-sensitive and have to be specified exactly like the INI variable names. The PGRMS.EXE
parameters and the extra parameters can be given in any order (also mixed-up) on the command line for to start
PgRmsWrapper.exe.

All the command line parameters that are starting with the string "RMS" will be written into the
file PGRMS.INI. The same happens additionally also for the command line parameter "LOG=path\file".

All the other command line parameters of PgRmsWrapper will be passed onto the execution of PGRMS.EXE (like
e.g. Mode).

Please note that the ini variables within the file PGRMS.INI will not be restored to their old/previous values!
So the variable values within PGRMS.INI will always have the values of the last execution of PgRmsWrapper.
Therefore if you want to execute PGRMS.EXE from your installation directory without PgRmsWrapper then you have
to make sure that all the INI variables are having their correct values.

The following example call will overwrite the values of the PGRMS.INI-variables RMSCashier and RMSCashNo (with
6 and 99) and will then execute PGRMS.EXE with the Mode and RoomID parameters:

    PgRmsWrapper.exe RMSCashier=6 Mode=RoomReq RMSCashNo=99 RoomID=124


PgRmsWrapper Exit Cods
-----------------------

1 == The executable file PGRMS.EXE is not in the current working directory. Please move PgRmsWrapper.exe into
     the installation folder of the PGRMS application and start it from there.

2 == The configuration file PGRMS.INI is not in the current working directory. Please move PgRmsWrapper.exe
     into the installation folder of the PGRMS application and start it from there.

3 == The execution of PGRMS.EXE failed. For the determine the problem please check the printout by running
     PgRmsWrapper with the same command line parameters in a command shell (e.g. CMD.EXE under Windows).
