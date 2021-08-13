from flask import Flask, redirect, url_for #new
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


# The url_for() function is very useful for dynamically building a URL for a specific function.
#  The function accepts the name of a function as first argument,
#  and one or more keyword arguments, each corresponding to the variable part of URL.
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      print(url_for('hello_admin'))
      return redirect(url_for('hello_admin')) #new
   else:
      print(url_for('hello_guest',guest = name))
      return redirect(url_for('hello_guest',guest = name)) #new

if __name__ == '__main__':
   app.run(debug = True)