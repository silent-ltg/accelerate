import streamlit as st
import google.generativeai as genai

# basic setup
st.set_page_config(page_title="critique clone", page_icon="🥷🏽")
st.title("accelerate ai")

# add as many habits as you want here
st.header("daily habits 🔪")
habit1 = st.checkbox("went to the gym")
habit2 = st.checkbox("drank 2L water")
habit3 = st.checkbox("no junk food")
habit4 = st.checkbox("8 hours sleep")
habit5 = st.checkbox("read for 15 mins")
habit6 = st.checkbox("hit protein goal")
habit7 = st.checkbox("went for a walk")
if st.button("save progress"):
    st.success("habits locked in! 🩸")

import streamlit as st
import google.generativeai as genai
from PIL import Image

# your secret api key is now locked in 💉
genai.configure(api_key="AIzaSyD2I-jkX5ZqkmYDIox8GnR9qeAZxQNDihs")

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded 🥷🏽")

# basic setup
st.set_page_config(page_title="accelerate ai", page_icon="🩸")
st.title("accelerate ai meal scanner 💫")

# meal scanner section 💉
uploaded_file = st.file_uploader("upload a photo of your meal...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="your meal", use_container_width=True)
    
    if st.button("analyze meal 😂"):
        image_data = input_image_setup(uploaded_file)
        # the prompt that tells the ai what to do
        prompt = "analyze this food image. give me a breakdown of calories, protein, carbs, and fats. be honest but helpful 🩸"
        
        with st.spinner("scanning your gains... 🥷🏽"):
            response = get_gemini_response(prompt, image_data)
            st.subheader("the breakdown 💉")
            st.write(response)

