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

def ifMatch(str, str2):
    if str == str2:
        return True
    else:
        return False

def noSpace(str):
    if " " in str:
        return True
    else:
        return False

def emailValid(email):
    if "." in email and "@" in email:
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
    match_error = ""
    length_error = ""
    email_ask = ""
    space_error = ""

    if isEmpty(email):
        email_ask = "Any chance you could enter that email?"

    if isEmpty(username):
        username_error = "Please Enter Your Username"

    if isEmpty(password):
        password_error = "Please Enter Your Password"

    if isEmpty(verify):
        verify_error = "Please Verify Your Password"

    if not ifMatch(password, verify):
        match_error = "The passwords do not match"

    if len(password) < 3 or len(password) > 20:
        length_error = "The password must be at least 3 characters or less than 21"

    if noSpace(password) == True:
        space_error = "Please do not enter spaces in your password"

    if not username_error and not password_error and not verify_error and password == verify and len(password) > 2 and noSpace(password) == False:
        return render_template('/welcome.html', username=username)
    else:
        return render_template('user-signup.html',
                                 username=username,
                                 email=email,
                                 username_error=username_error,
                                 password_error=password_error,
                                 verify_error=verify_error,
                                 match_error=match_error,
                                 length_error=length_error,
                                 email_ask=email_ask,
                                 space_error=space_error
                                 )



app.run()
