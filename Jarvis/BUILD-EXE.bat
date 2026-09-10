@echo off
setlocal
title Building Mark-LIII.exe
cd /d "%~dp0"

echo.
echo  This will build Mark-LIII.exe. It can take several minutes.
echo  Leave this window open until it says DONE.
echo.
pause

if not exist ".venv\Scripts\python.exe" (
  echo Creating Python environment...
  where python >nul 2>&1
  if errorlevel 1 (
    echo Python is not installed. Install Python 3.12 from https://www.python.org/downloads/
    echo Check "Add python.exe to PATH", then double-click this file again.
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

echo.
echo Installing PyInstaller...
python -m pip install -r requirements-build.txt
if errorlevel 1 (
  echo Failed to install PyInstaller.
  pause
  exit /b 1
)

echo.
echo Building the exe...
python -m PyInstaller --noconfirm --clean mark.spec
if errorlevel 1 (
  echo PyInstaller failed. Scroll up for the error.
  pause
  exit /b 1
)

set DEST=%cd%\dist\Mark-LIII
if not exist "%DEST%\Mark-LIII.exe" (
  echo Build finished but Mark-LIII.exe was not found.
  pause
  exit /b 1
)

echo Copying app folders next to the exe...
for %%D in (actions plugins core config dashboard memory) do (
  if exist "%%D" (
    if exist "%DEST%\%%D" rmdir /s /q "%DEST%\%%D"
    xcopy "%%D" "%DEST%\%%D\" /e /i /y /q >nul
  )
)

echo.
echo ========================================
echo  DONE
echo  Your app is:
echo  %DEST%\Mark-LIII.exe
echo ========================================
echo.
echo Opening that folder now. You can pin Mark-LIII.exe to the taskbar
echo or copy the whole Mark-LIII folder anywhere. Keep the folder together.
echo.
explorer "%DEST%"
pause
