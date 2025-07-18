import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image

# Load the model once
model = load_model('brain_tumor_multiclass_model.h5')
class_names = ['glioma', 'meningioma', 'notumor', 'pituitary']

# Custom CSS for dark theme
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .reportview-container {
        background: #0e1117;
        color: white;
    }
    .stButton>button {
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #555;
        padding: 0.5em 1.5em;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #333;
        border: 1px solid #999;
    }
    .result {
        background-color: #1e1e1e;
        padding: 1.5em;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 20px;
        text-align: center;
        color: #00ff99;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("🧠 Brain Tumor Detection")
st.subheader("Upload an MRI image to predict the tumor type")
st.markdown("")

# Image Uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Prediction function
def predict_image(image):
    # 🔧 Force image to RGB mode
    image = image.convert('RGB')
    img = image.resize((150, 150))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction[0])
    predicted_class = class_names[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    return predicted_class, confidence


# Submit button
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    if st.button("🔍 Predict"):
        label, conf = predict_image(image)
        st.markdown(f"<div class='result'>Prediction: {label.upper()}<br>Confidence: {conf:.2%}</div>", unsafe_allow_html=True)
