import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

dataset = pd.read_csv('Pesticide.csv')

diseases = dataset['Diseases'].unique()
pesticides = dataset['Pesticide'].unique()

disease_mapping = {disease: i for i, disease in enumerate(diseases)}
pesticide_mapping = {pesticide: i for i, pesticide in enumerate(pesticides)}

dataset['Diseases'] = dataset['Diseases'].map(disease_mapping)
dataset['Pesticide'] = dataset['Pesticide'].map(pesticide_mapping)

x = dataset['Diseases'].values.reshape(-1, 1)  # Reshape for single feature
y = dataset['Pesticide']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

with open('PesticideModel.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Trained model saved as linear_regression_model.pkl")