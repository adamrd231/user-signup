from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

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
    if email == "":
        return True
    if "." in email and "@" in email:
        return True
    else:
        return False


@app.route("/", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template("user-signup.html")


    if request.method == 'POST':
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
        email_error = ""

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

        if len(password) not in range(3,21) and len(password) != 0:
            length_error = "The password should be in between 3 and 20 characters."

        if noSpace(password) == True:
            space_error = "Please do not enter spaces in your password"

        if emailValid(email) == False:
            email_error = "Email must include a '@' and '.' "

        if not username_error and not password_error and not verify_error and password == verify and len(password) > 2 and noSpace(password) == False and emailValid(email) == True:
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
                                         space_error=space_error,
                                         email_error=email_error
                                         )

app.run()
