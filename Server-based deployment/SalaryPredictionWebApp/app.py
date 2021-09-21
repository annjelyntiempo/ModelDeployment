#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pickle

from flask import Flask, request, jsonify, render_template


# In[8]:


model = pickle.load(open('salaryregressionmodel.pkl', 'rb'))


# In[9]:


app = Flask(__name__, template_folder='templates')


# In[10]:


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
        yearsnum = request.form['yearsnum']
        yearsnum = float(yearsnum)
        
        prediction = model.predict([[yearsnum]])
        
        # online train
        model.fit(yearsnum, prediction)
    
        return render_template('index.html', result=prediction[0])


# In[11]:


if __name__ == '__main__':
    app.run(host="128.134.65.180")


# In[ ]:




