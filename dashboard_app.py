'''
Streamlit app to download recent job offers from linkedin based on keyword given by the user

Usage: 
streamlit run dashboard_app.py
'''

import pandas as pd
import streamlit as st


# configuration of the page
st.set_page_config(layout="wide")
SPACER = .2
ROW = 1


def hide_streamlit_header_footer():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)


def main():

    hide_streamlit_header_footer()

    hs_1, title, hs_2, header_button, hs_3 = st.columns((.05, ROW, .05, ROW*2, .05))
    with title:
        st.title('Instacart sales dashboard')

    with header_button:
        button_1, button_2, button_3, button_4 = st.columns(4)
        with button_1:
            week = st.selectbox('Week', ["Week 1", "Week 2"])

        with button_2:
            report = st.selectbox('Report', ["Sales", "Customer"])

        with button_3:
            department = st.selectbox('Department', ["All", "Department 1"])

        with button_4:
            ailse = st.selectbox('Aisle', ["All", "Aisle 1"])


if __name__ == "__main__":
    main()
