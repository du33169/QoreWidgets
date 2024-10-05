
$old_path = (Get-Location).Path
# switch to current script path
Set-Location $PSScriptRoot
pyside6-uic -g python main.ui  -o ui_main.py
pyside6-rcc assets/assets.qrc -o rc_assets.py
# switch back to original path
Set-Location $old_path