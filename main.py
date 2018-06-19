from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/signup-confirmation", methods=['POST'])
def user_signup_confirmation():

    #username = request.form['username']
    #password = request.form['password']
    #verify_password = request.form['verify-password']
    #email = request.form['email']

    return render_template('signup-confirmation.html', username = request.form['username'])

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html')

app.run()