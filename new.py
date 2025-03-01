# Streamlit ko import karenge
import streamlit as st  # pip install streamlit

# Function banayenge jis mien hum 3 cheezen add karenge
# values = user ka input, from_unit = jisko convert karna h, to_unit = jis mien convert karna h
def Convert_units(values, from_unit, to_unit):
    conversion_formula = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
        "feet": {"meters": 0.3048, "centimeters": 30.48},
        "centimeters": {"meters": 0.01, "feet": 0.0328084},
    }

    if from_unit == to_unit:
        return values

    factor = conversion_formula.get(from_unit, {}).get(to_unit, None)
    if factor is None:
        return None  # Agar conversion formula nahi milta

    return values * factor

# Streamlit UI
st.title("Simple Unit Converter")
st.sidebar.header("Select Conversion")

# User input fields
from_unit = st.sidebar.selectbox("From", ["meters", "kilometers", "miles", "centimeters", "feet"])
to_unit = st.sidebar.selectbox("To", ["meters", "kilometers", "miles", "centimeters", "feet"])
values = st.sidebar.number_input("Enter your value", min_value=0.0, format="%.2f")

# Conversion button
if st.sidebar.button("Convert"):
    result = Convert_units(values, from_unit, to_unit)
    if result is not None:
        st.success(f"{values} {from_unit} is equal to {result:.3f} {to_unit}")
    else:
        st.error("Conversion not possible between selected units!")
