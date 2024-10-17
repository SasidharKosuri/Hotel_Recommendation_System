import streamlit as st
from streamlit_option_menu import option_menu
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
import base64
import plotly.express as px
import json 
import requests 
#impoerting the files
from sort_price import *
from sort_amenities import *
from sort_rating import *

# to render the gif 
import streamlit as st 
from streamlit_lottie import st_lottie 
url = requests.get( 
	"https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json") 
url_json = dict() 
if url.status_code == 200: 
	url_json = url.json() 
else: 
	print("Error in URL") 

# code to init the session state
def init_session_state():
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None

# code to render the image
@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("sidebar.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: image1.jpg;
background-repeat: no-repeat;
background-attachment: local;
background-size: cover;
background-position: center;
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-size: cover;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Define function to display page content based on selection
def display_page(selected_option):
    init_session_state()
    if selected_option == "Home":
        st.write("Welcome to the Home page!")
    elif selected_option == "Search":
        st.write("Welcome to the Search page!")
        
        data = pd.read_csv('modified_data.csv')
        merged = pd.read_csv('modified_merged.csv')

        st.title('HOTEL INFORMATION')

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
        st.write("Here are the details :")
        st.subheader(f"{hotel}")
        st.write(f"📍 {raw_add}")

        hotel_rating = data[data['hotel_name'] == hotel]['Rating']
        hotel_star = hotel_rating.iloc[0]
        st.write(f"⭐ Hotel Rating : {hotel_star}")
        st.write("")
        st.write("📌 Popular Amenities :")
        # st.write(f"{raw_amenities}")
        # st.write()
        l=[]
        prev=0
        for i in range(len(raw_amenities)):
            if raw_amenities[i]==",":
                l.append(raw_amenities[prev+1:i])
                prev=i
        # st.table(l)
        actual_list = literal_eval(raw_amenities)
        st.table(actual_list)

        # maps, details , link, and in last add functions 
        # this is the hyperlink part
        first_link = "[Goibibo Link](https://www.goibibo.com"
        url = data[data['hotel_name'] == hotel]['URL']
        second_link = str(url.iloc[0])
        link = first_link + second_link + ")"

        st.subheader("🔗 Hotel Website Link :")
        st.write(link)
        

        # this is the map part of the project
        latitude = merged[merged['hotel_name'] == hotel]['Latitude']
        longitude = merged[merged['hotel_name'] == hotel]['Longitude']

        map = folium.Map(location=[latitude,longitude],zoom_start=12)
        folium.Marker(location=[latitude,longitude],tooltip = "Location").add_to(map)
        st.subheader("🗺️ Hotel Map Location :")
        st_folium(map,width=700,height=500)
    # here include the footer 
    
        
    elif selected_option == "Stays":
        st.write("Welcome to the Stays page!")
        st.title("HOTEL RECOMMENDATION")
        st.write("🎡Explore the perfect stay for your next trip with our intuitive recommendation system.🏂 We understand that every traveler has unique preferences, 🏖️ which is why we offer three different ways to find your ideal hotel ✨ : ")
        st.write("1. RECOMMEND BY PRICE 💸: Looking for a budget-friendly option? Click this button to discover hotels that fit your budget while still offering great amenities and services.                Recommend by Rating: Quality is key! Click here to find hotels with top ratings and excellent guest reviews, ensuring a memorable and satisfying stay.")
        st.write("2. RECOMMEND BY AMENITIES 📚: Customize your search based on the amenities that matter most to you. Whether it's a swimming pool, free Wi-Fi, or complimentary breakfast, we'll find the perfect match for your needs.")
        st.write("3. RECOMMEND BY RATING ⭐: Quality is key! Whether you prefer luxury or value, click here to find hotels with top ratings and excellent guest reviews, ensuring a memorable and satisfying stay.")
        st.write("Simply click on one of the buttons above to get started, and let us take care of the rest! Travel planning has never been easier.""")
        st.write("")

        col1,col2,col3=st.columns([5,5,5])
        with col1:
            if st.button("Rating"):
                st.session_state.selected_option = "rating"
        with col2:
            if st.button("price"):
                st.session_state.selected_option = "price"
        with col3:
            if st.button("amenities"):
                st.session_state.selected_option = "amenities"
    
        # Display content based on selected option
        if st.session_state.selected_option == "rating":
            st.write("You selected Rating.")
            sort_rating()
            # Call your rating.py file here
        elif st.session_state.selected_option == "price":
            st.write("You selected price")
            sort_price()
            # Call your price.py file here
        elif st.session_state.selected_option == "amenities":
            st.write("You selected amenities")
            sort_amenities()
            


    elif selected_option == "Attractions":
        st.write("Welcome to the Attractions page!")
    elif selected_option == "Settings":
        st.write("Welcome to the Settings page!")
    elif selected_option == "Help":
        st.write("Welcome to the Help page!")
        st.title("HELP")
        st.header("FAQ")
        col1, col2 = st.columns([3, 1])
        with col1:
        # FAQ 1
            with st.expander("How do I get started with the app?"):
                st.markdown("""
                To get started with the app, simply follow these steps:
                1. Navigate to the home page.
                2. Select your preferences (e.g., rating, price, amenities).
                3. Click on the corresponding button to view recommended hotels.
                """)

    elif selected_option == "Account":
        st.write("Welcome to the Account page!")
        col1,col2=st.columns([3,3])
        with col1:
            st.button("LOGIN")
        with col2:
            st.button("SIGNUP")


# ------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    selected = option_menu("HOTEL RECOMMENDER", ["Home", 'Search','Stays','Attractions','Settings',"Account",'Help'], 
        icons=['house-heart','search','luggage','pin-map', 'gear','person-circle','question-circle'], menu_icon="buildings", default_index=0)
    
# Display page content based on selection
display_page(selected)


