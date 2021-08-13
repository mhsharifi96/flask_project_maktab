from flask import Flask ,render_template #new
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello_v7.html')

if __name__ == '__main__':
   app.run(debug = True)

#Flask will try to find the HTML file in the templates folder, 
# in the same folder in which this script is present.


#Flask uses jinja2 template engine.
# A web template contains HTML syntax interspersed placeholders 
# for variables and expressions (in these case Python expressions)
#  which are replaced values when the template is rendered.