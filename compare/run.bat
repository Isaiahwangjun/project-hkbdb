@echo off
setlocal EnableDelayedExpansion

set "firstline=true"
set "file_path=C:\Users\wang\Desktop\daoyi\HongKong\ocr\name.txt"

for /f "tokens=1 delims=," %%a in (%file_path%) do (
    if "!firstline!"=="true" (
        set "firstline=false"
    ) else (
        echo Processing: %%a
        python main.py %%a
    )
)

endlocal
