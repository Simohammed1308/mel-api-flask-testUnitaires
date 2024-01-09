
# Le lien de l'API  déployée sur heroku : https://mb-oc-p7-api.herokuapp.com/

import flask
from flask import Flask
from flask import request, jsonify
import joblib
import pandas as pd
import shap
import json
import numpy as np

def create_app(config):

    app = Flask(__name__)
    app.config["DEBUG"] = True

    app.config.from_object(config)

    #PATH = './data/final/'

    #df = pd.read_pickle("df.gz")
    #print('df shape = ', df.shape)

    #PATH = './data/preprocessed_data/'
    #df = pd.read_csv(PATH+'df_final.csv')


    #df = pd.read_pickle("df.gz")
    #print('df shape = ', df.shape)

    #df = pd.read_csv('df2.csv', nrows=200)
    #print('data_test shape = ', df.shape)

    #df = pd.read_csv('df4.csv')
    #print('df shape = ', df.shape)

    #df = pd.read_csv('data_test.csv', nrows=200)
    #print('data_test shape = ', df.shape)

    #PATH_1 = './data/preprocessed_data/'
    #df = pd.read_csv(PATH_1+'data_global.csv', nrows=200)
    #print('data_train shape = ', df.shape)



    #Chargement du modèle
    #load_clf = joblib.load("model.joblib")
    #explainer = joblib.load("shap_explainer.joblib")

    #Premiers pas sur l'API
    @app.route('/index')
    def index():
        return 'Welcome to my Flask API!'

    @app.route('/score_min/', methods=['GET'])
    def score_min():
        return {"score_min" : 0.55}


    return app


# Lancement de l'application

app = create_app({"TESTING": False})

if __name__ == "__main__":
    app.run()
