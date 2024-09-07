from request_process import RequestProcess as rp
from data_process import DataProcess as dp
from map_visualization_process import MapVisualizationProcess as mvp
from datetime import datetime


date_range = (datetime(2024, 9, 1), datetime(2024, 9, 8))
data = rp().get_request(*date_range)

option_filter = {"depth": {"max": 30, "min": 5}, "magnitude": {"max": 10, "min": 2}, "location_list": ["All"]}

if data:
    dataframe = dp().data_filter(data, *date_range, option_filter)
    if dataframe:
        mvp().map_visualization(dataframe, "HeatMap")
