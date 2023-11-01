from flask import Flask, redirect, request, render_template
import pickle
import numpy as np

app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("salary_prediction.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm= request.form ['name']
    age= float(request.form ['age'])
    gender=int(request.form['gender'])
    edu_level=int(request.form['education_level'])
    Exp = float(request.form['Exp'])

    mymodel= pickle.load(open('salary_pred_model.pkl', 'rb'))
    sal = round(mymodel.predict([[age,gender,edu_level,Exp]])[0],2)
    return render_template("response.html",name =nm, salary =sal)

if __name__ == "__main__" :
    app.run(debug=True)

