
$old_path = (Get-Location).Path
# switch to current script path
Set-Location $PSScriptRoot
pyside6-uic.exe -g python main.ui  -o ui_main.py
pyside6-rcc.exe assets/assets.qrc -o rc_assets.py
# switch back to original path
Set-Location $old_path