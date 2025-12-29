# Wildfire Guard (NASA VIIRS Fire Detection and FRP Modeling)

Automates downloads of NASA FIRMS VIIRS SNPP NRT fire detections and models Fire Radiative Power (FRP). Includes a reproducible pipeline from data ingest to EDA to regression modeling, plus map visualizations of active fires.

## What it does
- Pulls VIIRS SNPP NRT fire detections from NASA FIRMS for a chosen time window (e.g., last 1–10 days)
- Cleans and explores detections in an EDA notebook
- Trains a regression model to predict / model FRP from available features
- Produces fire maps for quick spatial inspection

## Pipeline
| Stage | Location | Notes |
|------|----------|------|
| Data ingest | `src/wildfire_guard/firms_api.py` | Pull 1–10 day CSV window |
| EDA | `notebooks/01_eda_viirs.ipynb` | Data exploration and plots |
| Modeling | `notebooks/02_frp_regression.ipynb` | RandomForest baseline, log-RMSE ≈ 0.29 |
| Environment | `environment.yml` | Conda reproducibility |

## Results
- Baseline model: RandomForest regression
- Metric: log-RMSE ≈ 0.29 (see `notebooks/02_frp_regression.ipynb` for details)

## Setup
```bash
conda env create -f environment.yml
conda activate wildfire
```

Run (Download and Analyze)
Download last N days of detections (example: 7):

```
python src/wildfire_guard/firms_api.py 7
```
Start notebooks:

```
jupyter notebook
```
Open:
```
notebooks/01_eda_viirs.ipynb
notebooks/02_frp_regression.ipynb
```
Outputs:
Downloaded FIRMS CSV data (wherever your script saves it)

EDA plots and summary tables in 01_eda_viirs.ipynb

Model training, evaluation, and feature analysis in 02_frp_regression.ipynb


Fire map visualization 

Map of Fires
<img width="800" height="655" alt="image" src="https://github.com/user-attachments/assets/a14f1ea6-d64d-4279-857f-ef706be6b722" />

Notes / Next Improvements
Add CLI flags: output directory, bounding box, satellite/product selection

Add time-aware validation split and stronger baselines (XGBoost/LightGBM)

Package as an installable module and simple dashboard 
