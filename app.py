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

# meal scanner section
st.header("meal scanner 💉")
uploaded_file = st.file_uploader("scan your meal...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="your meal", use_container_width=True)
    st.info("ai is analyzing your gains... 😂")
