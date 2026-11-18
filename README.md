# 🚗 Used Car Price Prediction System

A Machine Learning web application that predicts the estimated selling price of used cars using **Python, Scikit-learn, Random Forest Regressor and Streamlit**.

The application allows users to enter car details and get an estimated selling price in Indian Rupees (Lakhs).

## Project Overview

Buying or selling a used car can be challenging because its price depends on several factors, such as manufacturing year, present price, kilometres driven, fuel type and transmission.

This project uses Machine Learning to analyse these factors and estimate the selling price of a used car through an interactive web application.

## Features

- Predict the estimated selling price of a used car.
- Select car name from a dropdown.
- Enter manufacturing year and present price.
- Enter kilometres driven.
- Select fuel type, seller type and transmission.
- Select the number of previous owners.
- Interactive dashboard built using Streamlit.
- Dataset insights and visualisations.
- Clean and user-friendly interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| Scikit-learn | Machine Learning |
| Random Forest Regressor | Price prediction model |
| Streamlit | Web application |
| Joblib | Model saving and loading |

## Dataset

The project uses the Used Car Dataset from Kaggle.

**Dataset:** CarDekho Vehicle Dataset

**Source:** [Kaggle - Vehicle Dataset from CarDekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

The dataset contains information such as:

- Car Name
- Manufacturing Year
- Selling Price
- Present Price
- Kilometres Driven
- Fuel Type
- Seller Type
- Transmission
- Previous Owners

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Data Visualisation
5. Feature Encoding and Preprocessing
6. Model Training using Random Forest Regressor
7. Model Evaluation
8. Model Saving
9. Web Application Development using Streamlit

## Project Structure

```text
Used-Car-Price-Prediction/
│
├── data/
│   ├── car data.csv
│   └── cleaned_car_data.csv
│
├── Graph/
│   ├── Correlation Heatmap.png
│   ├── Distribution of car price.png
│   ├── Fuel Type Vs Selling Price.png
│   ├── Manufacturing Year Vs Selling Price.png
│   ├── Present Price Vs Selling Price.png
│   └── Transmission Vs Selling Price.png
│
├── models/
│   ├── app.py
│   ├── car_price_model.pkl
│   ├── eda.py
│   ├── preprocess.py
│   └── train_model.py
│
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Used-Car-Price-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Used-Car-Price-Prediction
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

```bash
source venv/bin/activate
```

### 5. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

### 6. Run the Streamlit Application

```bash
streamlit run models/app.py
```

The application will open in your browser at:

`http://localhost:8501`

## Model Information

- **Algorithm:** Random Forest Regressor
- **Problem Type:** Regression
- **Target Variable:** Selling Price
- **Prediction Unit:** Indian Rupees (Lakhs)

The trained model uses the following seven input features:

- Manufacturing Year
- Present Price
- Kilometres Driven
- Fuel Type
- Seller Type
- Transmission
- Previous Owners

Car Name is displayed in the application but is not currently used as a model input.
## Model Evaluation

The Random Forest Regression model was evaluated using a  train-test split (80% training and 20% testing).

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 1.54 Lakhs |
| Root Mean Squared Error (RMSE) | 3.74 Lakhs |
| R² Score | 0.46 |

### Performance Summary

- The model achieved an MAE of 1.54 Lakhs.
- The RMSE was 3.74 Lakhs.
- The R² score was 0.46, indicating that the model explains approximately 46% of the variation in car selling prices.

These results provide a baseline for future model improvements.

## Project Objective

The main objective of this project is to apply Machine Learning concepts to a real-world problem and develop an interactive application that helps estimate used car prices.

---

