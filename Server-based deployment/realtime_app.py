#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import pickle

from flask import Flask, request, jsonify, render_template


# In[10]:


app = Flask(__name__, template_folder='templates')


# In[11]:


@app.route('/', methods=['GET', 'POST'])
def index():
    
    model = pickle.load(open('salaryregressionmodel.pkl', 'rb'))
    
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
        yearsnum = request.form['yearsnum']
        yearsnum = float(yearsnum)
        
        prediction = model.predict([[yearsnum]])
        
        # realtime training
        model.fit([[yearsnum]], [prediction[0]])
        # saving model
        pickle.dump(model, open('salaryregressionmodel.pkl', 'wb'))
    
        return render_template('index.html', result=prediction[0])


# In[12]:


if __name__ == '__main__':
    app.run(host="128.134.65.180")

