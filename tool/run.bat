@REM @echo off
@REM setlocal

@REM rem 
@REM set "file_path=C:\Users\wang\Desktop\daoyi\HongKong\ocr\name.txt"
@REM for /f "tokens=1" %%A in (%file_path%) do (
@REM     echo Parameter: %%A
@REM )

@REM endlocal

@echo off
setlocal EnableDelayedExpansion

set "firstline=true"
set "file_path=C:\Users\wang\Desktop\daoyi\HongKong\ocr\name.txt"

for /f "tokens=1 delims=," %%a in (%file_path%) do (
    if "!firstline!"=="true" (
        set "firstline=false"
    ) else (
        echo Processing: %%a
        python wholePreprocess.py %%a
        @REM python ../compare/pre.py %%a
    )
)

endlocal
