import pickle
import pandas as pd

def load_model():
    """
    Load the pre-trained CatBoost model from a pickle file.
    """
    try:
        with open('catboost_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except FileNotFoundError:
        raise FileNotFoundError("The file 'catboost_model.pkl' was not found. Ensure the model file exists.")

def load_feature_importance():
    """
    Load the feature importance data from a pickle file.
    """
    try:
        with open('feature_importance.pkl', 'rb') as importance_file:
            feature_importance = pickle.load(importance_file)
        return pd.DataFrame(feature_importance, columns=['feature', 'importance'])
    except FileNotFoundError:
        raise FileNotFoundError("The file 'feature_importance.pkl' was not found. Ensure the feature importance file exists.")
    except KeyError:
        raise KeyError("Feature importance data is not formatted as expected.")

def make_prediction(model, input_data):
    """
    Make a prediction using the loaded model and input data.
    Args:
        model: The pre-trained CatBoost model.
        input_data: A pandas DataFrame containing the input features.
    Returns:
        Prediction results as a numpy array.
    """
    if not isinstance(input_data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    return model.predict(input_data)
