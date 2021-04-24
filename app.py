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
        session['user'] = str(mongo.db.users.find_one(
            {"username": request.form.get('username').lower()})['_id'])
        flash('Registration Successful!')
        return redirect(url_for('my_trials', user_id=session['user']))

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
                    session['user'] = str(mongo.db.users.find_one(
                        {"username": request.form.get(
                            'username').lower()})['_id'])
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        'my_trials', user_id=session['user']))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password. Please try again!")

        else:
            # username does not exist
            flash("Incorrect Username and/or Password. Please try again!")

    return render_template('pages/login.html')


# Creates an instance of a Swagger client
OPENTRIALS_API_SPEC = (
    'https://api.opentrials.net/v1/swagger.yaml')
config = {'use_models': False}
client = SwaggerClient.from_url(OPENTRIALS_API_SPEC, config=config)
dir(client)


@app.route('/clinical_trials')
def clinical_trials():

    trials = client.trials.searchTrials(q='immunotherapy&cancer').result()

    return render_template('pages/clinical_trials.html', trials=trials)


@app.route('/add_trial/', methods=['GET', 'POST'])
def add_trial():

    if not session.get('user'):
        flash('You can not bookmark a trial prior to sign in. Please log in and try again!')
        return redirect(url_for('login'))

    if request.method == "POST":

        user_trial_id = request.form.get('trial_api_id') + session.get('user')

        favourite = {
            'id': request.form.get('trial_api_id'),
            'user_id': session.get('user'),
            'user_trial_id': user_trial_id
        }

        mongo.db.trials.insert_one(favourite)
        flash('Trial added to your favourites!')
        return redirect(url_for('clinical_trials'))

    return render_template(
        'pages/add_trial.html', favourite=favourite)


@app.route('/my_trials/<user_id>', methods=['GET', 'POST'])
def my_trials(user_id):

    if session['user']:

        trials_mdb = mongo.db.trials.find({'user_id': user_id})
        trials = []

        for trial in trials_mdb:
            id = str('id:' + ' ' + trial['id'])
            trial_api = client.trials.searchTrials(q=id).result()
            trials.append(trial_api)

        mongo_comments = mongo.db.comments.find()
        comments = []
        for comment in mongo_comments:
            comments.append(comment)

        return render_template(
            'pages/mytrials.html', user_id=user_id,
            trials=trials, comments=comments)

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
