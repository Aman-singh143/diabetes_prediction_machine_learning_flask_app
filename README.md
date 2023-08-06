# Diabetes Prediction Web Application using Machine Learning and Flask

![GitHub](https://img.shields.io/github/license/Aman-singh143/diabetes_prediction_machine_learning_flask_app)

## Introduction

The **Diabetes Prediction Web Application** is a user-friendly platform that harnesses the power of machine learning to predict the likelihood of an individual having diabetes based on specific input features. Developed using Flask, a lightweight web framework for Python, and powered by scikit-learn, a renowned machine learning library, the application offers both accuracy and accessibility. Bootstrap is utilized for elegant styling, while Chart.js enhances data visualization.

## Live View

Experience the live view of the app: [Diabetes Prediction Web App](https://diabetes-prediction-ml-flask-app.onrender.com/)

## Dataset Overview

The project relies on the Pima Indians Diabetes Database, encompassing data from 768 female patients of Pima Indian heritage. This dataset features 8 input parameters and 1 binary target variable:

1. Pregnancies: Frequency of pregnancies
2. Glucose: Plasma glucose concentration after a 2-hour oral glucose tolerance test
3. BloodPressure: Diastolic blood pressure (mm Hg)
4. SkinThickness: Triceps skin fold thickness (mm)
5. Insulin: 2-hour serum insulin (mu U/ml)
6. BMI: Body mass index (weight in kg / (height in m)^2)
7. DiabetesPedigreeFunction: Diabetes pedigree function
8. Age: Age in years

The target variable (Outcome) indicates diabetes presence (1) or absence (0). The dataset is not only imbalanced but also contains instances of missing values, represented as zeros in certain features.

## Machine Learning Model

A Logistic Regression classifier serves as the backbone of this project's machine learning model. Acknowledged for its simplicity and proficiency in binary classification, the model undergoes training through 10-fold cross-validation. This results in a test set accuracy of 77.6%. All relevant model coefficients and performance metrics are securely stored within the designated "model" folder.

## Web Application Features

The web application seamlessly integrates two main pages: the home page and the prediction page. The home page provides an insightful overview of the project, the dataset, and facilitates easy navigation to the prediction page. On the prediction page, users are prompted to input values for the 8 features. Upon submission, a detailed prediction outcome is generated. This includes a conclusive determination of the likelihood of diabetes, accompanied by the corresponding probability. A dynamic pie chart vividly illustrates the distribution of positive and negative cases within the dataset.

## Getting Started

To launch this project, ensure that Python 3 and pip are installed on your system. Necessary packages can be installed via:

```bash
pip install -r requirements.txt
```

Following package installation, run the app using:

```bash
python app.py
```

Access the application via your web browser at http://127.0.0.1:5000/ to leverage its advanced prediction functionality .

## Live Demo

Visit the live demo of the Diabetes Prediction Web Application and start making accurate diabetes predictions based on your input data. For more details, explore the [GitHub repository](https://github.com/Aman-singh143/diabetes_prediction_machine_learning_flask_app).

