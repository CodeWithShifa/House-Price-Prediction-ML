# House-Price-Prediction-ML
A Python-based Machine Learning model using Linear Regression to predict property prices based on square footage and house features
# 🏠 House Price Prediction (Linear Regression)

A Machine Learning project that predicts property prices based on square footage. This project marks my transition into **Predictive Analytics** and **Supervised Learning**.

## 📊 Project Insight
Using the `house_prices.csv` dataset, I built a **Linear Regression** model. The goal was to understand the mathematical relationship between the size of a house (Size_sqft) and its market value (Price).

## 🛠️ How it Works
1. **Data Loading:** Used **Pandas** to handle the CSV dataset.
2. **Feature Selection:** Isolated `Size_sqft` as the independent variable (X) and `Price` as the target variable (y).
3. **Model Training:** Utilized **Scikit-Learn**'s Linear Regression algorithm to train the model.
4. **Prediction:** The model can estimate the price for any given square footage. For example, a 2000 sq ft house was predicted at approximately 503k.

## 📁 Repository Content
- `house_prediction.py`: The Python script containing the ML logic.
- `house_prices.csv`: The dataset used for training (contains Size, Bedrooms, Bathrooms, Age, and Price).

## 💻 Tech Stack
- **Python**
- **Pandas**
- **Scikit-Learn**
