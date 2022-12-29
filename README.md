# MyTestAPI

## OpenAPI 3.0 Generated Flask project

All the routes are defined in 'project/api' folder. 
Each route parses the request and calls the corresponding function in the 'project/impl' directory passing all the parameters and request body as function arguments.

To run this project (Linux):
```
pip install -r requirements.txt
export FLASK_APP='MyTestAPI'
export FLASK_ENV=development
flask run
```
To run this project (Windows):
```
pip install -r requirements.txt      (needs to be done only once)
$env:FLASK_APP = "MyTestAPI"            (at every restart you need to run this)
$env:FLASK_ENV = "development"          (at every restart you need to run this)
python -m flask run                     (at every restart you need to run this)
```
