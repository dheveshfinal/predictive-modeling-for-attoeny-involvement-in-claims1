import streamlit as st
import pandas as pd
from model import load_model, make_prediction
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")

# Constants
DATA_PATH = "C:/Users/dheve/OneDrive/Desktop/ML-project/predictive modeling for attoeny involvement in claims/Updated_Claimants_Dataset.csv"

def load_data():
    """Load the dataset from the specified path."""
    return pd.read_csv(DATA_PATH)

def setup_sidebar():
    """Setup the sidebar for navigation."""
    st.sidebar.title("Insurance Prediction App")
    st.sidebar.markdown("This app predicts whether an attorney is involved in a claim.")
    
    navigation_buttons = {
        "Prediction Page": "prediction",
        "Visualizations": "visualizations",
        "About": "about"
    }
    
    for button_text, page_value in navigation_buttons.items():
        if st.sidebar.button(button_text):
            st.experimental_set_query_params(page=page_value)

def render_prediction_page():
    """Render the prediction page."""
    st.title("Prediction Page")
    st.markdown("Enter the data to predict whether an attorney is involved in the claim.")
    
    # User input fields
    input_fields = {
        "CLMINSUR": st.selectbox(
            "Insurance Status", 
            [1, 0], 
            format_func=lambda x: "Insured" if x == 1 else "Not Insured"
        ),
        "CLMSEX": st.selectbox(
            "Gender", 
            [1, 0], 
            format_func=lambda x: "Male" if x == 1 else "Female"
        ),
        "Accident_Severity_Encoded": st.selectbox(
            "Accident Severity",
            [1, 2, 3],
            format_func=lambda x: {1: "Severe", 2: "Moderate", 3: "Minor"}[x]
        ),
        "LOSS": st.number_input(
            "Loss Amount (standardized)", 
            step=0.1, 
            format="%.2f"
        ),
        "CLMAGE": st.number_input(
            "Claimant Age", 
            min_value=0, 
            max_value=100, 
            step=1
        )
    }
    
    # Prepare input data for prediction
    input_data = pd.DataFrame([list(input_fields.values())], columns=list(input_fields.keys()))
    
    if st.button("Make Prediction"):
        model = load_model()
        prediction = make_prediction(model, input_data)
        message = "The claim involves an attorney!" if prediction[0] == 1 else "No attorney involved in the claim."
        st.success(message)

def main():
    """Main function to run the Streamlit app."""
    df = load_data()
    setup_sidebar()
    
    # Get the current page from query parameters
    page = st.experimental_get_query_params().get("page", ["prediction"])[0]
    
    # Page routing
    pages = {
        "prediction": render_prediction_page,
        "visualizations": lambda: __import__("visualizations").render_visualizations(df),
        "about": lambda: __import__("about").render_about()
    }
    
    pages[page]()

if __name__ == "__main__":
    main()
