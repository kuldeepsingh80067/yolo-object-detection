import streamlit as st
from PIL import Image
import base64
from openai import OpenAI

st.set_page_config(page_title="AI Object Detection", page_icon="🚀")

st.title("🚀 AI Object Detection (Real)")
st.markdown("Built by Kuldeep Singh 💪")

# 🔑 API KEY
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to base64
    img_bytes = uploaded_file.read()
    img_base64 = base64.b64encode(img_bytes).decode()

    with st.spinner("Detecting objects..."):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Detect all objects in this image and list them clearly."},
                    {"type": "input_image", "image_base64": img_base64}
                ]
            }]
        )

        result = response.output_text

        st.success("✅ Detection Complete")
        st.subheader("📊 Detected Objects")
        st.write(result)
