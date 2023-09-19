rem Virtual environment name
set venv_name= .venv

rem Check if the virtual environment exists
if not exist %venv_name% (
    rem Create a virtual environment
    python -m venv %venv_name%
)

rem Activate the virtual environment
call %venv_name%\Scripts\activate

rem Install requirements
pip install -r requirements.txt

rem Set the FLASK_APP environment variable to run app/app.py
set FLASK_APP=app/app

rem default port number
set port=5000

rem Check if a port was provided
if "%~1" neq "" (
    rem Use the provided port instead
    set port=%~1
)

rem Run Flask on the specified or default port
flask run --port %port%
