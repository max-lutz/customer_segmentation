'''
Streamlit app to download recent job offers from linkedin based on keyword given by the user

Usage: 
streamlit run dashboard_app.py
'''

import os
import pandas as pd
import streamlit as st

import plotly.graph_objects as go

# configuration of the page
st.set_page_config(layout="wide")
SPACER = .2
ROW = 1


@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)


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


def plot_metric(number, delta_number, title):
    config = {'staticPlot': True}

    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=number,
        title={"text": title, "font": {"size": 24}},
        delta={'reference': delta_number, 'relative': True},
        domain={'row': 0, 'column': 0}))

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        margin=dict(t=30, b=0),
        showlegend=False,
        plot_bgcolor="white",
        height=100,
    )

    st.plotly_chart(fig, use_container_width=True, config=config)


def main():

    hide_streamlit_header_footer()

    # HEADER
    title, _, header_button = st.columns((ROW, .05, ROW*2))
    with title:
        st.title('Instacart sales dashboard')

    with header_button:
        button_1, button_2, button_3, button_4 = st.columns(4)
        with button_1:
            week_list = [file for file in os.listdir("data/processed") if file[0:6] == "orders"]
            week_list = [file[7:-4] for file in week_list]
            week_list.sort(reverse=True)
            week = st.selectbox('Week', week_list[1:-1])

            df_orders = load_data(f"data/processed/orders_{week}.zip")
            df_orders_prev = load_data(f"data/processed/orders_{week_list[week_list.index(week)+1]}.zip")

        with button_2:
            report = st.selectbox('Report', ["Sales", "Customer"])

        with button_3:
            department = st.selectbox('Department', ["All", "Department 1"])

        with button_4:
            ailse = st.selectbox('Aisle', ["All", "Aisle 1"])

    st.write("")
    st.write("")

    col_1, _, col_2 = st.columns((ROW, .05, ROW))
    with col_1:
        _, col_1_1, _, col_1_2, _, col_1_3, _ = st.columns((0.1, ROW, .01, ROW, 0.1, ROW, 0.1))
        with col_1_1:
            plot_metric(len(df_orders["user_id"].unique()), len(df_orders_prev["user_id"].unique()), "Total users")

            # st.write("Take inspiration from https://github.com/andfanilo/social-media-tutorials/blob/master/20230816-stdashboard/streamlit_app.py")
            # st.write("and https://www.klipfolio.com/resources/dashboard-examples/sales")
        with col_1_2:
            plot_metric(len(df_orders["order_id"].unique()), len(df_orders_prev["order_id"].unique()), "Total orders")

        with col_1_3:
            plot_metric(df_orders["basket_size"].mean(), df_orders_prev["basket_size"].mean(), "Average basket size")

    st.write()

    st.write(df_orders)
    st.write(df_orders_prev)


if __name__ == "__main__":
    main()
