import streamlit as st
import pandas as pd
import numpy as np
import joblib  # Import joblib

# Load the trained model using a relative path
model_path = 'C:\\Users\\emrid\\AI_PROJECT\\HOUSE_PRICE_PREDICTION(LATEST).joblib'  # Go up one level (..) then into model_folder

#for checking the model's req features
# try:
#     model = joblib.load(model_path)
#
#     # --- START: Code to inspect feature_names_in_ (for debugging) ---
#     if hasattr(model, 'feature_names_in_'):
#         st.subheader("Model's Expected Features:")
#         st.write(model.feature_names_in_)
#     else:
#         st.info("The loaded model does not have a 'feature_names_in_' attribute.")
#     # --- END: Code to inspect feature_names_in_ ---
#
# except FileNotFoundError:
#     st.error(f"Model file not found at: {model_path}")
#     st.stop()
# except Exception as e:
#     st.error(f"Error loading the model: {e}")
#     st.stop()


try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}")
    st.stop()
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

# ... Streamlit code ...
st.title("CALIFORNIA HOUSE PRICE PREDICTION")

# Option to choose between manual input and default value
longitude_choice = st.radio(
    "Choose Longitude Input Method:",
    ("Enter Manually", "Use Default Value(30.0)"),
)

longitude = None  # Initialize longitude variable
default_longitude = 30.0  # Define your default longitude value

if longitude_choice == "Enter Manually":
    # Get manual input for longitude
    manual_longitude = st.number_input(
        "Enter Longitude:",
        min_value=-150.0,
        max_value=150.0,
        step=0.01,
    )
    longitude = manual_longitude  # Store the manually entered value

elif longitude_choice == "Use Default Value(30.0)":
    longitude = default_longitude  # Use the predefined default value


# Option to choose between manual input and default value
latitude_choice = st.radio(
    "Choose Latitude Input Method:",
    ("Enter Manually", "Use Default Value(30.0)"),
)

latitude = None  # Initialize latitude variable
default_latitude = 30.0  # Define your default latitude value

if latitude_choice == "Enter Manually":
    # Get manual input for latitude
    manual_latitude = st.number_input(
        "Enter Latitude:",
        min_value=-150.0,
        max_value=150.0,
        step=0.01,
    )
    latitude = manual_latitude  # Store the manually entered value

elif latitude_choice == "Use Default Value(30.0)":
    latitude = default_latitude  # Use the predefined default value

# # Display the selected/default latitude
# if latitude is not None:
#     st.write(f"Selected/Default Latitude: {latitude}")

housing_median_age = st.number_input("housing_median_age",format="%0.1f",value=0.0, step=0.1)
#st.write("The current number is ", number3)
total_rooms= st.number_input("total_rooms",format="%0.1f",value=0.0, step=1.0)
#st.write("The current number is ", number4)
total_bedrooms = st.number_input("total_bedrooms",format="%0.1f",value=0.0, step=1.0)
#st.write("The current number is ", number5)
population = st.number_input("population",format="%0.1f",value=0.0, step=1.0)
#st.write("The current number is ", number6)
households = st.number_input("households",format="%0.1f",value=0.0, step=1.0)
#st.write("The current number is ", number7)
median_income = st.number_input("median_income",format="%0.4f", value=0.0, step=0.0001)
#st.write("The current number is ", number8)


ocean_proximity = st.selectbox(
    "Select Ocean Proximity",
    ("NEAR OCEAN", "NEAR BAY","INLAND","<1H OCEAN","ISLAND"),
)
#st.write("You selected:", option)



##PREDICTION WORK START.....
#creating dataframe for prediction
if all([latitude is not None, longitude is not None]):
    input_data_dict = {
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    }

    #creating pandas dataframe
    input_df = pd.DataFrame(input_data_dict)

    # --- Apply get_dummies for 'ocean_proximity' with drop_first=True ---
    input_df = pd.get_dummies(input_df, columns=['ocean_proximity'], drop_first=True)

    # Create the missing features
    input_df['bedroom_ratio'] = input_df['total_bedrooms'] / input_df['total_rooms']
    input_df['household_rooms'] = input_df['total_rooms'] / input_df['households']

    # Define the expected feature order (MATCHING YOUR TRAINING DATA)
    feature_order = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
                     'households', 'median_income', 'ocean_proximity_INLAND', 'ocean_proximity_ISLAND',
                     'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN', 'bedroom_ratio', 'household_rooms']

    # Reindex the DataFrame to ensure all expected columns are present and in the correct order
    input_df = input_df.reindex(columns=feature_order, fill_value=0)

    try:
        input_df = input_df[feature_order]
    except KeyError as e:
        st.error(f"Error: Missing feature in input data after reindexing: {e}")
        st.info(f"Make sure your input includes all the following columns in the correct order: {feature_order}")
        st.stop()

    # --- Make Prediction ---
    try:
        prediction = model.predict(input_df)[0]
        st.subheader(f"Predicted House Price: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")