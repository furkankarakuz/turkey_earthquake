from bs4 import BeautifulSoup as bs
from datetime import datetime
from streamlit_tools import secret_url

import requests


class RequestProcess:
    def __init__(self):
        """
        Initializes the RequestProcess class with the base URL from the config.

        Methods:
            get_request(start_date: datetime, end_date: datetime) -> list
            month_range(start_date: datetime, end_date: datetime) -> list
            get_monthly_data(monthly_data: dict) -> dict
        """
        self.url = secret_url

    def get_request(self, start_date: datetime, end_date: datetime) -> list[dict]:
        """
        Retrieves earthquake data within the specified date range.

        Args:
            start_date (datetime): Start date for earthquake data.
            end_date (datetime): End date for earthquake data.

        Returns:
            Optional[list[dict]]: A list of dictionaries containing earthquake data, or None if an error occurs.
        """
        data = []
        try:
            for selected_month in self.month_range(start_date, end_date):
                selected_url = self.url + selected_month + ".xml"
                r = requests.get(selected_url)
                content = bs(r.content, "xml")
                # Corrected the tag name
                for monthly_data in content.find_all("earhquake"):
                    data.append(self.get_monthly_data(monthly_data))
            return data
        except:
            return None

    def month_range(self, start_date: datetime, end_date: datetime) -> list:
        """
        Generates a list of month identifiers (YYYYMM) between the specified start and end dates.

        Args:
            start_date (datetime): Start date for earthquake data.
            end_date (datetime): End date for earthquake data.

        Returns:
            list: A list of strings in the format "YYYYMM" representing each month between the start and end dates.
        """
        date_list = []
        current_date = start_date
        while current_date <= end_date:
            date_list.append(f"{current_date.year}{current_date.month:02}")
            next_month = current_date.month % 12 + 1
            next_year = current_date.year + (current_date.month // 12)
            current_date = datetime(next_year, next_month, 1)

        return date_list

    def get_monthly_data(self, monthly_data: dict) -> dict:
        """
        Processes a single month's earthquake data and returns a dictionary.

        Args:
            monthly_data: A BeautifulSoup element representing an earthquake record.

        Returns:
            dict: A dictionary with earthquake data.
        """
        return {
            "depth": float(monthly_data["Depth"]),
            "lat": monthly_data["lat"],
            "lng": monthly_data["lng"],
            "location": (lambda text, limit: text[:text.find(limit)] if text.find(limit) != -1 else text)(monthly_data.get("lokasyon", "Unknown").strip(), "REVIZE"),
            "magnitude": float(monthly_data["mag"]),
            "day": monthly_data["name"].split()[0],
            "time": monthly_data["name"].split()[1]
        }
