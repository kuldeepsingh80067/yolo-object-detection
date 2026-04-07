"""
==========================================
YOLO Object Detection App (Stable Version)
==========================================
Author: Kuldeep Singh 😎
==========================================
"""

import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

# ==============================
# 🎨 PAGE CONFIG
# ==============================
st.set_page_config(page_title="YOLO Detection", page_icon="🎯")

st.title("🎯 YOLO Object Detection")
st.markdown("Built by **Kuldeep Singh** 🚀")

# ==============================
# 📦 LOAD MODEL (CACHED)
# ==============================
@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")  # small & fast model
    return model

try:
    model = load_model()
    st.success("✅ Model Loaded Successfully")
except:
    st.error("❌ Model failed to load")
    st.stop()

# ==============================
# 📂 IMAGE UPLOAD
# ==============================
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# ==============================
# 🔍 DETECTION
# ==============================
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = np.array(image)

    with st.spinner("🔍 Detecting objects..."):
        try:
            results = model(img)

            # Draw boxes
            annotated = results[0].plot()

            st.image(annotated, caption="Detected Objects", use_column_width=True)

            # ==============================
            # 📊 SHOW RESULTS
            # ==============================
            st.subheader("📊 Detection Summary")

            names = model.names
            detected = results[0].boxes.cls.tolist()

            if detected:
                detected_names = [names[int(cls)] for cls in detected]

                for obj in set(detected_names):
                    count = detected_names.count(obj)
                    st.write(f"👉 {obj}: {count}")
            else:
                st.warning("No objects detected")

        except Exception as e:
            st.error(f"❌ Error: {e}")
