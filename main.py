from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("user-signup.html")

@app.route("/", methods=['POST'])
def sign_up():
    username = request.form[('username')]
    password = request.form[('password')]
    verify = request.form[('verify')]
    email = request.form[('email')]

    username_error = ""
    password_error = ""
    verify_error = ""

    if username == "":
        username_error = "Please Enter Your Username"

    if 1 == 1:
        return render_template('user-signup.html',
                                 username=username,
                                 username_error=username_error,
                                 password_error=password_error,
                                 verify_error=verify_error
                                 )
    else:
        return render_template('/welcome.html', username=username)



app.run()
