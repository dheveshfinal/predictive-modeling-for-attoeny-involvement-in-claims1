import streamlit as st

def render_about():
    st.title("About the Insurance Claims Analysis Tool")
    
    st.markdown("""
    ## Overview
    Welcome to the **Insurance Claims Analysis Tool**, a powerful application designed to predict **attorney involvement in insurance claims** and provide **in-depth data analysis**. This tool leverages **machine learning** and **data visualization** to enhance claim assessment and decision-making.
    
    ## Key Features
    - **Predictive Modeling**: Utilizes an advanced ML model to determine the likelihood of attorney involvement in claims.
    - **Interactive Visualizations**: Explore claim trends, financial distributions, and key relationships in the data.
    - **User-Friendly Interface**: Intuitive design for seamless navigation and data input.
    - **Comprehensive Insights**: Helps insurance professionals make informed decisions based on claim characteristics.
    
    ## How It Works
    - **Data Input**: Users provide claim details such as insurance status, gender, accident severity, loss amount, and claimant age.
    - **Prediction Engine**: A trained machine learning model processes the input data and predicts whether an attorney is involved in the claim.
    - **Visual Analytics**: The interactive dashboard enables users to analyze claim trends, correlations, and financial distributions.
    
    ## Navigation
    - **Prediction Page**: Enter claim details to receive a real-time prediction on attorney involvement.
    - **Visualizations Page**: Gain deeper insights through interactive graphs and statistical summaries.
    - **About Page**: Learn more about the application's capabilities and purpose.
    
    ## Why This Matters
    Attorney involvement in claims can significantly impact **settlement costs, legal fees, and claim resolution times**. By leveraging predictive analytics, insurance companies and claim adjusters can **proactively manage cases, reduce litigation risks, and optimize resource allocation**.
    
    ---
    Developed with **Streamlit, Pandas, and Machine Learning**, this tool aims to streamline claim assessment and improve operational efficiency.
    
    _Empowering smarter insurance decisions with data-driven insights._
    
    """)
