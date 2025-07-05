**Goal**  
Automate NASA VIIRS SNPP NRT fire-detection downloads and model Fire Radiative Power (FRP).

| Stage | Tools |
|-------|-------|
| Data ingest | `src/wildfire_guard/firms_api.py` (1–10 day CSV pull) |
| EDA | `notebooks/01_eda_viirs.ipynb` |
| Modelling | `notebooks/02_frp_regression.ipynb` – RandomForest log-RMSE ≈ 0.29 |
| Environment | `environment.yml` (Conda) |

![map of fires](figures/viirs_map.png)
```bash
conda env create -f environment.yml
conda activate wildfire
python src/wildfire_guard/firms_api.py 7
jupyter notebook
*(Open the file in PyCharm and tweak wording as you like.)*
