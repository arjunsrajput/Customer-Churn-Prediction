# Customer Churn Prediction System

A Machine Learning-based web application that predicts whether a telecom customer is likely to churn based on demographic information, subscription details, service usage patterns, and billing history.

The project covers the complete Data Science lifecycle including Exploratory Data Analysis (EDA), Data Preprocessing, Class Imbalance Handling, Model Development, Model Evaluation, and Deployment using Flask and Docker.

---

# Live Demo

Hugging Face Space:

https://huggingface.co/spaces/arjunsrajput/customer-churn-prediction

---

# Problem Statement

Customer churn is one of the most critical challenges faced by subscription-based businesses. Acquiring a new customer is significantly more expensive than retaining an existing one.

The objective of this project is to predict whether a customer is likely to leave the telecom service so that businesses can proactively implement retention strategies.

---

# Dataset Information

The dataset contains telecom customer information including demographics, account details, service subscriptions, and billing information.

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Total Customers | 7043 |
| Features | 21 |
| Average Tenure | 32.37 Months |
| Average Monthly Charges | 64.76 |
| Maximum Tenure | 72 Months |
| Churn Rate | 26.54% |
| Retention Rate | 73.46% |

### Target Variable

| Value | Meaning |
|---------|----------|
| Yes | Customer Churned |
| No | Customer Retained |

---

# Project Structure

text customer-churn-prediction/ │ ├── app.py ├── model.sav ├── first_telc.csv ├── CustomerChurn.csv ├── requirements.txt ├── Dockerfile │ ├── CustomerChurn-EDA.ipynb ├── ModelBuilding.ipynb │ ├── templates/ │   └── home.html │ └── README.md 

---

# Exploratory Data Analysis

Comprehensive EDA was performed to understand customer behavior and identify patterns contributing to churn.

### Analysis Performed

- Churn Distribution Analysis
- Gender-wise Churn Analysis
- Senior Citizen Analysis
- Partner and Dependents Analysis
- Contract Type Analysis
- Internet Service Analysis
- Monthly Charges Distribution
- Total Charges Distribution
- Tenure Analysis
- Payment Method Analysis
- Online Security Analysis
- Online Backup Analysis
- Device Protection Analysis
- Tech Support Analysis
- Streaming Services Analysis

---

# Key Insights

### Class Imbalance

The dataset was highly imbalanced.

| Churn Status | Percentage |
|--------------|------------|
| No Churn | 73.46% |
| Churn | 26.54% |

This imbalance negatively affects the model's ability to correctly identify churn customers.

### Customer Behavior Insights

- Customers with shorter tenure are more likely to churn.
- Month-to-month contract customers exhibit the highest churn rate.
- Customers lacking Online Security and Tech Support are more likely to leave.
- Customers with higher monthly charges show increased churn tendencies.
- Long-term contracts significantly improve customer retention.

---

# Data Preprocessing

Several preprocessing steps were applied before model training.

### Missing Value Treatment

- Converted TotalCharges to numeric format.
- Removed invalid records.
- Handled missing values.

### Feature Engineering

Created:

text tenure_group 

Customers were categorized into tenure ranges:

- 1–12 Months
- 13–24 Months
- 25–36 Months
- 37–48 Months
- 49–60 Months
- 61–72 Months

### Encoding

Applied One-Hot Encoding to categorical variables:

- Gender
- Partner
- Dependents
- Internet Service
- Contract Type
- Payment Method
- Security Services
- Streaming Services

---

# Handling Class Imbalance

Since the dataset was highly imbalanced, SMOTEENN was used.

### SMOTEENN

SMOTEENN combines:

#### SMOTE

Synthetic Minority Oversampling Technique

Benefits:

- Generates synthetic churn samples.
- Increases minority class representation.

#### ENN

Edited Nearest Neighbour

Benefits:

- Removes noisy observations.
- Improves decision boundaries.

This resulted in a more balanced dataset and significantly improved model performance.

---

# Machine Learning Models

Two classification algorithms were evaluated.

## 1. Decision Tree Classifier

### Performance Before SMOTEENN

| Metric | Score |
|----------|----------|
| Accuracy | 80.00% |
| Precision | 64% |
| Recall | 54% |
| F1 Score | 58% |

### Performance After SMOTEENN

| Metric | Score |
|----------|----------|
| Accuracy | 93.85% |
| Precision | 95% |
| Recall | 95% |
| F1 Score | 95% |

---

## 2. Random Forest Classifier

### Performance Before SMOTEENN

| Metric | Score |
|----------|----------|
| Accuracy | 80.17% |
| Precision | 66% |
| Recall | 47% |
| F1 Score | 55% |

### Performance After SMOTEENN

| Metric | Score |
|----------|----------|
| Accuracy | 94.16% |
| Precision | 93% |
| Recall | 96% |
| F1 Score | 95% |

---

# Model Comparison

| Model | Accuracy |
|----------|----------|
| Decision Tree | 80.00% |
| Decision Tree + SMOTEENN | 93.85% |
| Random Forest | 80.17% |
| Random Forest + SMOTEENN | 94.16% |

---

# Final Model Selection

### Selected Model

Random Forest Classifier + SMOTEENN

### Why Random Forest?

- Highest Accuracy
- Better Generalization
- Strong Recall for Churn Detection
- Robust against Overfitting
- Better Performance on Balanced Dataset

### Final Accuracy

text 94.16% 

The trained model is stored as:

text model.sav 

and is used by the Flask application for real-time predictions.

---

# Web Application

A Flask-based web application was developed to allow users to interact with the trained model.

### Input Features

- Senior Citizen
- Gender
- Partner
- Dependents
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Tenure

### Output

- Churn Prediction
- Confidence Score

---

# Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-Learn
- Imbalanced-Learn

## Web Development

- Flask
- HTML
- Bootstrap

## Deployment

- Docker
- Hugging Face Spaces

---

# Installation

Clone the repository:

bash git clone https://github.com/arjunsrajput/customer-churn-prediction.git cd customer-churn-prediction 

Install dependencies:

bash pip install -r requirements.txt 

Run the application:

bash python app.py 

Open:

text http://127.0.0.1:5000 

---

# Docker Deployment

Build Docker image:

bash docker build -t churn-prediction . 

Run container:

bash docker run -p 7860:7860 churn-prediction 

---

# Future Improvements

- Explainable AI using SHAP
- Customer Retention Recommendations
- REST API Development
- Feature Importance Dashboard
- Authentication System
- Database Integration
- Cloud-Native Deployment

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Exploratory Data Analysis
- Feature Engineering
- Handling Imbalanced Data
- Classification Algorithms
- Model Evaluation
- Flask Development
- Docker Deployment
- Machine Learning Deployment

---

# Author

Arjun Singh Rajput

Master of Computer Applications (MCA)  
National Institute of Technology, Tiruchirappalli

GitHub: https://github.com/arjunsrajput

---

# License

This project is developed for educational and learning purposes.