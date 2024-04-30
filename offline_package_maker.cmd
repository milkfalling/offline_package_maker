@echo off

echo Running bot_py_duplicator.py...
python bot_py_duplicator.py
echo bot_py_duplicator.py has finished.

echo Running lost_module_inspector.py...
python lost_module_inspector.py
echo lost_module_inspector.py has finished.

echo Installing dependencies from requirements.txt...
python installpackacges.py
echo Dependencies installed successfully.

echo Freezing requirements.txt with updated versions...
pip freeze > requirements.txt
echo Updated versions saved in requirements.txt.

echo Installing pip-download...
pip install pip-download
echo pip-download installed successfully.

echo Creating dependency directory...
mkdir dependency
echo Dependency directory created successfully.

echo Downloading offline installation packages for dependencies...
pip-download -r requirements.txt -d dependency
echo Offline installation packages downloaded successfully.

echo Deleting duplicated .py files...
del /Q duplicate*.py
echo Duplicated .py files deleted successfully.

pause
