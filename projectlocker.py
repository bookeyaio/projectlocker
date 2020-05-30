from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 'c472d29d07aa206ccbf8457fddaed518'

@app.route('/home',methods=['GET', 'POST'])
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/mylocker')
def mylocker():
    return render_template("mylocker.html")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)