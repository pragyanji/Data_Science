import streamlit as st
import requests

st.set_page_config(page_title="DataScience", page_icon=":wave:", layout="centered")
st.write("<h1>Hello Pragyan !</h1>", unsafe_allow_html=True)


name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome to DataScience, {name}!") 

age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
if age:
    st.write(f"You are {age} years old.")

st.markdown("___")

if st.button("Explore DataScience"):
    st.success("Successfully clicked the button!")
    st.warning("This is a warning message.")

r = requests.get("http://0.0.0.0:8000/greet")
# if r.status_code == 200:
#     st.write(r.json())
# else:    st.error("Failed to fetch greeting from the API.")

for message in r.json():
    st.write(message["name"])