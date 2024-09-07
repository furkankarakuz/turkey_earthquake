import pandas as pd
from datetime import datetime


class DataProcess:
    """
    A class for processing and filtering earthquake data.

    Methods:
        data_filter(data: list, start_date: datetime, end_date: datetime, filter_option: dict) -> pd.DataFrame
    """
    def __init__(self):
        pass

    def data_filter(self, data, start_date: datetime, end_date: datetime, filter_option: dict) -> pd.DataFrame:
        """
        Filters the earthquake data based on date range, depth, magnitude, and location.

        Args:
            data (list): List of dictionaries containing earthquake data.
            start_date (datetime): Start date for filtering the data.
            end_date (datetime): End date for filtering the data.
            filter_option (dict): Dictionary containing filtering options such as depth, magnitude, and location list.

        Returns:
            pd.DataFrame: A DataFrame containing the filtered earthquake data.
        """
        # Set DataFrame
        df = pd.DataFrame(data)

        # Data Filter with Date
        df["day"] = pd.to_datetime(df["day"], format="%Y.%m.%d")
        df = df[(df["day"] >= start_date) & (df["day"] <= end_date)]
        df["day"] = df["day"].dt.strftime("%d.%m.%Y")

        # Data Filter with Depth and Magnitude
        df = df[(df["depth"] >= filter_option["depth"]["min"]) & (df["depth"] <= filter_option["depth"]["max"])]
        df = df[(df["magnitude"] >= filter_option["magnitude"]["min"]) & (df["magnitude"] <= filter_option["magnitude"]["max"])]

        # Data Filter with Location List
        if not ("All" in filter_option["location_list"]):
            df_location = pd.DataFrame(columns=df.columns)
            for location in filter_option["location_list"]:
                df_location = pd.concat([df_location, df[df["location"].str.contains(f"({location})", na=False)]], ignore_index=True)
            df = df_location.copy()
        df.sort_index(inplace=True)
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)
        return df
