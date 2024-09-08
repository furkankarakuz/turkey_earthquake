from request_process import RequestProcess as rp
from data_process import DataProcess as dp
from map_visualization_process import MapVisualizationProcess
from streamlit_tools import StreamlitTools


import streamlit as st
import warnings


warnings.filterwarnings('ignore')


def display_title():
    """Display the main title of the application."""
    st.markdown("<center><h2>Turkey Earthquake</h2></center>", unsafe_allow_html=True)


def setup_sidebar(slt):
    """Set up the sidebar tools using StreamlitTools."""
    st.sidebar.title("Select Range for Data Filter")
    slt.sidebar_tools()


def run_filter_button():
    """Display and handle the Run Filter button action."""
    return st.sidebar.button("Run Filter")


def display_data(dataframe):
    """Display the filtered data and the visualization map."""
    st.dataframe(dataframe[["day", "time", "magnitude", "depth", "location"]], width=1000)
    st.components.v1.html(open('map.html', 'r').read(), width=1000, height=600)


def display_no_data():
    """Display a message if no data is found."""
    st.markdown("<center><h2>Data Not Found :(</h2></center>", unsafe_allow_html=True)


def fetch_and_filter_data(slt, rp_instance, dp_instance):
    """Fetch and filter data based on user inputs."""
    data = rp_instance.get_request(*slt.date_range)
    if data:
        dataframe = dp_instance.data_filter(data, *slt.date_range, slt.option_filter)
        return dataframe, True
    return None, None


def main():
    """Main function to run the Streamlit app."""
    display_title()

    slt = StreamlitTools()
    setup_sidebar(slt)

    if run_filter_button():
        dataframe, control = fetch_and_filter_data(slt, rp(), dp())
        if control:
            mvp = MapVisualizationProcess()
            mvp.map_visualization(dataframe, slt.type)
            display_data(dataframe)
        else:
            # Display message if no data
            display_no_data()


if __name__ == "__main__":
    main()
