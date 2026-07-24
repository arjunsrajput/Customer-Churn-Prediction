import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load training data and model
df_train = pd.read_csv("first_telc.csv")

if 'Unnamed: 0' in df_train.columns:
    df_train.drop('Unnamed: 0', axis=1, inplace=True)
    
model = pickle.load(open("model.sav", "rb"))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def predict():

    values = []

    for i in range(1, 20):
        values.append(request.form.get(f"query{i}"))

    columns = [
        'SeniorCitizen',
        'MonthlyCharges',
        'TotalCharges',
        'gender',
        'Partner',
        'Dependents',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'tenure'
    ]

    new_customer = pd.DataFrame([values], columns=columns)

    df = pd.concat([df_train, new_customer], ignore_index=True)

    labels = [
        "1 - 12",
        "13 - 24",
        "25 - 36",
        "37 - 48",
        "49 - 60",
        "61 - 72"
    ]

    df['tenure_group'] = pd.cut(
        df['tenure'].astype(int),
        bins=[1,13,25,37,49,61,73],
        labels=labels,
        right=False
    )

    df.drop('tenure', axis=1, inplace=True)

    categorical_cols = [
        'gender',
        'Partner',
        'Dependents',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
        'tenure_group'
    ]

    final_df = pd.get_dummies(df, columns=categorical_cols)

    prediction = model.predict(final_df.tail(1))
    probability = model.predict_proba(final_df.tail(1))

    if prediction[0] == 1:
        output1 = "This customer is likely to churn."
    else:
        output1 = "This customer is likely to stay."

    output2 = f"Confidence: {probability[0][1] * 100:.2f}%"

    return render_template(
        "home.html",
        output1=output1,
        output2=output2,
        **{f'query{i}': request.form.get(f'query{i}') for i in range(1,20)}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)