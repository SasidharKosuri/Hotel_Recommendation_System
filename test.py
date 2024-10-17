# CAROUSEL CODE -----------------------------------------------------------------------------------------------------------------------
# from streamlit_carousel import carousel

# test_items = [
#     dict(
#         title="Slide 1",
#         text="A tree in the savannah",
#         img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
#         link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819"
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
#     ),
#     dict(
#         title="Slide 3",
#         text="A distant mountain chain preceded by a sea",
#         img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master"
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
#     ),
#     dict(
#         title="Slide 2",
#         text="A wooden bridge in a forest in Autumn",
#         img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
#         link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel"
#     ),
# ]

# carousel(items=test_items, width=1)


# SESSION MANAGEMENT CODE --------------------------------------------------------------------------------------------------------------
# import streamlit as st
# from sort_amenities import *
# from sort_price import *
# from sort_rating import * 

# # Function to initialize session state
# def init_session_state():
#     if 'selected_option' not in st.session_state:
#         st.session_state.selected_option = None

# # Main function
# def main():
#     init_session_state()
    
#     # Display context
#     st.write("This is the main context.")
#     st.write("Welcome to the Stays page!")
#     st.title("HOTEL RECOMMENDATION")
#     st.write("🎡Explore the perfect stay for your next trip with our intuitive recommendation system.🏂 We understand that every traveler has unique preferences, 🏖️ which is why we offer three different ways to find your ideal hotel ✨ : ")
#     st.write("1. RECOMMEND BY PRICE 💸: Looking for a budget-friendly option? Click this button to discover hotels that fit your budget while still offering great amenities and services.                Recommend by Rating: Quality is key! Click here to find hotels with top ratings and excellent guest reviews, ensuring a memorable and satisfying stay.")
#     st.write("2. RECOMMEND BY AMENITIES 📚: Customize your search based on the amenities that matter most to you. Whether it's a swimming pool, free Wi-Fi, or complimentary breakfast, we'll find the perfect match for your needs.")
#     st.write("3. RECOMMEND BY RATING ⭐: Quality is key! Whether you prefer luxury or value, click here to find hotels with top ratings and excellent guest reviews, ensuring a memorable and satisfying stay.")
#     st.write("Simply click on one of the buttons above to get started, and let us take care of the rest! Travel planning has never been easier.""")
#     st.write("")
    
#     # Buttons
#     if st.button("Rating"):
#         st.session_state.selected_option = "rating"
#     if st.button("price"):
#         st.session_state.selected_option = "price"
#     if st.button("amenities"):
#         st.session_state.selected_option = "amenities"
    
#     # Display content based on selected option
#     if st.session_state.selected_option == "rating":
#         st.write("You selected Rating.")
#         sort_rating()
#         # Call your rating.py file here
#     elif st.session_state.selected_option == "price":
#         st.write("You selected price")
#         sort_price()
#         # Call your other1.py file here
#     elif st.session_state.selected_option == "amenities":
#         st.write("You selected amenities")
#         sort_amenities()
#         # Call your other2.py file here

# if __name__ == "__main__":
#     main()

# BACKGROUND IMAGE CODE --------------------------------------------------------------------------------------------------------------
# import base64
# import streamlit as st
# import plotly.express as px

# df = px.data.iris()

# @st.cache_data 
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# img = get_img_as_base64("image1.jpg")

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://unsplash.com/photos/ypqyuASFNps/download");
# background-repeat: no-repeat;
# background-attachment: local;
# background-size: cover;
# background-position: center;
# position: absolute;
# top: 0;
# left: 0;
# width: 100%;
# height: 100%;
# }}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}

# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)
# st.title("It's summer!")
# st.sidebar.header("Configuration")

# with st.container():
#     st.header("Big one")
#     st.markdown(
#         "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#     )
#     st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))
# with st.container():
#     st.header("Big 2")
#     st.markdown(
#         "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#     )
#     st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))
# with st.container():
#     st.header("Big 3")
#     st.markdown(
#         "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#     )
#     st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))
# with st.container():
#     st.header("Big 4")
#     st.markdown(
#         "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#     )
#     st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))

import json 
import requests 

import streamlit as st 
from streamlit_lottie import st_lottie 
url = requests.get( 
	"https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json") 
url_json = dict() 
if url.status_code == 200: 
	url_json = url.json() 
else: 
	print("Error in URL") 

# HELP PAGE
import streamlit as st

def help_page():
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
            # this is ewhere lastly i copied my friend

        # Add more FAQ items as needed
        # FAQ 2
        with st.expander("How do I provide feedback?"):
            st.markdown("""
            We value your feedback! You can provide feedback by:
            - Clicking on the 'Feedback' button on the sidebar.
            - Sending us an email at feedback@example.com.
            """)
        with st.expander("How do I provide feedback?"):
            st.markdown("""
            We value your feedback! You can provide feedback by:
            - Clicking on the 'Feedback' button on the sidebar.
            - Sending us an email at feedback@example.com.
            """)

        with st.expander("How do I provide feedback?"):
            st.markdown("""
            We value your feedback! You can provide feedback by:
            - Clicking on the 'Feedback' button on the sidebar.
            - Sending us an email at feedback@example.com.
            """)

    with col2:
        # Add the GIF and center the button
        st_lottie(url_json, 
            # change the direction of our animation 
            reverse=True, 
            # height and width of animation 
            height="50%", 
            width="100%", 
            # speed of animation 
            speed=1, 
            # means the animation will run forever like a gif, and not as a still image 
            loop=True, 
            # quality of elements used in the animation, other values are "low" and "medium" 
            quality='high', 
            # This is just to uniquely identify the animation 
            key='Car'
        ) 
        st.markdown("""
            <div style="text-align: center;">
            <p style="overflow-wrap: break-word; word-wrap: break-word; text-align: center;">
            means the animation will run forever like a gif, and not as a still image 
            </p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<center><button>READMORE</button></center>", unsafe_allow_html=True)

# Sidebar navigation
selected_page = st.sidebar.radio("Navigation", ["Help"])

# Display selected page
if selected_page == "Home":
    # Display your home page content
    st.write("Welcome to the home page!")
elif selected_page == "Help":
    # Display the help page
    help_page()



