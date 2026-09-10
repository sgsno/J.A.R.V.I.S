# Build Mark-LIII.exe on Windows (run from the project folder).
# Requires the same .venv you already use to launch the app.

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
    Write-Error "No .venv found. Create it first:  python -m venv .venv ; .\.venv\Scripts\Activate.ps1 ; python setup.py"
}

$py = ".\.venv\Scripts\python.exe"
& $py -m pip install -r requirements-build.txt
& $py -m PyInstaller --noconfirm --clean mark.spec

$dest = Join-Path $PSScriptRoot "dist\Mark-LIII"
if (-not (Test-Path $dest)) {
    Write-Error "PyInstaller did not create dist\Mark-LIII"
}

# Runtime folders the exe reads/writes next to itself (not inside _internal).
foreach ($name in @("actions", "plugins", "core", "config", "dashboard", "memory")) {
    $src = Join-Path $PSScriptRoot $name
    $out = Join-Path $dest $name
    if (Test-Path $src) {
        if (Test-Path $out) { Remove-Item $out -Recurse -Force }
        Copy-Item $src $out -Recurse -Force
    }
}

Write-Host ""
Write-Host "Built: $dest\Mark-LIII.exe"
Write-Host "Keep the whole dist\Mark-LIII folder together — the exe needs those sibling folders."
Write-Host "Double-click Mark-LIII.exe to launch."
