import streamlit as st
import time
st.set_page_config(
    page_title="Shape Calculator App",
    page_icon="📐",
    layout="wide")

st.title("shaps calculator app")
st.write("This app calculates the area and perimeter of different shapes.")

st.sidebar.header("Select a shape to calculate its area and perimeter")
st.sidebar.header('configuration')

with st.sidebar:
   shape=st.selectbox("Select shape", ["Ciecle", "Square", "Rectangle", "triangle"])
   
if shape == "Ciecle":
    radius = st.number_input("Enter radius", min_value=0, max_value=100, value=10,step=10)
    area = 3.14 * radius ** 2
    perimeter = 2 * 3.14 * radius

if shape == "Rectangle":
   width = st.number_input("Enter width", min_value=0, max_value=100, value=10,step=10)
   height = st.number_input("Enter height", min_value=0, max_value=100, value=10,step=10)
   area = width * height
   perimeter = 2 * (width + height)


cmpute_btn = st.button("Compute Rectangle")
if cmpute_btn:
  with st.spinner("Calculating..."):
    time.sleep(1)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")
