import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bravado.client import SwaggerClient
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Creates an instance of a Swagger client
OPENTRIALS_API_SPEC = (
    'https://api.opentrials.net/v1/swagger.yaml')
config = {'use_models': False}
client = SwaggerClient.from_url(OPENTRIALS_API_SPEC, config=config)
dir(client)


@app.route('/')
def home():
    """
    Function to load the landing page and get 5 last comments
    """
    comments = mongo.db.comments.find().limit(5).sort('posted_on', -1)

    # Convert comments into list for loop within loop functionality
    last5comments = []
    for comment in comments:
        last5comments.append(comment)

    # For each comment, find the corresponding trial when found
    # If trial not found (due to being removed from API),
    # flash appropriate message to user
    all_trials = []
    for comment in last5comments:
        result = client.trials.searchTrials(
            q=comment["trial_id"]).result()
        if result["total_count"] != 0:
            all_trials.append(result)
        else:
            flash(f'Trial corresponding with comment {comment.user_comment} \
                not found.')

    return render_template('pages/home.html',
                           last5comments=last5comments, all_trials=all_trials)


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
        return redirect(url_for('home', user_id=session['user']))

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
                    existing_user["fname"].capitalize()))
                return redirect(url_for(
                    'home', user_id=session['user']))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password. Please try again!")

        else:
            # username does not exist
            flash("Incorrect Username and/or Password. Please try again!")

    return render_template('pages/login.html')


@app.route('/clinical_trials', methods=["GET", "POST"])
def clinical_trials():
    """
    Function to load clinical trials from API
    """

    # Load all comments and convert to list to enable loop
    # within loop on add trial modal
    mongo_comments = mongo.db.comments.find().sort('posted_on', -1)
    comments = []
    for comment in mongo_comments:
        comments.append(comment)

    # Search functionality that retrieves coresponding trials from API
    # Limited to max 100 trials due to restriction from API
    if request.method == "POST":
        search = "cancer&immunotherapy&"+request.form.get('search')

        trials = client.trials.searchTrials(
            q=search, per_page=100).result()

        # If more than 100 trials are found, set count to 100
        # As maximum 100 trials will be retrieved / displayed
        count = trials['total_count']
        if count > 100:
            count = 100

        if not session.get('user'):
            return render_template('pages/clinical_trials.html',
                                   trials=trials, search=search, count=count)
        else:
            my_trials = mongo.db.trials.find({'user_id': session.get('user')})
            added_trials = []
            for trial in my_trials:
                added_trials.append(trial['id'])
            return render_template('pages/clinical_trials.html', trials=trials,
                                   added_trials=added_trials, search=search,
                                   comments=comments, count=count, public=True)

    elif not session.get('user'):
        trials = client.trials.searchTrials(
            q='immunotherapy&cancer', per_page=100).result()

        count = trials['total_count']

        return render_template('pages/clinical_trials.html',
                               trials=trials, count=count)

    else:
        # On loading of page, show the first 100 trials available
        trials = client.trials.searchTrials(
            q='immunotherapy&cancer', per_page=100).result()

        # Show accurate counter to users know the total available trials
        count = trials['total_count']

        my_trials = mongo.db.trials.find({'user_id': session.get('user')})
        added_trials = []
        for trial in my_trials:
            added_trials.append(trial['id'])
        return render_template('pages/clinical_trials.html', trials=trials,
                               added_trials=added_trials, comments=comments,
                               count=count, public=True)


@app.route('/add_trial/', methods=['GET', 'POST'])
def add_trial():
    """
    Function to add trial to your favorites
    """
    if request.method == "POST":
        favourite = {
                'id': request.form.get('trial_api_id'),
                'user_id': session.get('user')
                }

        mongo.db.trials.insert_one(favourite)
        flash('Trial added to your favourites!')

        return redirect(url_for('clinical_trials'))

    return render_template(
        'pages/add_trial.html', favourite=favourite)


@app.route('/my_trials/<user_id>', methods=['GET', 'POST'])
def my_trials(user_id):
    """
    Function to display the trials added to your favorites
    and display the comments written by that specific user
    """
    if session['user']:
        # Retrieve all trials added to favourites for specific user
        trials_mdb = mongo.db.trials.find({'user_id': user_id})
        trials = []

        for trial in trials_mdb:
            id = str('id:' + ' ' + trial['id'])
            trial_api = client.trials.searchTrials(q=id).result()
            if trial_api["total_count"] != 0:
                trials.append(trial_api)

        # Retrieve all the comments and convert to list
        mongo_comments = mongo.db.comments.find().sort('posted_on', -1)
        comments = []
        for comment in mongo_comments:
            comments.append(comment)

        # For each comment, find corresponding trial
        all_trials = []
        for comment in comments:
            result = client.trials.searchTrials(
                q=comment["trial_id"]).result()
            if result["total_count"] != 0:
                if result not in all_trials:
                    all_trials.append(result)
            # if trial not found, flash appropriate message
            else:
                flash(f'Trial corresponding with comment {comment.user_comment} \
                not found.')

        return render_template(
            'pages/mytrials.html', user_id=user_id,
            trials=trials, comments=comments,
            public=False, all_trials=all_trials)

    return redirect(url_for('login'))


@app.route('/view_trial/<trial_id>', methods=['GET', 'POST'])
def view_trial(trial_id):
    """
    Function to display specific trial when clicking name of trial in comment
    Redirects to clinical trials page where trial id is inserted in search
    """
    # Retrieve all comments and convert to list
    mongo_comments = mongo.db.comments.find().sort('posted_on', -1)
    comments = []
    for comment in mongo_comments:
        comments.append(comment)

    # Search specific trial based on trial id
    search = "cancer&immunotherapy&"+trial_id
    trials = client.trials.searchTrials(
        q=search).result()
    if trials["total_count"] != 0:
        count = trials['total_count']
        if not session.get('user'):
            return render_template('pages/clinical_trials.html',
                                   search=search, count=count, trials=trials)
        else:
            my_trials = mongo.db.trials.find({'user_id': session.get('user')})
            added_trials = []
            for trial in my_trials:
                added_trials.append(trial['id'])
            return render_template('pages/clinical_trials.html',
                                   added_trials=added_trials, trials=trials,
                                   search=search, comments=comments,
                                   count=count, public=True)
    else:
        flash('Trial not found.')
        return redirect(url_for('home'))


@app.route('/remove_trial/<trial_id>')
def remove_trial(trial_id):
    """
    Function to remove trial from your favorites
    """
    trial_to_remove = mongo.db.trials.find_one({
        'id': trial_id,
        'user_id': session['user']
    })
    mongo.db.trials.delete_one({"_id": trial_to_remove["_id"]})

    flash('Trial successfully deleted from your favourites!')

    return redirect(url_for('my_trials', user_id=session['user']))


@app.route('/add_comment/<user_id>/<trial_id>', methods=['GET', 'POST'])
def add_comment(user_id, trial_id):
    """
    Function to add a comment to a specific trial
    """
    if request.method == 'POST':
        user_comment = request.form.get('user_comment')
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        comment = {
            'user_id': user_id,
            'trial_id': trial_id,
            'user_comments': user_comment,
            'username': user["fname"],
            'posted_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        mongo.db.comments.insert_one(comment)
        flash('Review successfully added!')
    return redirect(url_for('clinical_trials'))


@app.route('/edit_reviews/<comment_id>', methods=['GET', 'POST'])
def edit_reviews(comment_id):
    """
    Function to edit comments/reviews and redirects back to clinical trials
    """
    comment_to_edit = mongo.db.comments.find_one({
        "_id": ObjectId(comment_id)})

    user = mongo.db.users.find_one({'_id': ObjectId(session.get('user'))})

    if request.method == "POST":

        update_comment = {"$set": {
                'user_id': session.get('user'),
                'trial_id': request.form.get('trial_api_id'),
                'user_comments': request.form.get('user_comments'),
                'username': user["fname"],
                'posted_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }}

        mongo.db.comments.update_one(comment_to_edit, update_comment)

        flash('Review successfully saved!')
        return redirect(url_for('clinical_trials'))

    return render_template('pages/edit_reviews.html', comment=comment_to_edit)


@app.route('/delete_reviews/<comment_id>', methods=['GET', 'POST'])
def delete_reviews(comment_id):
    """
    Function to delete comments / reviews
    """
    mongo.db.comments.delete_one({"_id": ObjectId(comment_id)})

    return redirect(url_for('clinical_trials'))


@app.route('/logout')
def logout():
    # clear session cookies
    flash('You are now logged out!')
    session.pop('user')
    return redirect(url_for('home'))


# Error handlers

@app.errorhandler(404)
def page_not_found(error):
    error = str(error)
    return render_template('pages/error.html',
                           error=error), 404


@app.errorhandler(500)
def server_error(error):
    error = str(error)
    return render_template('pages/error.html',
                           error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
