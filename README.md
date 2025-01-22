README: Hybrid Climate Model Scripts

This repository contains Python scripts developed for a study on hybrid climate modeling, with a specific focus on interpolating and validating temperature data for the Eastern Black Sea Region. The scripts facilitate data processing, error analysis, and visualization of results. Below is a brief description of each script and its purpose.

---

## Repository Contents

1. **`Errormetrics.py`**
   - **Purpose**: Computes performance metrics to evaluate model accuracy.
   - **Key Features**:
     - Calculates Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and Bias.
     - Includes functions for validating observed data against predictions.
   - **Usage**:
     - Import the script or run it standalone to assess model error metrics.

2. **`Hybritmodel.py`**
   - **Purpose**: Implements the hybrid model combining WorldClim, CHELSA datasets, and observed data.
   - **Key Features**:
     - Trains a Random Forest model to improve interpolation accuracy.
     - Integrates meteorological station data with climate datasets.
     - Outputs predictions with enhanced reliability.
   - **Usage**:
     - Use as a core script for hybrid model development and predictions.

3. **`Rastermerge.py`**
   - **Purpose**: Merges and processes raster datasets for spatial analysis.
   - **Key Features**:
     - Combines raster layers (e.g., WorldClim and CHELSA) into a unified dataset.
     - Ensures consistency in resolution and extent across datasets.
   - **Usage**:
     - Use for preprocessing raster data before hybrid model training.

4. **`Spyder_plot.py`**
   - **Purpose**: Generates visualizations for performance analysis.
   - **Key Features**:
     - Creates spider (radar) plots for comparing model metrics (e.g., MAE, RMSE, R²).
     - Supports customization for publication-quality plots.
   - **Usage**:
     - Run to produce visualizations of the model's performance.

---

How to Use

1. **Preprocessing**:
   - Use `Rastermerge.py` to merge and preprocess raster datasets.
2. **Model Training**:
   - Run `Hybritmodel.py` to train the hybrid model using preprocessed data.
3. **Validation**:
   - Use `Errormetrics.py` to evaluate model accuracy with performance metrics.
4. **Visualization**:
   - Use `Spyder_plot.py` to generate visual representations of model results.

---

Requirements

- **Python Version**: Python 3.7 or higher
- **Libraries**:
  - `NumPy`
  - `Pandas`
  - `Matplotlib`
  - `Scikit-learn`
  - `GDAL` (for raster data processing)

Install the dependencies using:
```bash
pip install numpy pandas matplotlib scikit-learn gdal
