# from importlib.resources import read_binary
# import pandas as pd  # pip install pandas openpyxl
# import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
# from openpyxl import load_workbook
# import numpy as np
# from sklearn.linear_model import LinearRegression
from PIL import Image
# import webbrowser
import datetime
from stardata import data

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Starbooks",
                   page_icon=":flying_saucer:", layout="wide")
st.title(":rocket: Welcome to Starbooks")
st.subheader("Start booking your flight now and experience the joy and excitement of interstellar travel with your love ones!")

st.markdown("""---""")


# ---- SIDEBAR ----

# pnri = Image.open('pnri.png')
# st.sidebar.image(pnri)
# st.sidebar.header("Philippine Nuclear Reasearch Institute")
# st.write("Philippine Nuclear Reasearch Institute")

# ---- SIDEBAR ----
st.markdown("##")

col1, col2, col3, col4 = st.columns(4)

with col1:
    title = st.text_input('Search Stars')
    st.write('Showing results for', title)
    

with col2:
    d1 = st.date_input(
        "Check-in date",
        datetime.date(2022, 10, 1), key="d1")
    st.write(f'Your Check-in date is: {d1}')

with col3:
    d2 = st.date_input(
        "Check-out date",
        datetime.date(2019, 10, 2), key="d2")
    st.write(f'Your Check-out date is: {d2}')

with col4:
    option = st.selectbox(
        'How many are you?',
        ('Solo', 'Pair', 'Group'))

    st.write('You selected:', option)

# st.video("https://www.youtube.com/watch?v=FsrMPexJkI4")
# st.image("https://apod.nasa.gov/apod/image/2210/Lu20220729-0826_1050.jpg")

st.markdown("##")
st.subheader("🔥 Hot Right Now!")

star = []
for i in data.keys():
    star.append(i)



for i in data.keys():    
    with st.container():
        st.write(i)
        col1, col2, col3 = st.columns(3)

        with col1:
            betelgeuse = Image.open(data[i]['image'])
            st.image(betelgeuse)

        with col2:
            st.write(data[i]['description'])

        with col3:
            # st.write(data[i]['distance'])
            st.write('Distance from the sun: ', data[i]['distance'])
            if st.button('Reserve', key = i):
                st.write('Congratulations! You reserved this star')
                st.balloons()

    # You can call any Streamlit command, including custom components:
    # st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'Made by Andrei Cyril Gimoros and Irichelle Monterozo from Aycy Tech'; 
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 1px;
            }
            # header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
