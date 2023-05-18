@rem 这是一个自动化编译的脚本，自动编译最新的main.ui文件.version-230516
@echo off

set "file1=.\ui\main.ui" > nul
set "file2=.\ui\main_ui.py" > nul
set "file3=.\ui\main.rc" > nul
set "file4=.\ui\main_rc.py" > nul

echo [%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%]auto_ui_install start now! >> auto_ui_install.txt
echo --------------------------------------------
echo # automatic compilation has been turned on
echo # program will automatically return a report
echo --------------------------------------------

for %%A in ("%file1%") do set "file1date=%%~tA"
for %%B in ("%file2%") do set "file2date=%%~tB"
for %%C in ("%file3%") do set "file3date=%%~tC"
for %%D in ("%file4%") do set "file4date=%%~tD"
if not "%file1date%" gtr "%file2date%" (
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py is latest!
)
if not "%file3date%" gtr "%file4date%" (
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_qrc.py is latest!
)

:loop
timeout /t 5 > nul
for %%A in ("%file1%") do set "file1date=%%~tA"
for %%B in ("%file2%") do set "file2date=%%~tB"
for %%C in ("%file3%") do set "file3date=%%~tC"
for %%D in ("%file4%") do set "file4date=%%~tD"
if "%file1date%" gtr "%file2date%" (
  PySide6-uic ui/main.ui -o ui/main_ui.py --from-imports
  echo [%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py was update! >> auto_ui_install.txt
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_ui.py was update!
)
if "%file3date%" gtr "%file4date%" (
  PySide6-rcc ui/main.qrc -o ui/main_rc.py
  echo [%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2%]main_qr.py was update! >> auto_ui_install.txt
  echo [INFO][%time:~0,2%:%time:~3,2%:%time:~6,2%]main_qr.py was update!
)
goto loop

