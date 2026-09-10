# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Mark LIII. Build on Windows:  .\build_exe.ps1
from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_submodules

ROOT = Path(SPECPATH)

datas = [
    (str(ROOT / "core" / "prompt.txt"), "core"),
    (str(ROOT / "config" / "jarvis.ico"), "config"),
    (str(ROOT / "dashboard" / "static"), "dashboard/static"),
]

binaries = []
hiddenimports = [
    "PyQt6",
    "PyQt6.QtCore",
    "PyQt6.QtGui",
    "PyQt6.QtWidgets",
    "sounddevice",
    "numpy",
    "cv2",
    "PIL",
    "mss",
    "google.genai",
    "google.genai.types",
    "fastapi",
    "starlette",
    "uvicorn",
    "uvicorn.logging",
    "uvicorn.loops",
    "uvicorn.loops.auto",
    "uvicorn.protocols",
    "uvicorn.protocols.http",
    "uvicorn.protocols.http.auto",
    "uvicorn.lifespan",
    "uvicorn.lifespan.on",
    "cryptography",
    "qrcode",
    "playwright",
    "pyautogui",
    "pyperclip",
    "psutil",
    "bs4",
    "duckduckgo_search",
    "requests",
    "openpyxl",
    "pptx",
    "youtube_transcript_api",
    "send2trash",
    "tinytuya",
    "googleapiclient",
    "google_auth_oauthlib",
]
hiddenimports += collect_submodules("google.genai")

for pkg in ("PyQt6", "google.genai", "uvicorn", "fastapi"):
    try:
        extras = collect_all(pkg)
        datas += extras[0]
        binaries += extras[1]
        hiddenimports += extras[2]
    except Exception:
        pass

a = Analysis(
    [str(ROOT / "main.py")],
    pathex=[str(ROOT)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Mark-LIII",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    icon=str(ROOT / "config" / "jarvis.ico"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="Mark-LIII",
)
