import streamlit as st
from PIL import Image
import numpy as np

# Try importing YOLO safely
try:
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")  # lightweight model
    model_loaded = True
except:
    model_loaded = False

# ---------------- UI ----------------
st.set_page_config(page_title="YOLO Object Detection", page_icon="🚀")

st.title("🚀 YOLOv8 Object Detection App")
st.markdown("Built by Kuldeep Singh 💪")

# ---------------- CHECK MODEL ----------------
if not model_loaded:
    st.error("❌ Model failed to load. Check requirements.")
    st.stop()
else:
    st.success("✅ Model Loaded Successfully")

# ---------------- IMAGE UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    img = np.array(image)

    # ---------------- DETECTION ----------------
    with st.spinner("🔍 Detecting objects..."):
        results = model(img)

        # Draw results
        annotated = results[0].plot()

        st.image(annotated, caption="✅ Detected Objects", use_column_width=True)

        # ---------------- SUMMARY ----------------
        st.subheader("📊 Detection Summary")

        names = model.names
        detected = results[0].boxes.cls.tolist()

        if detected:
            counts = {}
            for cls in detected:
                name = names[int(cls)]
                counts[name] = counts.get(name, 0) + 1

            for k, v in counts.items():
                st.write(f"👉 {k}: {v}")
        else:
            st.write("No objects detected.")
