@echo off

echo Running bot_py_duplicator.py...
python bot_py_duplicator.py
echo bot_py_duplicator.py has finished.

echo Running lost_module_inspector.py...
python lost_module_inspector.py
echo lost_module_inspector.py has finished.

echo Installing dependencies from wheels...
echo Installing dependencies from wheels... > installation_log.txt

for /r %%i in (dependency\*.whl) do (
    echo Installing %%i...
    echo Installing %%i... >> installation_log.txt
    pip install "%%i"
    if %errorlevel% equ 0 (
        echo Successfully installed %%i.
        echo Successfully installed %%i. >> installation_log.txt
    ) else (
        echo Error installing %%i.
        echo Error installing %%i. >> installation_log.txt
    )
)

echo Installing dependencies from tarballs...
echo Installing dependencies from tarballs... >> installation_log.txt

for /r %%i in (dependency\*.tar.gz) do (
    echo Installing %%i...
    echo Installing %%i... >> installation_log.txt
    pip install "%%i"
    if %errorlevel% equ 0 (
        echo Successfully installed %%i.
        echo Successfully installed %%i. >> installation_log.txt
    ) else (
        echo Error installing %%i.
        echo Error installing %%i. >> installation_log.txt
    )
)

echo All dependencies installed.
echo All dependencies installed. >> installation_log.txt

pause
