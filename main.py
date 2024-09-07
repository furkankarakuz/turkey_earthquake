from request_process import RequestProcess as rp
from data_process import DataProcess as dp
from map_visualization_process import MapVisualizationProcess
from datetime import datetime, timedelta
from city_list import city_list

import streamlit as st
import warnings


warnings.filterwarnings('ignore')


st.markdown("<center><h2>Turkey Earthquake</h2></center>", unsafe_allow_html=True)
st.sidebar.title("Select Range for Data Filter")
st.sidebar.title("")


class StreamlitTools:
    """
    A class to handle the Streamlit sidebar tools for filtering and visualizing earthquake data.

    Attributes:
        option_filter (dict): Dictionary to store filter options for depth, magnitude, and location.
        date_range (tuple): Tuple containing start and end dates for the data filter.
        type (str): Type of visualization selected by the user.
    """
    def __init__(self):
        """
        Initializes the StreamlitTools class with default filter options.
        """
        self.option_filter = {"depth": {"min": 5, "max": 30}, "magnitude": {"min": 3, "max": 7}, "location_list": []}

    def sidebar_tools(self):
        """
        Sets up the Streamlit sidebar widgets for user inputs including city selection, date range, visualization type, and filters for depth and magnitude.
        """
        city_options = st.sidebar.multiselect("Select a city or cities", city_list)

        st.sidebar.title("")
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        date_range = st.sidebar.date_input("Select date range", (yesterday, today), datetime(2020, 1, 1), today, format="DD.MM.YYYY")
        self.date_range = datetime(date_range[0].year, date_range[0].month, date_range[0].day), datetime(date_range[1].year, date_range[1].month, date_range[1].day)

        st.sidebar.title("")
        self.type = st.sidebar.radio("What's your decision about visualization type", ["Marker", "Cluster", "HeatMap"])

        st.sidebar.title("")
        depth_slider = st.sidebar.slider("Select depth range of values", 3, 100, (self.option_filter["depth"]["min"], self.option_filter["depth"]["max"]))

        st.sidebar.title("")
        magnitude_slider = st.sidebar.slider("Select magnitude range of values", 2, 8, (self.option_filter["magnitude"]["min"], self.option_filter["magnitude"]["max"]))

        self.option_filter["depth"] = {"min": depth_slider[0], "max": depth_slider[1]}
        self.option_filter["magnitude"] = {"min": magnitude_slider[0], "max": magnitude_slider[1]}
        self.option_filter["location_list"] = city_options


slt = StreamlitTools()
try:
    slt.sidebar_tools()
except:
    pass

st.sidebar.title("")
button_pressed = st.sidebar.button("Run Filter")

if button_pressed:
    # Fetch the earthquake data based on the selected date range
    data = rp().get_request(*slt.date_range)
    if data:
        # Filter the data based on user inputs
        dataframe = dp().data_filter(data, *slt.date_range, slt.option_filter)
        if len(dataframe) > 0:
            mvp = MapVisualizationProcess()
            mvp.map_visualization(dataframe, slt.type)

            # Display the filtered data and the map
            st.dataframe(dataframe[["day", "time", "magnitude", "depth", "location"]], width=1000)
            st.components.v1.html(open('map.html', 'r').read(), width=1000, height=600)
        else:
            # Display a message if no data is found
            st.write("")
            st.write("")
            st.write("")
            st.markdown("<center><h2>Data Not Found :( </h2></center>", unsafe_allow_html=True)
    button_pressed = False  # Reset button state after processing
