@rem 这是一个自动化编译的脚本，自动编译最新的main.ui文件
@echo off

set "file1=.\ui\main.ui" > nul
set "file2=.\ui\main_ui.py" > nul

:loop
timeout /t 5 > nul
for %%A in ("%file1%") do set "file1date=%%~tA"
for %%B in ("%file2%") do set "file2date=%%~tB"
if "%file1date%" gtr "%file2date%" (
  PySide6-uic ui/main.ui -o ui/main_ui.py
  echo [RUNNING][%time%]main_ui.py was update!
) else (
  echo [INFO][%time%]main_ui is latest!
)
@echo off
goto loop

