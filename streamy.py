import pandas as pd
import streamlit as st
import pydeck as pdk

# Load the tourist attractions data
file_path = 'tourist.csv'
tourist_data = pd.read_csv(file_path)

# Select relevant columns for mapping
map_data = tourist_data[['관광지명', '위도', '경도']].dropna()

# Renaming columns for ease of use
map_data.columns = ['Tourist Attraction', 'Latitude', 'Longitude']

# Create a map visualization with Pydeck
st.title("Korean Tourist Attractions")

st.write("### Tourist Attractions Data")
st.dataframe(map_data.head())

# Create a callback function to handle selection
def handle_selection(selected):
    if selected:
        st.write(f"You selected: {selected['Tourist Attraction']} at {selected['Latitude']}, {selected['Longitude']}")

# Create a pydeck map for tourist attractions with hover details
st.write("### Tourist Attractions Map")
selected_data = st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=pdk.ViewState(
            latitude=map_data['Latitude'].mean(),
            longitude=map_data['Longitude'].mean(),
            zoom=6,
            pitch=50,
on_select=handle_selection,  # Handle selection event
    selection_mode="single-object"  # Single object selection
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=map_data,
                get_position='[Longitude, Latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=5000,
                pickable=True,
                tooltip={
                    "html": "<b>{Tourist Attraction}</b>",
                    "style": {
                        "backgroundColor": "steelblue",
                        "color": "white",
                        "fontSize": "16px",
                        "padding": "10px",
                    },
                },
            ),
        ],
    ),

)

