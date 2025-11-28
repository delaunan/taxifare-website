import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
'''

# --- User controllers ---
pickup_date = st.date_input("Pickup date and time (format: YYYY-MM-DD)",
    value="2014-07-06")
pickup_time = st.time_input("Pickup time", value="19:06:20")
pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)
pickup_longitude = st.number_input("Pickup longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.748817)
passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, step=1)

# --- Build parameters dictionary ---
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# --- Use only the Le Wagon API ---
url = 'https://taxifare.lewagon.ai/predict'

# --- Call the API only when user clicks ---
if st.button("Get fare prediction"):
    st.markdown("running request...")
    response = requests.get(url, params=params)

    if response.status_code == 200:

        st.markdown(f"{response.status_code}")
        st.markdown(f"{response.json()}")
        prediction = response.json().get("fare_amount")
        st.success(f"Predicted fare: {prediction} USD")
    else:
        st.error("The API request failed. Please verify the API URL and parameters.")
