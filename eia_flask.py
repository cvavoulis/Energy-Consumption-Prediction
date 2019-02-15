

# coding: utf-8

# In[1]:

# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pymongo
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import rcParams
rcParams['figure.figsize']=10,6
import numpy as np
import pandas as pd
import requests
from config import api_key
import eia
import datetime
import re
from sqlalchemy import create_engine
from datetime import datetime
import statsmodels.api as sm

from pyramid.arima import auto_arima

import plotly
from plotly.plotly import plot_mpl
plotly.tools.set_credentials_file(username='cvavoulis', api_key='idvhBcrfyB7GaC6jqdr8')
from statsmodels.tsa.seasonal import seasonal_decompose

#client = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = client["eia_db"]


app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)


df=pd.read_csv("clean_data.csv")

def model(day):
    # day= **calculate # months from last day in data set
    results.predict(548,day)
    # build the model -- mostly the same code as othe file, without print statements and plots
    return predictions

@app.route("/model", method="POST")
def forecast():
    day=request.form["day"]
    model(day)

    return jsonify(predictions)
    

