from request_process import RequestProcess as rp
from data_process import DataProcess as dp
from datetime import datetime


date_range = (datetime(2024, 9, 3), datetime(2024, 9, 5))
data = rp().get_request(*date_range)

option_filter = {"depth": {"max": 10, "min": 0}, "magnitude": {"max": 10, "min": 0}, "location_list": ["All"]}

if data:
    dataframe = dp().data_filter(data, *date_range, option_filter)
    print(dataframe)