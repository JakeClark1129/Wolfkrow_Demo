
@echo off

rem Get the directory where this .bat file is located
set SCRIPT_DIR=%~dp0

rem Run Python script located in the parent directory of the .bat file
python "%SCRIPT_DIR%..\src\wolfkrow_demo\ingest\ingest.py" %*