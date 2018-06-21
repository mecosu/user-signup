from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

def verify_username():
    username = request.form['username']
    number_of_characters = len(username)
    if number_of_characters > 3 and number_of_characters < 20:
        return True
    return False

def verify_password_length():
    password = request.form['password']
    number_of_characters = len(password)
    if number_of_characters > 3 and number_of_characters < 20:
            if " " not in password:
                return True       
    return False

def verify_passwords_match():
    password = request.form['password']
    verify_password = request.form['verify-password']
    if password == verify_password:
        return True
    return False

def verify_email():
    email = request.form['email']
    number_of_characters = len(email)
    if email == "":
        return True
    if number_of_characters > 3:
        if '@' in email:
            if '.' in email:
                if ' ' not in email:
                    return True
    return False

@app.route("/signup-confirmation", methods=['POST'])
def user_signup_confirmation():

    username = request.form['username']
    email = request.form['email']

    if not verify_username():
        username_error = "Please enter a valid username."
    else: 
        username_error = ""
    if not verify_password_length():
        password_valid_error = "Please enter a valid password."
    else:
        password_valid_error = ""
    if not verify_passwords_match():
        password_match_error = "Passwords do not match."
    else:
        password_match_error = ""
    if not verify_email():
        email_error = "Please enter a valid email address."
    else:
        email_error = ""

    if not username_error and not password_valid_error and not password_match_error and not email_error:
        return render_template('signup-confirmation.html', username = request.form['username'], password = request.form['password'], verify_password = request.form['verify-password'], email = request.form['email'] )
    else:
        return render_template('edit.html', username_error = username_error, password_valid_error = password_valid_error, password_match_error = password_match_error, email_error = email_error)
    
@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html')

app.run()