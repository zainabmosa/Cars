import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("Car Price Prediction 🏎️")

year = st.number_input("Year", min_value=1990, max_value=2017, value=2010)
engine_hp = st.number_input("Engine HP",min_value=55, max_value=1001, value=239)
engine_cylinders = st.number_input("Engine Cylinders", min_value=0, max_value=16, value=6)
highway_mpg = st.number_input("Highway MPG", min_value=12, max_value=111, value=25)
city_mpg = st.number_input("City MPG", min_value=7, max_value=137, value=25)
popularity = st.number_input("Popularity", min_value=2, max_value=5657, value=1385)

hp_per_cylinder = engine_hp / engine_cylinders
average_mpg = (highway_mpg + city_mpg) / 2
car_age = 2026 - year

make = st.text_input("Make")
model_name = st.text_input("Model")
doors = st.selectbox("Number of Doors",[2, 4],index=1)
market = st.text_input("Market Category")
style = st.selectbox(
    "Vehicle Style",
    [
        "Sedan",
        "Extended Cab Pickup",
        "2dr SUV",
        "4dr SUV",
        "Passenger Minivan",
        "Convertible",
        "2dr Hatchback",
        "Regular Cab Pickup",
        "Coupe",
        "Passenger Van",
        "Wagon",
        "Crew Cab Pickup",
        "4dr Hatchback",
        "Cargo Van",
        "Cargo Minivan",
        "Convertible SUV"
    ]
)

fuel = st.selectbox(
    "Engine Fuel Type",
    [
        "electric",
        "regular unleaded",
        "premium unleaded (required)",
        "flex-fuel (unleaded/E85)",
        "premium unleaded (recommended)",
        "diesel",
        "flex-fuel (premium unleaded recommended/E85)",
        "flex-fuel (premium unleaded required/E85)",
        "flex-fuel (unleaded/natural gas)",
        "natural gas"
    ]
)

transmission = st.selectbox(
    "Transmission Type",
    [
        "DIRECT_DRIVE",
        "AUTOMATIC",
        "MANUAL",
        "AUTOMATED_MANUAL"
    ]
)

drive = st.selectbox(
    "Driven Wheels",
    [
        "all wheel drive",
        "rear wheel drive",
        "front wheel drive",
        "four wheel drive"
    ]
)

size = st.selectbox(
    "Vehicle Size",
    [
        "Large",
        "Compact",
        "Midsize"
    ]
)
if st.button("Predict"):
    data = pd.DataFrame([{
        "Make": make,
        "Model": model_name,
        "Year": year,
        "Engine Fuel Type": fuel,
        "Engine HP": engine_hp,
        "Engine Cylinders": engine_cylinders,
        "Transmission Type": transmission,
        "Driven_Wheels": drive,
        "Number of Doors": doors,
        "Market Category": market,
        "Vehicle Size": size,
        "Vehicle Style": style,
        "highway MPG": highway_mpg,
        "city mpg": city_mpg,
        "Popularity": popularity,
        "HP_per_Cylinder": hp_per_cylinder,
        "Average_MPG": average_mpg,
        "Car_Age": car_age
    }])

    prediction = model.predict(data)[0]
    st.success(f"Predicted MSRP: ${prediction:,.2f}")