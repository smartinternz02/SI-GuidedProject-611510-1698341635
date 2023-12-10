import pickle
from flask import Flask, render_template,request
import pandas as pd
import numpy as np
model = pickle.load(open("svc_model.pkl",'rb'))
scale = pickle.load(open("scale.pkl",'rb'))
ct = joblib.load('column')
@app.route('/')
def home():
    return render_template('first_page.html')
@app.route('/form')
def form():
    return render_template('form_page.html')
@app.route('/guest', methods = ["POST"])
def Guest():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    e = request.form['e']
    f = request.form['f']
    g = request.form['g']
    h = request.form['h']
    i = request.form['i']
    j = request.form['j']
    k = request.form['k']
    l = request.form['l']
    m = request.form['m']
    data = [[a,b,c,d,e,f,g,h,i,j,k,l,m]]
    data = ct.transform(data)
    data = scale.fit_transform(data)
    prediction = model.predict(data)
    if prediction==0:
        session['output'] = 'Yes, with the help of meteorological and geospatial features we suspect a strong possibility of the occurence of Lumpy skin disease in this area'
    else: session['output'] = 'no, with the help of meteorogical and geospatial features we suspect a less posibility of the occurence of the Lumpy skin disease in this area'
    
    return predict()

    if__name__=='__main__'
    app.run()
    
