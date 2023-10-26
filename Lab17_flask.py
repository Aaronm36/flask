from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)

boostrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
   return '<h1> Hello world from Flask! </h1>'


@app.route('/aaron')
def t_test():
    return render_template('index.html')