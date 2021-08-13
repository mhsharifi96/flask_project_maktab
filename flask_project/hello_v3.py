from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
   print('name : ',name)
   print('type : ',type(name))
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
@app.route('/blog/<float:postID>')
def show_blog(postID):
   print('postID : ',postID)
   print('type : ',type(postID))
   return 'Blog Number %s' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# accepts slashes used as directory separator character
# اسلش را به عنوان جدا کننده میپذیرد
@app.route('/path/<path:path>')
def pathSample(path):
   return 'path sample is  %s' % path

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run(debug = True)
