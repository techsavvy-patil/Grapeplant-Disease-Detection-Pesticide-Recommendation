# Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import tensorflow as tf

# Loading the Model
model = load_model('model.keras')
                    
# Name of Classes
CLASS_NAMES = ['Grape Black Measles', 'Grape Black rot', 'Grape Healthy', 'Grape Isariopsis Leaf Spot', 'Powdery Mildew']

# Setting Title of App
st.title("Grape Plant Disease Detection")
st.markdown("Upload an image of the plant leaf")

# Uploading the image
plant_image = st.file_uploader("Choose an image...", type="jpg")
submit = st.button('Predict Disease')

# On predict button click
if submit:
    if plant_image is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # Displaying the image
        st.image(opencv_image, channels="BGR")
        st.write(opencv_image.shape)
        
        # Resizing the image
        opencv_image = cv2.resize(opencv_image, (256, 256))
        
        # Convert image to 4 Dimension
        opencv_image = np.expand_dims(opencv_image, axis=0)
        
        # Make Prediction
        Y_pred = model.predict(opencv_image)
        
        max_prob_index = 0
        max_prob = 0.0
        for i, prob in enumerate(Y_pred[0]):
            if prob > max_prob:
                max_prob = prob
                max_prob_index = i

        # Get the corresponding class label
        result = CLASS_NAMES[max_prob_index]

        #result_index = np.argmax(Y_pred)
        #result = CLASS_NAMES[result_index]

        st.title(str("Disease Detected: "+result))

        pesticide_recommendations = {
            'Grape Black Measles': 'Mancozeb and Ziram',
            'Grape Black rot': 'Spraying Bordeaux mixture (4:4:100) once or twice on young bunches and Copper fungicides',
            'Grape Healthy': 'No pesticide recommendation needed.',
            'Grape Isariopsis Leaf Spot': 'Streptocycline (500ppm) and Bordeaux Mixture', 'Powdery Mildew': 'Pottassium Carbonate and Neem Oil'
        }

        if result in pesticide_recommendations:
            recommendation = pesticide_recommendations[result]
            st.write("Recommended Pesticide: ", recommendation)
        else:
            st.write("No pesticide recommendation available for this disease.")

    print("Y_pred:", Y_pred)
    print("Maximum value in Y_pred:", np.max(Y_pred))
    print("Argmax of Y_pred:", result)
    print("Number of classes:", len(CLASS_NAMES))
    print("Class Names:", CLASS_NAMES)