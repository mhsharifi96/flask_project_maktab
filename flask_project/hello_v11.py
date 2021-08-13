from flask import Flask, redirect, url_for, render_template, request, abort
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello_v11_login.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['username'] == 'admin' :
      return redirect(url_for('success'))
   else:
      #   abort(401)
      #   return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully hoooraaaaaa :|'
	
if __name__ == '__main__':
   app.run(debug = True)



