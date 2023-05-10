@rem 这是一个自动化编译的脚本，自动编译最新的main.ui文件.version-230510
@echo off

set "file1=.\ui\main.ui" > nul
set "file2=.\ui\main_ui.py" > nul

echo [%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%]auto_ui_install start now! >> auto_ui_install.txt
echo --------------------------------------------
echo # automatic compilation has been turned on
echo # program will automatically return a report
echo --------------------------------------------

for %%A in ("%file1%") do set "file1date=%%~tA"
for %%B in ("%file2%") do set "file2date=%%~tB"
if not "%file1date%" gtr "%file2date%" (
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py is latest!
)

:loop
timeout /t 5 > nul
for %%A in ("%file1%") do set "file1date=%%~tA"
for %%B in ("%file2%") do set "file2date=%%~tB"
if "%file1date%" gtr "%file2date%" (
  PySide6-uic ui/main.ui -o ui/main_ui.py
  echo [%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py was update! >> auto_ui_install.txt
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py was update!
)
@echo off
goto loop

