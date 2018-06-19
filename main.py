from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

def verify_password():
    password = request.form['password']
    verify_password = request.form['verify-password']
    number_of_characters = len(password)
    if password == verify_password:
        if number_of_characters > 3 and number_of_characters < 20:
            if " " not in password:
                return True       
    return False

def verify_username():
    username = request.form['username']
    number_of_characters = len(username)
    if number_of_characters > 3 and number_of_characters < 20:
        return True
    return False

def verify_email():
    email = request.form['email']
    if '@' in email:
        return True
    return False

@app.route("/signup-confirmation", methods=['POST'])
def user_signup_confirmation():

    #username = request.form['username']
    #password = request.form['password']
    #verify_password = request.form['verify-password']
    #email = request.form['email']
    error = "ERROR"
    if verify_password():
        if verify_email():
            if verify_username():
                return render_template('signup-confirmation.html', username = request.form['username'], password = request.form['password'], verify_password = request.form['verify-password'], email = request.form['email'] )
    return error

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html')

app.run()