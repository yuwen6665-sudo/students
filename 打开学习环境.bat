@echo off
chcp 65001 >nul
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
powershell.exe -NoExit -ExecutionPolicy Bypass -File "E:\study\env.ps1"
