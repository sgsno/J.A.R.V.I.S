# Mark LIII — Setup (this workspace)

Personal AI assistant from [FatihMakes/Mark-LIII](https://github.com/FatihMakes/Mark-LIII). Dependencies are installed in `.venv`.

## Run here (Linux cloud / local Linux)

```bash
source .venv/bin/activate
python main.py
```

On first launch, paste a free [Gemini API key](https://aistudio.google.com/apikey). Optional: enable **Hey Jarvis** from ⚙ → WAKE WORD.

## Fresh install (any machine)

**Windows** (your Downloads folder):

```powershell
cd $HOME\Downloads\Mark-LIII-main\Mark-LIII-main
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python setup.py
python main.py
```

**macOS / Linux**:

```bash
cd Mark-LIII
python3 -m venv .venv
source .venv/bin/activate
python setup.py
python main.py
```

`setup.py` installs `requirements.txt` (OS-filtered) and Playwright Chromium + Firefox.

## Windows .exe

Build on the Windows machine (this Linux environment cannot produce a Windows exe):

```powershell
cd $HOME\Downloads\Mark-LIII-main\Mark-LIII-main
.\.venv\Scripts\Activate.ps1
.\build_exe.ps1
```

Output: `dist\Mark-LIII\Mark-LIII.exe`. Keep that whole folder — the exe loads `actions`, `config`, and the rest from beside itself. Playwright browser automation still needs browsers installed via `python -m playwright install` in the venv you built from; voice and HUD work from the exe alone.

## Already installed in this environment

- Python 3.12 virtualenv at `.venv`
- All packages from `requirements.txt`
- Playwright Chromium + Firefox browsers
- Linux helpers: `portaudio`, `pulseaudio-utils` (volume), `brightnessctl`, `xdg-utils`, `python3-tk`
