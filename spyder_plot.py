import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor

def load_data(file_path):
    """Loads the dataset."""
    df = pd.read_excel(file_path)
    if df.isnull().values.any():
        print("There are missing values in the dataset. Please check.")
    return df

def hybrid_model_with_ensemble(df):
    """Combines Random Forest, Gradient Boosting, and XGBoost to create a hybrid model."""
    
    # Features and target variable
    X = df[['worldclim_average', 'chelsa_average']]  # Features
    y = df['idw_average']  # Target variable

    Model 1: Random Forest 
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X, y)
    df['rf_prediction'] = rf_model.predict(X)

    Model 2: Gradient Boosting
    gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    gb_model.fit(X, y)
    df['gb_prediction'] = gb_model.predict(X)

    Model 3: XGBoost 
    xgb_model = XGBRegressor(n_estimators=100, random_state=42)
    xgb_model.fit(X, y)
    df['xgb_prediction'] = xgb_model.predict(X)

    Hybrid Prediction 
    # Assign weights to models (e.g., 50% RF, 30% GB, 20% XGBoost)
    weight_rf = 0.5
    weight_gb = 0.3
    weight_xgb = 0.2

    df['hybrid_prediction'] = (
        weight_rf * df['rf_prediction'] +
        weight_gb * df['gb_prediction'] +
        weight_xgb * df['xgb_prediction']
    )

    mae_hybrid = mean_absolute_error(y, df['hybrid_prediction'])
    rmse_hybrid = np.sqrt(mean_squared_error(y, df['hybrid_prediction']))
    r2_hybrid = r2_score(y, df['hybrid_prediction'])
    print("Hybrid Model Performance (Ensemble):")
    print(f"MAE: {mae_hybrid}")
    print(f"RMSE: {rmse_hybrid}")
    print(f"R²: {r2_hybrid}")

    return df, mae_hybrid, rmse_hybrid, r2_hybrid

def plot_hybrid_analysis(df):
    """Analyzes the contributions of hybrid predictions."""
    plt.figure(figsize=(8, 6))
    plt.bar(['Random Forest', 'Gradient Boosting', 'XGBoost'], 
            [df['rf_prediction'].mean(), df['gb_prediction'].mean(), df['xgb_prediction'].mean()], 
            color=['blue', 'green', 'orange'], alpha=0.6)
    plt.title("Hybrid Model Contributions")
    plt.xlabel("Algorithms")
    plt.ylabel("Average Predictions")
    plt.show()

file_path = r"data_set"  # File path
df = load_data(file_path)

# Build the hybrid model and evaluate its performance
df, mae_hybrid, rmse_hybrid, r2_hybrid = hybrid_model_with_ensemble(df)

# Generate visualizations
plot_hybrid_analysis(df)
