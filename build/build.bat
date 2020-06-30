rem call venv\Scripts\activate.bat

rem pyinstaller.exe -F --add-data="../weather;weather" --icon="view.ico" ../signage.py
rem copy ..\bg.mp3 dist\
pyinstaller.exe -F --add-data="../bg.jpg;." --add-data="../bgp.jpg;." --add-data="../balarm.wav;." --icon="view.ico" ../temp.py
rem xcopy /s /y ..\pictures dist\pictures\
copy ..\options.json dist\
copy ..\bg.jpg dist\
copy ..\bgp.jpg dist\
copy ..\balarm.wav dist\
