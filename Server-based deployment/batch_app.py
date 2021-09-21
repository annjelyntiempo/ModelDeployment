#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import pickle

from flask import Flask, request, jsonify, render_template


# In[6]:


app = Flask(__name__, template_folder='templates')


# In[7]:


@app.route('/', methods=['GET', 'POST'])
def index():
    
    model = pickle.load(open('salaryregressionmodel.pkl', 'rb'))
    dataset = pd.read_csv('Salary_Data.csv')
    
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
        yearsnum = request.form['yearsnum']
        yearsnum = float(yearsnum)
        
        prediction = model.predict([[yearsnum]])
        
        # batch training
        new_data = {'YearsExperience': [yearsnum], 'Salary': [prediction[0]]}
        df = pd.DataFrame(new_data)
        df.to_csv('Salary_data.csv', mode='a', index=False, header=False)
        if len(dataset) > 40:
            new_data = dataset.drop(dataset.head(30).index, axis=0)
            X = new_data.iloc[:, :-1].values
            y = new_data.iloc[:, 1].values
            model.fit(X, y)
            # saving model
            pickle.dump(model, open('salaryregressionmodel.pkl', 'wb'))
    
        return render_template('index.html', result=prediction[0])


# In[8]:


if __name__ == '__main__':
    app.run(host="128.134.65.180")

