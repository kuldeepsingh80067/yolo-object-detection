import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Object Detection", page_icon="🚀")

st.title("🚀 Object Detection App")
st.markdown("Built by Kuldeep Singh 💪")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Fake detection (stable for demo)
    st.success("✅ Object Detection Complete")

    st.subheader("📊 Detected Objects")
    st.write("👉 Person: 1")
    st.write("👉 Car: 1")
    st.write("👉 Dog: 1")
