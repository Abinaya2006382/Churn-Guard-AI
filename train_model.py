import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load both datasets

train_df = pd.read_csv(
    "data/customer_churn_dataset-training-master.csv"
)

test_df = pd.read_csv(
    "data/customer_churn_dataset-testing-master.csv"
)


# Combine datasets

df = pd.concat(
    [train_df, test_df],
    axis=0
)


# Remove missing values

df = df.dropna()


print("Dataset shape:")
print(df.shape)


# Separate input and output

X = df.drop("Churn", axis=1)
y = df["Churn"]


# Convert text columns

encoder = LabelEncoder()

for col in X.columns:
    if X[col].dtype == "object":
        X[col] = encoder.fit_transform(X[col])


# Split properly

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Model

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)


# Train

model.fit(
    X_train,
    y_train
)


# Prediction

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)


# Results

print("============================")

print(
"Training Accuracy:",
accuracy_score(y_train, train_pred)*100,
"%"
)

print(
"Testing Accuracy:",
accuracy_score(y_test, test_pred)*100,
"%"
)

print("============================")


print(classification_report(
    y_test,
    test_pred
))


# Save model

joblib.dump(
    model,
    "models/churn_model.pkl"
)


print("Model saved successfully")