
### Python

* Pipenv

```
pipenv --python 3.7 # Create a new project using Python 3.7, specifically
pipenv --rm # Remove project virtualenv 
pipenv install --dev # Install all dependencies for a project (including dev)
pipenv lock --pre # Create a lockfile containing pre-releases
pipenv graph # Show a graph of your installed dependencies
pipenv check # Check your installed dependencies for security vulnerabilities
pipenv install -e . # Install a local setup.py into your virtual environment/Pipfile
pipenv run pip freeze # Use a lower-level pip command
```

* Use venv on Linux (Debian10)
```
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
deactivate
pip install -r requirements.txt
```
