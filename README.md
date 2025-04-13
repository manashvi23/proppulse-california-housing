# 🏡 Propulse: Feel the Price of Property

Welcome to **Propulse**, a machine learning project that predicts housing prices using the California Housing dataset. This project aims to explore the relationship between various housing features and their influence on property prices, while demonstrating the power of feature engineering and ensemble models like Random Forest.

---

## 📌 Project Overview

Propulse is designed to give insights into housing prices across California by:
- Exploring the dataset through visualization and statistics.
- Engineering new features to improve predictive power.
- Training and evaluating regression models.
- Delivering accurate price predictions for new or unseen data.

---

## 🔍 Dataset

We use the **California Housing Prices dataset**, which includes the following key features:
- Latitude and longitude
- Median income
- House_median_age
- total_rooms
- total_bedrooms
- population
- households
- median_income
- median_house_value  


Additional features are created based on combinations and transformations of the original ones to boost performance.

---

## 🧠 Features Engineered

We derived new features such as:
- `bedroom_ratio`
- `household_rooms`

These features help the model capture more complex patterns in the data.

---

## ⚙️ Models Used

We experimented with multiple regression models including:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor** (final model)

The Random Forest model was chosen due to its strong performance and robustness.

---

## 📈 Evaluation Metrics

Model performance is evaluated using:
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score (Coefficient of Determination)**

---

