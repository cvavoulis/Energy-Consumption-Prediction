

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
from pandas.tseries.offsets import DateOffset
#client = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = client["eia_db"]


app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/"
# mongo = PyMongo(app)
# app = Flask(__name__)

# app.config["EIA_DATA"] = pd.read_csv("clean_data.csv")
# data=pd.read_csv(app)

raw_df=pd.read_csv("clean_data.csv")

@app.route("/")
def index():
    print(raw_df)
    return render_template("index.html", raw_df=raw_df)

def model(day):
    # day= **calculate # months from last day in data set
    day=700
    # results.predict(548,day)
    model=sm.tsa.statespace.SARIMAX(raw_df["Total Primary Energy Consumption, Monthly (Trillion Btu)"],order=(1,1,1), seasonal_order=(2,1,1,12))
    results=model.fit()
    # predictions = raw_df["Forecast"].tail(49)
    actual = raw_df["Total Primary Energy Consumption, Monthly (Trillion Btu)"][500:]
    future_dates=[raw_df.index[-1] + DateOffset(months=x) for x in range (0,500)]
    futures_datest_df=pd.DataFrame(index=future_dates[1:], columns=raw_df.columns)
    future_df=pd.concat([raw_df, futures_datest_df])
    predictions=results.predict(start= 548, end= day, dynamic=True)
    # future_df["Forecast"]=results.predict(start= 548, end= day, dynamic=True)
    # build the model -- mostly the same code as othe file, without print statements and plots
    return predictions



@app.route("/model", methods=["POST", "GET"])
def forecast():
    if request.method=="POST":
        day=request.form["day"]
        print(day)
        model(day)
        return redirect("/", code=302)
    return render_template("form.html")
    # return jsonify(predictions)
    





# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         df = pd.read_csv(request.files.get('clean_data.csv'))
#         return render_template('form.html', shape=df.shape)
#     return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)

    