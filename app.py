import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

st.set_page_config(page_title="Object Detection Lite", page_icon="🚀")

st.title("🚀 Object Detection (FREE & WORKING)")
st.markdown("Built by Kuldeep Singh 💪")

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    return model

model = load_model()

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).resize((224, 224))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("Detecting objects..."):
        predictions = model.predict(img_array)
        decoded = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    st.success("✅ Detection Complete")

    st.subheader("📊 Detected Objects")
    for i, (imagenetID, label, prob) in enumerate(decoded):
        st.write(f"{i+1}. {label} ({prob*100:.2f}%)")
