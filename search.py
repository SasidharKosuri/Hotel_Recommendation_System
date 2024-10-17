import nltk
import ssl
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import folium
from streamlit_folium import st_folium
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from ast import literal_eval

# data = pd.read_csv('clean_data.csv')
# # merged is only location on the map
# merged = pd.read_csv('merged_data.csv')

data = pd.read_csv('modified_data.csv')
merged = pd.read_csv('modified_merged.csv')

st.title('Hotel recommendation System')

unique_cities = data['City'].unique()
unique_cities.sort()

# This creates two columns of equal width
col1, col2 = st.columns(2)  

with col1:
    city = st.selectbox("Select your city", unique_cities, key="city")

with col2:
    hotel = st.selectbox("Select your hotel", data[data['City'] == city]['hotel_name'], key="hotel")

# st.write(f"The city is ***{city}***")
# st.write(f"The hotel is ***{hotel}***")

city_hotels = data[data['City'] == city]
hotel_address = data[data['hotel_name'] == hotel]['Address']

# iloc allows you to select rows and columns by their integer indices
# loc allows you to select rows and columns by their label indexing 
raw_add = hotel_address.iloc[0]
hotel_amenities = data[data['hotel_name'] == hotel]['Amenities']
raw_amenities = hotel_amenities.iloc[0]

# st.write(f"Here are the detaiils of ***{hotel}*** in ***{city}***")

# this is the details part 
st.write("Here are the details ")
st.subheader(f"{hotel}")
st.write(f"📍 {raw_add}")
st.write("")
st.write("Popular Amenities")
st.write(f"{raw_amenities}")
st.write()
# maps, details , link, and in last add functions 
# this is the hyperlink part
first_link = "[Goibibo Link](https://www.goibibo.com"
url = data[data['hotel_name'] == hotel]['URL']
second_link = str(url.iloc[0])
link = first_link + second_link + ")"

st.write(link)

# this is the map part of the project
latitude = merged[merged['hotel_name'] == hotel]['Latitude']
longitude = merged[merged['hotel_name'] == hotel]['Longitude']

map = folium.Map(location=[latitude,longitude],zoom_start=12)
folium.Marker(location=[latitude,longitude],tooltip = "Location").add_to(map)
st_folium(map,width=700,height=500)
