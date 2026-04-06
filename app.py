import streamlit as st
import google.generativeai as genai
from PIL import Image

# 2026 stable configuration 🥷🏽
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# this is the magic sauce to change the look 🩸
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stCheckbox {
        background-color: #1a1c23;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
    }
    h1, h2 {
        color: #ff4b4b !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("accelerate ai 💫")

# habit tracker 🥷🏽
st.header("daily habits 🔪")
habits = ["gym", "2l water", "no junk", "8h sleep", "15m read", "protein goal"]
cols = st.columns(2)
for i, habit in enumerate(habits):
    with cols[i % 2]:
        st.checkbox(habit)

if st.button("save progress"):
    st.success("habits locked in! 🩸")

# meal scanner 💉
st.header("meal scanner 🩸")
uploaded_file = st.file_uploader("upload meal photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="your meal", use_container_width=True)
    
    if st.button("analyze meal 😂"):
        with st.spinner("scanning your gains... 🥷🏽"):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(["break down the macros in this image 🩸", image])
                st.subheader("the breakdown 💉")
                st.write(response.text)
            except Exception as e:
                st.error(f"error: {e} 🔪 check secrets!")
