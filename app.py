import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bravado.client import SwaggerClient
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


@app.route('/my_trials')
def my_trials():
    trials = mongo.db.trials.find()
    return render_template('pages/mytrials.html', trials=trials)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # switch to False before delivering project
            debug=True)
