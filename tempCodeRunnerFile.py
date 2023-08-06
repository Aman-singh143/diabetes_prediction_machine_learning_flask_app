from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import plotly.express as px

app = Flask(__name__)

# Load the scaler and model
scaler = pickle.load(open("model/StandardScaler.pkl", "rb"))
model = pickle.load(open("model/model_prediction.pkl", "rb"))

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    result = ""
    chart_html = ""

    if request.method == "POST":
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = float(request.form.get("Age"))

        new_data = scaler.transform(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        )
        predict = model.predict(new_data)

        if predict[0] == 1:
            result = "Diabetic"
        else:
            result = "Non-Diabetic"

        # Create a dictionary with feature names and their corresponding values
        features = {
            'Pregnancies': Pregnancies,
            'Glucose': Glucose,
            'Blood Pressure': BloodPressure,
            'Skin Thickness': SkinThickness,
            'Insulin': Insulin,
            'BMI': BMI,
            'Diabetes Pedigree Function': DiabetesPedigreeFunction,
            'Age': Age
        }

        # Create a bar chart using Plotly
        fig = px.bar(x=list(features.keys()), y=list(features.values()), title='Feature Values')
        chart_html = fig.to_html(full_html=False)

    return render_template("singleresult.html", result=result, chart_html=chart_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
