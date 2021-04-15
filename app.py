import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bravado.client import SwaggerClient
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def home():
    """
    Function to load the landing page
    """
    return render_template('pages/home.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Function to load the registration page
    """
    if request.method == 'POST':
        # check if username alrady exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        register = {
            'fname': request.form.get('fname').lower(),
            'lname': request.form.get('lname').lower(),
            'email': request.form.get('email').lower(),
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration Successful!')
        return redirect(url_for('clinical_trials', username=session['user']))

    return render_template('pages/register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password hash matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        'my_trials', username=session['user']))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password. Please try again!")

        else:
            # username does not exist
            flash("Incorrect Username and/or Password. Please try again!")

    return render_template('pages/login.html')


@app.route('/clinical_trials')
def clinical_trials():
    # Creates an instance of a Swagger client
    OPENTRIALS_API_SPEC = (
        'https://api.opentrials.net/v1/swagger.yaml')
    config = {'use_models': False}
    client = SwaggerClient.from_url(OPENTRIALS_API_SPEC, config=config)
    dir(client)
    trials = client.trials.searchTrials(q='immunotherapy&cancer').result()
    return render_template('pages/clinical_trials.html', trials=trials)


@app.route('/my_trials/<username>', methods=['GET', 'POST'])
def my_trials(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']

    if session['user']:
        return render_template('pages/mytrials.html', username=username)

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # clear session cookies
    flash('You are now logged out!')
    session.pop('user')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # switch to False before delivering project
            debug=True)
