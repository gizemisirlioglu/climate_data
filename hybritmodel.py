import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_data(file_path):
    """Loads the dataset."""
    df = pd.read_excel(file_path)
    if df.isnull().values.any():
        print("Warning: Missing values detected in the dataset. Please check.")
    return df
    
def hybrid_model_with_ml(df):
    """Creates and evaluates a hybrid model using WorldClim and CHELSA data."""
    # Features and target
    X = df[['worldclim_average', 'chelsa_average']]  # Input variables
    y = df['idw_average']  # Target variable (actual values)

    # Random Forest Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Predictions
    df['hybrid_ml'] = model.predict(X)

    # Performance evaluation
    mae_ml = mean_absolute_error(y, df['hybrid_ml'])
    rmse_ml = np.sqrt(mean_squared_error(y, df['hybrid_ml']))
    r2_ml = r2_score(y, df['hybrid_ml'])

    # Print results
    print("Machine Learning Hybrid Model Performance:")
    print(f"MAE: {mae_ml}")
    print(f"RMSE: {rmse_ml}")
    print(f"R²: {r2_ml}")

    # Visualizations
    plot_decision_tree(model, X.columns, max_depth=3)
    plot_feature_importance(model, X.columns)
    plot_actual_vs_predicted(y, df['hybrid_ml'])
    plot_residuals(y, df['hybrid_ml'])

    return df, mae_ml, rmse_ml, r2_ml

def plot_decision_tree(model, feature_names, max_depth=3):
    """Plots a decision tree from the Random Forest model (limited depth)."""
    first_tree = model.estimators_[0]  # Select the first tree

    plt.figure(figsize=(20, 10))
    plot_tree(first_tree, feature_names=feature_names, filled=True, max_depth=max_depth)
    plt.title(f"Random Forest Decision Tree (Max Depth: {max_depth})")
    plt.savefig(f"Decision_Tree_Limited_{max_depth}.png", dpi=300)
    plt.show()
    print(f"Decision Tree Plot (Max Depth: {max_depth}) saved successfully.")

def plot_feature_importance(model, feature_names):
    """Plots feature importance in the Random Forest model."""
    importance = model.feature_importances_
    plt.figure(figsize=(8, 6))
    plt.barh(feature_names, importance, color='skyblue')
    plt.xlabel("Feature Importance")
    plt.title("Importance of Features in the Model")
    plt.savefig("Feature_Importance.png", dpi=300)
    plt.show()
    print("Feature Importance Plot saved successfully.")

def plot_actual_vs_predicted(y_true, y_pred):
    """Plots actual vs predicted values."""
    plt.figure(figsize=(8, 8))
    plt.scatter(y_true, y_pred, alpha=0.5, label="Predictions")
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], color='red', linestyle='--', label="Perfect Prediction Line")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted Values")
    plt.legend()
    plt.grid(True)
    plt.savefig("Actual_vs_Predicted.png", dpi=300)
    plt.show()
    print("Actual vs Predicted Plot saved successfully.")

def plot_residuals(y_true, y_pred):
    """Plots residuals (errors) for predictions."""
    residuals = y_true - y_pred
    plt.figure(figsize=(8, 6))
    plt.hist(residuals, bins=30, color='orange', alpha=0.7)
    plt.axvline(x=0, color='red', linestyle='--', label="Zero Error Line")
    plt.xlabel("Residuals (Actual - Predicted)")
    plt.ylabel("Frequency")
    plt.title("Residuals Distribution")
    plt.legend()
    plt.grid(True)
    plt.savefig("Residuals_Distribution.png", dpi=300)
    plt.show()
    print("Residuals Distribution Plot saved successfully.")

file_path = r"data_set.xlsx"

# Load data
df = load_data(file_path)

# Create and evaluate the hybrid model
df, mae_ml, rmse_ml, r2_ml = hybrid_model_with_ml(df)

# Save performance results
results = pd.DataFrame({
    'Metric': ['MAE', 'RMSE', 'R²'],
    'Value': [mae_ml, rmse_ml, r2_ml]
})
results.to_excel("Hybrid_Model_Performance.xlsx", index=False)
print("Hybrid model performance results saved.")
