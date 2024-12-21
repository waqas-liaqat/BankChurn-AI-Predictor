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

## Approach
1. **Data Cleaning:**
   - Handled missing values and outliers.
   - Encoded categorical variables using one-hot encoding.
2. **Feature Engineering:**
   - Created age and balance categories.
   - Removed redundant features to prevent overfitting.
3. **Modeling:**
   - Tested multiple algorithms (Logistic Regression, Random Forest, XGBoost).
   - Selected the best-performing model based on precision, recall, and F1-score.
4. **Deployment:**
   - Built an interactive web app using Streamlit.
   - Deployed on Streamlit Cloud for accessibility.

---

## Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)  
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-013243?style=for-the-badge&logo=matplotlib&logoColor=white)  

---

## App Demonstration
### Preview of the App:
![App Screenshot](https://via.placeholder.com/800x400)

---

## Deployment
- **Platform:** Streamlit Cloud
- **Steps:**
  1. Clone the repository: `git clone https://github.com/your-repo/bank-churn-predictor.git`
  2. Install dependencies: `pip install -r requirements.txt`
  3. Run locally: `streamlit run app.py`
  4. Access deployed app: [Live App Link](https://your-app-link.com)

---

## Challenges and Learnings
- **Challenge:** Selecting optimal features without overfitting.
  - **Solution:** Iterative feature elimination using tree-based models.
- **Challenge:** Ensuring app usability for non-technical users.
  - **Solution:** Implemented clear instructions and user-friendly design.
- **Learning:** The importance of balancing interpretability and accuracy in model selection.

---

## Results
- **Model Performance:**
  - Accuracy: 87%
  - Precision: 84%
  - Recall: 79%
  - F1-Score: 81%
- **Key Insights:**
  - Age and geography were significant churn indicators.
  - Customers with high balances were less likely to churn.

---

## Try It Yourself
Access the deployed app: [Live App Link](https://your-app-link.com)

---

## Contact
**Developer:** Muhammad Waqas  
**Email:** waqasliaqat630@gmail.com  
**Phone:** +92 3097829808  
**GitHub:** [waqasliaqat](https://github.com/waqasliaqat)  

---

*"This project demonstrates my expertise in Python, machine learning, feature engineering, and application deployment. Feel free to test the app or explore the repository for more details!"*

