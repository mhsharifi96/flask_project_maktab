from flask import Flask 

from .api.routes import api 
from .site.routes import site

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app





# Blueprints and Views
# https://flask.palletsprojects.com/en/2.0.x/tutorial/views/



# The create_app() function is the Application Factory, which takes the configuration file as the parameter. 
# ... In the end, the factory function will create and return an application instance. 
# Blueprints are a set of . py files that 
# organize groups of related routes and views functions.

# more detail :     https://betterprogramming.pub/build-test-and-deploy-a-flask-application-part-3-3a2abfe4be21#:~:text=The%20create_app()%20function%20is,configuration%20file%20as%20the%20parameter.&text=In%20the%20end%2C%20the%20factory,related%20routes%20and%20views%20functions.