
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load cleaned dataset
df = pd.read_csv("data/cleaned_car_data.csv")

print("DATASET LOADED SUCCESSFULLY")
print("Dataset shape:", df.shape)

# 2. Select input features
X = df[
    [
        "Year",
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type",
        "Seller_Type",
        "Transmission",
        "Owner"
    ]
]

# 3. Select target variable
y = df["Selling_Price"]

# 4. Separate numerical and categorical columns
numeric_features = [
    "Year",
    "Present_Price",
    "Kms_Driven",
    "Owner"
]

categorical_features = [
    "Fuel_Type",
    "Seller_Type",
    "Transmission"
]

# 5. Preprocess categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         categorical_features)
    ],
    remainder="passthrough"
)

# 6. Create Random Forest model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ]
)

# 7. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# 8. Train model
print("\nTraining model...")
model.fit(X_train, y_train)

print("MODEL TRAINED SUCCESSFULLY!")

# 9. Make predictions
y_pred = model.predict(X_test)

# 10. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nMODEL PERFORMANCE")
print("MAE:", round(mae, 2), "Lakhs")
print("RMSE:", round(rmse, 2), "Lakhs")
print("R2 Score:", round(r2, 2))

# 11. Save trained model
joblib.dump(model, "models/car_price_model.pkl")

print("\nMODEL SAVED SUCCESSFULLY!")
print("File: models/car_price_model.pkl")