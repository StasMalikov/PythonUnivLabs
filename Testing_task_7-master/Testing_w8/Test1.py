from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
from Logic import syntax_highlighting_py


app= Flask(__name__)
bootstrap=Bootstrap(app)
text_changer=  syntax_highlighting_py() 


def write1(text):
    with open("output1.txt", "w") as file:
        print(text, file=file)

def write2(text):
    with open("output2.txt", "w") as file:
        print(text, file=file)

@app.route('/user/<name>')
def user(name):
    return render_template('myuser.html',name=name)

@app.route('/')
@app.route('/home')
def home():
    return render_template('MyIndex.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        result = request.form['FormText']
        write1(result)
        result=text_changer.set_syntax(result)
        write2(result)
        return render_template("MyResult.html",text = result)
        

if __name__=='__main__':
    app.run(debug=True)