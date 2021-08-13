from flask import Flask
app = Flask(__name__)  
#__name__ :  Flask uses this argument to determine the root path of the application 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



# export FLASK_APP=hello
# export FLASK_ENV=development #ubuntu
# $env:FLASK_APP = "hello" # powershell
# set FLASK_APP=hello #CMD
# flask run
