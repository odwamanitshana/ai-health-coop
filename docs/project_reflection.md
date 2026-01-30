# Project Reflection – Diabetes Risk Predictor

## 1. Problem Overview

- Goal: Build a small web app that predicts diabetes risk from basic clinical features.
- Dataset: Pima Indians Diabetes Dataset (768 rows, 8 features + binary outcome).

## 2. Data Preparation

- Steps:
  - Loaded CSV, inspected missing values and class balance.
  - Split into train/validation/test sets (e.g. 70/15/15, stratified on outcome).
  - Standardized features for models that need it (Logistic Regression, Neural Network) using `StandardScaler`.

## 3. Models

- Logistic Regression
  - Baseline linear model on scaled features.
- Random Forest
  - Ensemble of decision trees on raw features.
- Neural Network (Keras)
  - Feed-forward network with two hidden layers (16 and 8 units, ReLU, sigmoid output).

## 4. Evaluation

- Logistic Regression – validation accuracy ≈ 0.73
- Random Forest – validation accuracy ≈ 0.76
- Neural Network – test accuracy ≈ 0.76

Random Forest performed best on validation data while being relatively simple to train and deploy, so it was chosen as the production model for the app. The neural network reached similar performance but required more complexity (TensorFlow, additional tuning).

## 5. App and Deployment

- Implemented a Streamlit app (`app.py`) that:
  - Accepts 8 user inputs corresponding to the dataset features.
  - Uses the trained Random Forest to estimate diabetes risk.
  - Displays both a probability and a risk message with a clear disclaimer.
- Deployed the app on Streamlit Cloud using:
  - A GitHub repository for source code and models.
  - `requirements.txt` to reproduce the environment.

## 6. Challenges and Learnings

- Environment management:
  - Needed to align the Jupyter kernel with the project virtual environment.
  - Encountered issues installing and importing TensorFlow and resolved them by fixing the interpreter.
- Modeling:
  - Saw that more complex models (neural networks) do not always outperform simpler ones on small tabular datasets.
- Deployment:
  - Learned how to package a Python ML project with `requirements.txt`, Streamlit, and a cloud deployment platform.

## 7. Possible Future Work

- Add more evaluation metrics (precision, recall, ROC-AUC).
- Add option in the UI to compare predictions from Logistic Regression and the Neural Network.
- Improve calibration and explainability (e.g., feature importance, SHAP values).
- Experiment with threshold tuning for different risk categories.