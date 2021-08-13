from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
       print('args',request.args)
       print('form',request.form)
       user = request.form['username']
       return redirect(url_for('success',name = user))
   else:
        print('args',request.args)
        print('form',request.form)
        user = request.args.get('username')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)


#ابتدا فایل hello_v5_login را باز کنید
# توضیحات متد فرم در فایل hello_v5_login
# یک بار پست باشد
# یک بار گت