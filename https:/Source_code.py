import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Load your dataset (replace with actual path to CSV file)
data = pd.read_csv('transactions.csv')

# Example feature and label setup
features = ['amount', 'location_score', 'hour', 'device_score']
X = data[features]
y = data['is_fraud']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model and scaler
joblib.dump(model, 'fraud_model.pkl')
joblib.dump(scaler, 'scaler.pkl'

def is_fraudulent(transaction):
    """
    transaction: dict with keys 'amount', 'location_score', 'hour', 'device_score'
    """
    model = joblib.load('fraud_model.pkl')
    scaler = joblib.load('scaler.pkl')

    features = [[
        transaction['amount'],
        transaction['location_score'],
        transaction['hour'],
        transaction['device_score']
    ]]
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    return prediction[0] == 1

# Example usage
transaction = {
    'amount': 2500,
    'location_score': 3,
    'hour': 2,
    'device_score': 0.8
}

if is_fraudulent(transaction):
    print("Transaction flagged as FRAUDULENT. Blocking.")
else:
    print("Transaction approved.")
