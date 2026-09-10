@echo off
title Mark LIII
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo First-time setup: creating the Python environment...
  where python >nul 2>&1
  if errorlevel 1 (
    echo Python is not installed. Install Python 3.12 from https://www.python.org/downloads/
    echo Check "Add python.exe to PATH", then run this file again.
    pause
    exit /b 1
  )
  python -m venv .venv
  call ".venv\Scripts\activate.bat"
  python -m pip install --upgrade pip
  python setup.py
) else (
  call ".venv\Scripts\activate.bat"
)

python main.py
if errorlevel 1 pause
