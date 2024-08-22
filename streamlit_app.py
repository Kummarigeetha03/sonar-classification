import streamlit as st
import numpy as np
from sonar_classifier import predict, get_accuracy

# App title
st.title('Sonar Data Classification')

# Show model accuracy
train_acc, test_acc = get_accuracy()
st.write(f'Accuracy score on training data: {train_acc * 100:.2f}%')
st.write(f'Accuracy score on testing data: {test_acc * 100:.2f}%')

# Input features
st.header('Enter Input Data')
input_data = []
for i in range(60):
    input_data.append(st.number_input(f'Input Feature {i+1}', min_value=0.0, max_value=1.0, value=0.0))

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_data)
    
    # Adjust the output based on prediction
    if prediction[0] == 'R':
        st.write('The model predicts: It is Rock')
    else:
        st.write('The model predicts: It is Mine')

