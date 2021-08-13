from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello_v8_user.html', name = user)

@app.route('/score/<int:score>')
def hello_score(score):
   return render_template('hello_v8_score.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70,'maktab':51}
   return render_template('hello_v8_result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)