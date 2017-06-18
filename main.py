from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("user-signup.html")


def isEmpty(s):
    if s == "":
        return True
    else:
        return False


@app.route("/", methods=['POST'])
def sign_up():
    username = request.form[('username')]
    password = request.form[('password')]
    verify = request.form[('verify')]
    email = request.form[('email')]

    username_error = ""
    password_error = ""
    verify_error = ""

    if isEmpty(username):
        username_error = "Please Enter Your Username"

    if isEmpty(password):
        password_error = "Please Enter Your Password"

    if isEmpty(verify):
        verify_error = "Please Verify Your Password"

    if not username_error and not password_error and not verify_error:
        return render_template('/welcome.html', username=username)
    else:
        return render_template('user-signup.html',
                                 username=username,
                                 username_error=username_error,
                                 password_error=password_error,
                                 verify_error=verify_error
                                 )




app.run()
