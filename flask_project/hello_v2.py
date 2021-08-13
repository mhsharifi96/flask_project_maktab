from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # print(heeello)
    return 'Hello World'

if __name__ == '__main__':
    # app.run()
    # app.run(debug=True)
    app.run(debug = True,port=8000,host='0.0.0.0')
    #app.run(host, port, debug, options)    