
import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
        /* Body background color */
        .stApp {
            background-color: #fff0f5 !important;
        }

        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 30px;
            font-family: 'Arial', sans-serif;
        }

        .result-text {
            font-size: 24px;
            font-weight: bold;
            color: #FF5722;
            text-align: center;
            margin-top: 20px;
            font-family: 'Arial', sans-serif;
        }

        .stSelectbox label, .stNumber_input label {
            font-size: 18px;
            font-weight: bold;
            color: #333333;
            font-family: 'Arial', sans-serif;
        }

        .stSelectbox, .stNumber_input {
            background-color: #ffffff;
            border-radius: 12px;
            border: 1px solid #dddddd;
            padding: 10px;
            margin: 10px;
        }

        .stSelectbox div, .stNumber_input div {
            background-color: #ffffff;
        }

        /* Styled Buttons */
        .stButton {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 16px;
        }

        .stButton:hover {
            background-color: #45a049;
            cursor: pointer;
        }

        /* Spacing for the main section */
        .stSelectbox, .stNumber_input {
            margin: 20px 0;
        }
        
        /* Floating effect for results */
        .stAlert {
            padding: 10px 15px;
            border-radius: 12px;
            background-color: #FFEB3B;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }

        /* Custom Input Styling */
        .stNumber_input {
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Conversion Functions
def distance_converter(from_unit, to_unit, value):
    units = {"Meters": 1, "Kilometers": 1000, "Feet": 0.3048, "Miles": 1609.34}
    return value * units[from_unit] / units[to_unit]

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def weight_converter(from_unit, to_unit, value):
    units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
    return value * units[from_unit] / units[to_unit]

def pressure_converter(from_unit, to_unit, value):
    units = {"Pascals": 1, "Hectopascals": 100, "Kilopascals": 1000, "Bar": 100000}
    return value * units[from_unit] / units[to_unit]

# Streamlit UI
st.markdown("<h1 class='main-title'>⚡ Unit Converter 🌎</h1>", unsafe_allow_html=True)

category = st.selectbox("🔍 Select Category", ["📏 Distance", "🌡️ Temperature", "⚖️ Weight", "💨 Pressure"])

from_unit, to_unit, value = None, None, 0

if category == "📏 Distance":
    from_unit = st.selectbox("🔄 From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("🔄 To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")
    result = distance_converter(from_unit, to_unit, value)

elif category == "🌡️ Temperature":
    from_unit = st.selectbox("🔄 From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("🔄 To", ["Celsius", "Fahrenheit"])
    value = st.number_input("✏️ Enter Value", format="%.2f")
    result = temperature_converter(from_unit, to_unit, value)

elif category == "⚖️ Weight":
    from_unit = st.selectbox("🔄 From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("🔄 To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")
    result = weight_converter(from_unit, to_unit, value)

elif category == "💨 Pressure":
    from_unit = st.selectbox("🔄 From", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    to_unit = st.selectbox("🔄 To", ["Pascals", "Hectopascals", "Kilopascals", "Bar"])
    value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")
    result = pressure_converter(from_unit, to_unit, value)

# Display result
if value > 0:
    st.markdown(f"<p class='result-text'>🎯 {value} {from_unit} is equal to {result:.2f} {to_unit} 🎯</p>", unsafe_allow_html=True)
else:
    st.markdown("<p class='result-text'>🎯 Please enter a valid value to convert 🎯</p>", unsafe_allow_html=True)
