"""Train model script for Car Price Prediction
Author: Surya Prakash
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

df = pd.read_csv('../data/old_car_data.csv')

# Replace 'PRICE_COLUMN' with actual target column name
TARGET = 'Selling_Price'

# Basic preprocessing (numeric columns only)
X = df.select_dtypes(include=['number']).drop(columns=[TARGET])
y = df[TARGET].dropna()
X = X.loc[y.index].fillna(X.median())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print('R2:', r2_score(y_test, preds))
print('MAE:', mean_absolute_error(y_test, preds))
print('RMSE:', mean_squared_error(y_test, preds, squared=False))
