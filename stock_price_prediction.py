import streamlit as st
import pandas as pd
import numpy as np
import joblib

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load the saved model
model = joblib.load('lstm_trained_model.joblib')

# Load the scaler object used for preprocessing
scaler = joblib.load('scaler.joblib') 

# Preprocess function
def preprocess_data(input_data):
    # Rename the columns of input_data to match the feature names used during fitting
    input_data = input_data.rename(columns={
        'Annual Average Inflation': 'Annual_Average_Inflation',
        'Central Bank Rate': 'Central_Bank_Rate',
        'Dividend Yield': 'Dividend_Yield',
        'GDP Growth Rate': 'GDP_Growth_Rate'
    })

    # Scale the input data
    scaled_data = scaler.transform(input_data)
    scaled_df = pd.DataFrame(scaled_data, columns=input_data.columns)

    # Reshape the data to have the shape (1, -1), where -1 automatically computes the dimension based on the number of features
    preprocessed_data = scaled_df.values.reshape(1, -1)
    return preprocessed_data


# Prediction function
def make_predictions(model, input_data):
    # Repeat the input data to create a sequence of length 10
    X_test = np.repeat(input_data, repeats=10, axis=0)
    X_test = X_test.reshape(1, 10, -1)
    y_pred = model.predict(X_test)
    y_pred_actual = y_pred * 7
    return y_pred_actual


# Streamlit UI
def main():
    st.title('Stock Price Prediction')
    st.sidebar.header('User Input Features')

    # Input fields for user to enter data
    close_price = st.sidebar.number_input('Close Price')
    volume = st.sidebar.number_input('Volume')
    gdp_growth_rate = st.sidebar.number_input('GDP Growth Rate')
    annual_average_inflation = st.sidebar.number_input('Annual Average Inflation')
    central_bank_rate = st.sidebar.number_input('Central Bank Rate')
    dividend_yield = st.sidebar.number_input('Dividend Yield')
    rsi = st.sidebar.number_input('RSI')
    macd = st.sidebar.number_input('MACD')

    # Create a dictionary to hold user inputs
    input_data = {
        'Close': close_price,
        'Volume': volume,
        'GDP Growth Rate': gdp_growth_rate,  # Adjusted key
        'Annual Average Inflation': annual_average_inflation,  # Adjusted key
        'Central Bank Rate': central_bank_rate,  # Adjusted key
        'Dividend Yield': dividend_yield,
        'RSI': rsi,
        'MACD': macd
    }

    # Print input data for debugging
    st.write('Input Data:', input_data)

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Print input DataFrame for debugging
    st.write('Input DataFrame:', input_df)

    # Preprocess input data
    preprocessed_data = preprocess_data(input_df)

    # Print preprocessed data for debugging
    st.write('Preprocessed Data:', preprocessed_data)

    # Make predictions
    if st.button('Predict'):
        if preprocessed_data.size == 0:
            st.error('Input data is empty!')
        else:
            predictions = make_predictions(model, preprocessed_data)
            st.write('Predicted Close Price:', predictions[0])

if __name__ == '__main__':
    main()

