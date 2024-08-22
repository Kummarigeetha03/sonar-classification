import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv('data/sonardata.csv', header=None)

# Prepare the data
X = df.drop(columns=60, axis=1)
Y = df[60]

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)

# Model creation and training
model = SVC(kernel='rbf', gamma='scale')
model.fit(x_train, y_train)

# Functions for prediction and accuracy
def predict(input_data):
    inparr = np.asarray(input_data)
    reinparr = inparr.reshape(1, -1)
    prediction = model.predict(reinparr)
    return prediction

def get_accuracy():
    x_train_prediction = model.predict(x_train)
    training_accuracy = accuracy_score(x_train_prediction, y_train)

    x_test_prediction = model.predict(x_test)
    testing_accuracy = accuracy_score(x_test_prediction, y_test)

    return training_accuracy, testing_accuracy
