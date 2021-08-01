REM pip install pyinstaller
pyinstaller --onefile main.py

move ".\dist\main.exe" ".\Vocabulary.com_to_Anki.exe"

rmdir /S /Q ".\build" 
rmdir /S /Q ".\dist"
del /Q ".\test.spec"
