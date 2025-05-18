from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def train_ml_model(data):
    # Convert the input list of dicts to a DataFrame
    df = pd.DataFrame(data)

    # Drop unnecessary columns (adjust based on your actual keys)
    df = df.drop(columns=['recordId', 'doctorName', 'patientName', 'diagnosticAddress', 'patientAddress', 'cid'], errors='ignore')

    # Encode categorical variables
    label_encoders = {}
    for column in ['gender', 'bloodGroup']:
        if column in df.columns:
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            label_encoders[column] = le

    # Dummy target: predict age group (e.g., age > 50 as risk)
    df['target'] = (df['age'] > 50).astype(int)

    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    print("Model training complete.")
    print(f"Accuracy on training data: {model.score(X_train, y_train):.2f}")
    print(f"Accuracy on test data: {model.score(X_test, y_test):.2f}")

    return model