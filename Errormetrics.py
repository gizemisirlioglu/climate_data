import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from xgboost import XGBRegressor
from sklearn.ensemble import VotingRegressor
from scipy.stats import ks_2samp

def load_data(file_path):
    """Veri setini yükler ve eksik değerleri kontrol eder."""
    df = pd.read_excel(file_path)
    if df.isnull().values.any():
        print("Veri setinde eksik değerler var. Lütfen kontrol edin.")
    return df

def train_and_evaluate_model(model, X, y):
    """Bir modeli eğitir ve R², MAE, RMSE gibi metrikleri döner."""
    model.fit(X, y)
    predictions = model.predict(X)
    r2 = r2_score(y, predictions)
    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    return predictions, r2, mae, rmse

def calculate_metrics(y_true, y_pred):
    """Verilen gerçek ve tahmin değerler için ek metrikleri hesaplar."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    bias = np.mean(y_true - y_pred)
    willmott_d = 1 - (np.sum((y_true - y_pred)**2) / np.sum((np.abs(y_true - np.mean(y_true)) + np.abs(y_pred - np.mean(y_true)))**2))
    return mae, rmse, bias, willmott_d

def detailed_analysis(df):
    """Min, Max ve Average sütunları için hata metriklerini hesaplar."""
    metrics = []
    columns = [
        ('idw_min', 'chelsa_min', 'worldclim_min'),
        ('idw_max', 'chelsa_max', 'worldclim_max'),
        ('idw_average', 'chelsa_average', 'worldclim_average')
    ]
    for idw_col, chelsa_col, worldclim_col in columns:
        y_true = df[idw_col]
        chelsa_pred = df[chelsa_col]
        worldclim_pred = df[worldclim_col]

        # CHELSA için metrikler
        chelsa_mae, chelsa_rmse, chelsa_bias, chelsa_d = calculate_metrics(y_true, chelsa_pred)

        # WorldClim için metrikler
        worldclim_mae, worldclim_rmse, worldclim_bias, worldclim_d = calculate_metrics(y_true, worldclim_pred)

        metrics.append({
            "Metric": idw_col.split('_')[-1].capitalize(),
            "CHELSA_MAE": chelsa_mae,
            "CHELSA_RMSE": chelsa_rmse,
            "CHELSA_Bias": chelsa_bias,
            "CHELSA_D": chelsa_d,
            "WorldClim_MAE": worldclim_mae,
            "WorldClim_RMSE": worldclim_rmse,
            "WorldClim_Bias": worldclim_bias,
            "WorldClim_D": worldclim_d
        })

    return pd.DataFrame(metrics)

# Veri yükleme
file_path = "detailed_metrics_results.xlsx"  # Hata metriklerinin olduğu Excel dosyasını buraya koyun
detailed_metrics = pd.read_excel(file_path)

file_path = r"D:\Belgelerim\Desktop\sıcaklık karşılatırma\tumveriler.xlsx"
df = load_data(file_path)

# Detaylı Analiz (Min, Max, Average)
detailed_metrics = detailed_analysis(df)
print(detailed_metrics)

# Detaylı Analiz Sonuçlarını Kaydetme
detailed_metrics.to_excel("detailed_metrics_results.xlsx", index=False)
print("Detaylı analiz sonuçları Excel dosyasına kaydedildi.")

# Willmott D değerlerini kontrol et
print(detailed_metrics[['CHELSA_D', 'WorldClim_D']])




