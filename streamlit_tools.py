from datetime import datetime, timedelta
from city_list import city_list
import streamlit as st


st.set_page_config(layout="wide")
secret_url = st.secrets["URL"]



class StreamlitTools():
    """
    A class to handle the Streamlit sidebar tools for filtering and visualizing earthquake data.

    Attributes:
        option_filter (dict): Dictionary storing filter options such as depth, magnitude, and location.
    """

    def __init__(self):
        """Initializes the StreamlitTools class with default filter options."""
        self.option_filter = {"depth": {"min": 5, "max": 30}, "magnitude": {"min": 3, "max": 7}, "location_list": []}

    def sidebar_tools(self):
        """Sets up the Streamlit sidebar widgets for user inputs including city selection, date range, visualization type, and filters for depth and magnitude range."""

        self._select_city()
        self._select_date_range()
        self._select_visualization_type()
        self._select_depth_range()
        self._select_magnitude_range()

    def _select_city(self):
        """Creates a multi-select widget for cities."""

        city_options = st.sidebar.multiselect("Select a city or cities (Default : all)", city_list)
        self.option_filter["location_list"] = city_options

    def _select_date_range(self):
        """Creates a date range input widget for filtering earthquake data."""

        st.sidebar.title("")
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        date_range = st.sidebar.date_input("Select date range", (yesterday, today), datetime(2020, 1, 1), today, format="DD.MM.YYYY")
        self.date_range = datetime(date_range[0].year, date_range[0].month, date_range[0].day), datetime(date_range[1].year, date_range[1].month, date_range[1].day)

    def _select_visualization_type(self):
        """Creates a radio button widget for selecting the type of visualization (Marker, Cluster, HeatMap)."""

        st.sidebar.title("")
        self.type = st.sidebar.radio("What's your decision about visualization type", ["Marker", "Cluster", "HeatMap"])

    def _select_depth_range(self):
        """Creates a slider widget for selecting the depth range."""

        st.sidebar.title("")
        depth_slider = st.sidebar.slider("Select depth range of values", 3, 100, (self.option_filter["depth"]["min"], self.option_filter["depth"]["max"]))

        self.option_filter["depth"] = {"min": depth_slider[0], "max": depth_slider[1]}

    def _select_magnitude_range(self):
        """Creates a slider widget for selecting the magnitude range."""

        st.sidebar.title("")
        magnitude_slider = st.sidebar.slider("Select magnitude range of values", 2, 8, (self.option_filter["magnitude"]["min"], self.option_filter["magnitude"]["max"]))

        self.option_filter["magnitude"] = {"min": magnitude_slider[0], "max": magnitude_slider[1]}
