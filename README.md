# 🏗️ Cement Compressive Strength Prediction

This project predicts the **compressive strength of concrete** using a linear regression model based on chemical composition and age.

---

## 📊 Overview

The dataset contains various input parameters like:
- Cement, Fly Ash, Water content
- Aggregates and Additives
- Curing Age

The model predicts the final compressive strength in MPa.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 🚀 How to Run

- git clone https://github.com/nikgarhwal/cement_strength_probability.git

- cd cement_strength_probability

- pip install -r requirements.txt

- python cement_strength_predictor.py

---

## 💬 Sample Interaction

- 📊 Model Evaluation:
  - MAE: 8.11
  - MAPE: 30.61%
  - MSE: 105.97

- 🏗️ Predict Cement Compressive Strength
  - Cement (kg in a m^3 mixture) (range: 102.00 – 540.00): 350
  - Water (kg in a m^3 mixture) (range: 121.75 – 247.00): 190
  - ...
  - 🧾 Estimated Cement Strength: 27.15 MPa

---
