import streamlit as st
import pickle
import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Load the trained pipeline (model + preprocessing)
try:
    with open('model.pkl', 'rb') as file:
        final_pipeline = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Title and logo of the app
st.title("BankChurn AI Predictor")
# Sidebar input for user features
st.sidebar.header("Enter Details of Customer:")
user_input = {}
st.sidebar.markdown(
    "<p style='color: red; font-weight: bold;'>Note: Use 1 for Yes/True and 0 for No/False</p>",
    unsafe_allow_html=True
)

# Define numerical and categorical features
num_features = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary']
cat_features = ['Geography', 'Gender', 'Tenure', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'AgeGroups', 'BalanceCategory']
feature_names = num_features + cat_features

# Create sidebar inputs for each feature
for feature in num_features:
    user_input[feature] = st.sidebar.number_input(f"Enter {feature}", value=0.0)

for feature in cat_features:
    user_input[feature] = st.sidebar.selectbox(f"Select {feature}", df[feature].unique())

# Validate input ranges
if user_input['CreditScore'] < 300 or user_input['CreditScore'] > 850:
    st.sidebar.warning("Credit Score must be between 300 and 850.")
if user_input['Age'] < 18 or user_input['Age'] > 100:
    st.sidebar.warning("Age must be between 18 and 100.")

# Convert user input to a DataFrame
input_df = pd.DataFrame([user_input])

# Handle missing values in input_df
input_df.fillna(0, inplace=True)

# Predict button
if st.sidebar.button("Predict"):
    try:
        # Get prediction
        prediction = final_pipeline.predict(input_df)
        probabilities = final_pipeline.predict_proba(input_df)

        # Display prediction
        st.subheader("Prediction Result")
        if prediction[0] == 0:
            st.write("The customer is **not likely to churn.**")
        elif prediction[0] == 1:
            st.write("The customer is **likely to churn.**")
        
        # Display confidence score
        confidence = probabilities[0][prediction[0]]
        st.write(f"**Happening Chances:** {100*(confidence):.2f}%")

        # Display input features for clarity
        st.subheader("Based on Your Following Inputs:")
        st.write(input_df)
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Footer
st.sidebar.markdown("---")  # Horizontal line
st.sidebar.write("**App and Model Developed by**: Muhammad Waqas")
st.sidebar.write("Gmail: waqasliaqat630@gmail.com")
st.sidebar.write("Contact: +92 3097829808")

# Footer instructions
st.write("Use the sidebar to input values and click 'Predict' to get the results.")
