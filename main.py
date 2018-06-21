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

    error_count = 0

    if not verify_username():
        username_error = "Please enter a valid username."
        error_count += 1
    else: 
        username_error = ""
    if not verify_password_length():
        password_valid_error = "Please enter a valid password."
        error_count += 1
    else:
        password_valid_error = ""
    if not verify_passwords_match():
        password_match_error = "Passwords do not match."
        error_count += 1
    else:
        password_match_error = ""
    if not verify_email():
        email_error = "Please enter a valid email address."
        error_count += 1
    else:
        email_error = ""
    if error_count > 0:
        return render_template('edit.html', username_error = username_error, password_valid_error = password_valid_error, password_match_error = password_match_error, email_error = email_error)
    
    return render_template('signup-confirmation.html', username = request.form['username'], password = request.form['password'], verify_password = request.form['verify-password'], email = request.form['email'] )

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html')

app.run()