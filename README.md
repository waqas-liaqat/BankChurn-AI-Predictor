<h1 align="center" style="color:#2E86C1; font-family: 'Arial', sans-serif;">
    🌟 BankChurn AI Predictor 🌟
</h1>
<p align="center" style="font-size: 18px; color:#5D6D7E;">
    A project to predict customer churn and enhance retention strategies in the banking sector.
</p>
<hr style="border: 1px solid #AED6F1;">


![Project Logo](https://github.com/waqas-liaqat/BankChurn-AI-Predictor/blob/4c1797a8fb2fe97edea17e7688ed94a93489fcb2/Logo.png)

## Overview
This project focuses on predicting customer churn for a bank using machine learning. It includes EDA, model building, and deployment of a user-friendly web application to predict customer churn based on user inputs.

---

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Approach](#approach)
- [Technologies Used](#technologies-used)
- [App Demonstration](#app-demonstration)
- [Deployment](#deployment)
- [Challenges and Learnings](#challenges-and-learnings)
- [Results](#results)
- [Try It Yourself](#try-it-yourself)
- [Contact](#contact)

---

## Problem Statement
Banks often struggle with retaining customers who might leave (churn). This project predicts whether a customer will churn based on demographic and transactional data, enabling proactive retention strategies.

---

## Dataset
- **Source:** Kaggle
- Data [Link](https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset)
- **Size:** 10,000 rows, 14 features
- **Key Features:**
  - **Numerical:** Age, CreditScore, Balance, EstimatedSalary
  - **Categorical:** Geography, Gender, Tenure, NumOfProducts
  - **Target Variable:** Exited (0 = Not Churned, 1 = Churned)

---

## Exploratory Data Analysis (EDA)
EDA provided crucial insights into customer churn behavior:

1. **Target Variable Analysis:**
   - Churn rate: 20% (imbalanced dataset).
2. **Geographical Trends:**
   - Customers in Germany exhibited higher churn rates compared to France and Spain.
3. **Age Distribution:**
   - Older customers (46–60 years) were more likely to churn.
4. **Balance Insights:**
   - Customers with no balance showed unique churn patterns.
5. **Correlation Analysis:**
   - Weak correlations between numerical features, necessitating feature engineering.

Visualizations such as bar charts, heatmaps, and KDE plots were used to uncover these patterns.

---

## Approach
1. **Data Cleaning:**
   - Data consistency handled.
   - Relevant DataTypes assigned and irrelevant features removed.
   - Encoded categorical variables using one-hot encoding.
   - Scaled numerical features using MinMaxScaler.
2. **Feature Engineering:**
   - Created age and balance categories.
3. **Modeling:**
   - Tested multiple algorithms (Logistic Regression, Random Forest, XGBoost, etc.).
   - Selected the best-performing model based on recall.
4. **Deployment:**
   - Built an interactive web app using Streamlit.
   - Deployed on Streamlit Cloud for accessibility.

---

## Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-013243?style=for-the-badge&logo=matplotlib&logoColor=white)  
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)  
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)  
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)  
![Seaborn](https://img.shields.io/badge/Seaborn-2E8B57?style=for-the-badge&logo=seaborn&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  
![XGBoost](https://img.shields.io/badge/XGBoost-EB4034?style=for-the-badge&logo=xgboost&logoColor=white)  

---

## App Demonstration
### Preview of the App:
![App Screenshot](https://github.com/waqas-liaqat/BankChurn-AI-Predictor/blob/main/app_demo.png)

---

## Deployment
- **Platform:** Streamlit Cloud
- **Steps:**
  1. Clone the repository: `git clone https://github.com/your-repo/bank-churn-predictor.git`
  2. Install dependencies: `pip install -r requirements.txt`
  3. Run locally: `streamlit run app.py`
  4. Access deployed app: [Live App Link](https://bankchurn-ai-predictor.streamlit.app/)

---

## Challenges and Learnings
- **Challenge:** Selecting optimal features without overfitting.
  - **Solution:** Iterative feature elimination using tree-based models.
- **Challenge:** Addressing Data Imbalance in the Dataset.
  - **Solution:** Various techniques were tested to handle the imbalance, with underfitting yielding the best results. This approach effectively mitigated overfitting and other associated issues.
- **Challenge:** Ensuring app usability for non-technical users.
  - **Solution:** Implemented clear instructions and user-friendly design.
- **Learning:** The importance of balancing interpretability and Recall in model selection.

---

## Results
- **Model Performance:**
  - Accuracy: 72%
  - Recall: 73%
- **Key Insights:**
  - Age and geography were significant churn indicators.
  - Customers with high balances were more likely to churn.

---

## Try It Yourself
Access the deployed app: [Live App Link](https://bankchurn-ai-predictor.streamlit.app/)

---

## Contact
- **Developer:** Muhammad Waqas  
- **Email:** waqasliaqat630@gmail.com  
- **Phone:** +92 3097829808  
- **GitHub:** [waqasliaqat](https://github.com/waqas-liaqat)  
- **Linkedin:** [muhammadwaqasliaqat](https://www.linkedin.com/in/muhammad-waqas-liaqat/)  

---

*"This project demonstrates my expertise in Python, machine learning, Exploratory Data Analysis, feature engineering, and application deployment. Feel free to test the app or explore the repository for more details!"*

