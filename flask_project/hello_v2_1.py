from flask import Flask
app = Flask(__name__)

def hello_world():
   return 'hello world'

def about():
   return 'hello about'


app.add_url_rule('/hello', view_func=hello_world)
app.add_url_rule('/about', view_func=about)


# Register a rule for routing incoming requests and building URLs. 
# The route() decorator is a 
# shortcut to call this with the view_func argument

if __name__ == '__main__':
    # app.run()
    app.run(debug = True)
    #app.run(host, port, debug, options)    