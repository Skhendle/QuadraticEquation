
# **Web Server Application**
This is a learning webserver application ...


## **Getting Started** <br>
```python
# Python version: 3.9.0
"MINGW64 - bash terminal"

To create virtual environment.
$ Back End: python -m venv env

# To activate virtual environment
# Windows 
$ Back End : source ".\env\Scripts\activate"

# Ubuntu 
$ Back End : source ./env/bin/activate

# To install the requirements run
$ Back End : pip  install -r requirements.txt

# To update requirements.txt after installing new package
$ Back End : pip freeze > requirements.txt

# To run the application use the following command
$ Back End : uvicorn app.main:app --reload

# To run a service of the application use the following command
$ Back End : uvicorn app.'service name'.main:app --reload
# E.g
$ Back End : uvicorn app.quadratic_equation.main:app --reload

# To deactivate virtual enviroment
$ Back End : deactivate
```

## **Accessing API Documentation** <br>
- {server url}/docs
- {server url}/redoc

## </br> **API Routes Documentation Format**
* Describes how to setup a package that implements a system requirement  for the application. Specifies the file name, what the file contains and how it is used</br>

### **Package Layout | For Each System Feature**
<blockquote>

[x] __input.py__ - *Contains pyndatic classes, that are used as parameters for API functions and services class.*
</br>

[x] __route.py__ - *Contains the API function with the url describing its service path, states its Protocol( POST, GET, DELETE or UPDATE) and calls for the service to be executed*
</br>

[x] __service.py__ - *Where the logic for a system requirement is executed*
</br>

[x] __main.py__ - *Allows us to run a service independently independently*</br>
</blockquote>