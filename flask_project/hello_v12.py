from flask import Flask, render_template, request
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename

import os
app = Flask(__name__)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print('os path jsoin',os.path.join(app.config['UPLOAD_FOLDER']))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return 'file uploaded successfully'
    else :
        return render_template('hello_v12_uploader.html')
		
if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(str(dir_path )+'/uploads/' )
    app.config['UPLOAD_FOLDER'] = str(dir_path )+'/uploads/'

    app.run(debug = True)



# note : https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
