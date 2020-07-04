"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Testing_w8 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('MyIndex.html',text = "")

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        #result = request.form
        return render_template("MyIndex.html",text = "")
        #return render_template("result.html",text = "%s" % result)
