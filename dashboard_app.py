'''
Streamlit app to download recent job offers from linkedin based on keyword given by the user

Usage: 
streamlit run dashboard_app.py
'''

import pandas as pd
import streamlit as st


# configuration of the page
st.set_page_config(layout="wide")
# SPACER = .2
# ROW = 1


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
    st.title('Instacart users dashboard')
    st.markdown("""
                This app allows you scrape city bike information from https://api.citybik.es/v2/
                * The code can be accessed at [code](https://github.com/max-lutz/citybike_web_scraper).
                * You can select a country in the sidebar and download the data as csv once all the information have been retireved.
                """)

    hide_streamlit_header_footer()


if __name__ == "__main__":
    main()
