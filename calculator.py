# To run the file : streamlit run calculator.py
import streamlit as st

st.title("calculator")
st.markdown("This is a simple calculator")

c1,c2 = st.columns(2)
fnum = c1.number_input("Enter first number",value=0)
snum = c2.number_input("Enter second number", value=0)

options = [ "Addition","Subtraction","Multiplication","Divison"]
choice = st.radio("Select operation",options)

button = st.button("calculate")

if button:
    if choice == "Addition":
        result = fnum + snum
    if choice == "Subraction":
        result = fnum - snum
    if choice == "Multiplication":
        result = fnum * snum
    if choice == "Divison":
        result = fnum/snum

st.success(f"Result is {result}")