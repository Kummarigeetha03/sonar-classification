
# Sonar Data Classification

This project uses a Support Vector Classifier (SVC) to classify sonar signals as either a rock or a mine based on the sonar data. The web interface for this project is built using Streamlit and can be deployed on Streamlit Cloud.

## Project Structure

sonar-classification
│
├── sonar_classifier.py # Main model training and prediction script
├── streamlit_app.py # Streamlit app for deployment
├── requirements.txt # Required libraries
├── data # Folder to store your CSV file
│ └── sonardata.csv
└── .gitignore # To avoid committing unnecessary files

### Prerequisites

- Python 3.7 or higher
- Git installed on your system

### Setup Instructions

1. **Clone the Repository**:
   
   git clone https://github.com/kummarigeetha03/sonar-classification.git
   cd sonar-classification

2.Create and Activate a Virtual Environment:

Windows:

python -m venv venv
.\venv\Scripts\activate


3.Install Required Libraries:

In terminal run:

pip install -r requirements.txt

4.Place Data in the Appropriate Folder:

Add sonardata.csv file in the data folder.

5.Run the App Locally:

Once the environment is set up, you can run the Streamlit app locally:(pip install stream3lit)

streamlit run streamlit_app.py



## deployed streamlit link 

https://sonar-classification-03.streamlit.app/
