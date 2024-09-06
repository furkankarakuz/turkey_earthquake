from config import URL
from bs4 import BeautifulSoup as bs
from datetime import datetime

import requests


class RequestProcess:
    """
    Handles the process of making requests to a given URL, fetching earthquake data and processing it into a structured format.

    Attributes:
        url (str): The base URL used for making requests to fetch earthquake data.
    """

    def __init__(self):
        """
        Initializes the RequestProcess class with the base URL from the config.
        """
        self.url = URL

    def get_data(self, start_date: tuple[int, int, int], end_date: tuple[int, int, int], city: str = "All") -> list:
        """
        Retrieves earthquake data within the specified date range and for a specific city.

        Args:
            start_date (tuple[int, int, int]): Start date for earthquake data
            end_date (tuple[int, int, int]): End date for earthquake data
            city (str, optional): The name of the city for which to retrieve earthquake data. Defaults to "All".

        Returns:
            list: A list of dictionaries, each containing earthquake data including depth, latitude, longitude, location, magnitude, day, and time.

        Notes:
            The `start_date` and `end_date` arguments must be tuples in the format (YYYY, MM, DD).
        """

        self.all_data = []
        for selected_month in self.get_month_range(start_date, end_date):
            selected_url = self.url + selected_month + ".xml"
            r = requests.get(selected_url)
            if r.status_code == 200:
                content = bs(r.content, "lxml")
                montly_data = content.find_all("earhquake")
                self.concat_monthly_data(montly_data)
            else:
                return None
        else:
            return self.all_data

    def get_month_range(self, start_date: tuple[int, int, int], end_date: tuple[int, int, int]) -> list:
        """
        Generates a list of month identifiers (YYYYMM) between the specified start and end dates, inclusive.

        Args:
            start_date (tuple[int, int, int]): Start date for earthquake data
            end_date (tuple[int, int, int]): End date for earthquake data

        Returns:
            list: A list of strings in the format "YYYYMM" representing each month between the start and end dates.

        Notes:
            The function starts from the specified start date and iterates month by month until it reaches the end date.
            It includes both the start and end months in the output.
            The `start_date` and `end_date` arguments must be tuples in the format (YYYY, MM, DD).
        """

        start_date = datetime(start_date[0], start_date[1], 1)
        end_date = datetime(end_date[0], end_date[1], 1)

        date_list = []
        current_date = start_date
        while current_date <= end_date:
            date_list.append(f"{current_date.year}{current_date.month:02}")
            next_month = current_date.month % 12 + 1
            next_year = current_date.year + (current_date.month // 12)
            current_date = datetime(next_year, next_month, 1)

        return date_list

    def concat_monthly_data(self, montly_data: list) -> None:
        """
        Concatenates and processes monthly earthquake data into a single list of dictionaries.

        Args:
            monthly_data (list): A list of BeautifulSoup elements, where each element represents an earthquake record from the monthly XML data.

        Returns:
            None: The function modifies the `self.all_data` attribute in place, appending the processed earthquake data.

        Notes:
            Each earthquake record is expected to have the following attributes: "depth", "lat", "lng", "lokasyon", "mag", and "name".
            The function processes each record to create a dictionary with specific keys: "depth", "lat", "lng", "location", "magnitude", "day", and "time".
            The "location" field is processed to exclude a specific substring ("REVIZE") if it is present.
            The "day" and "time" fields are extracted from the "name" attribute, which is assumed to be in the format "YYYY.MM.DD HH:MM:SS".
        """
        for data in montly_data:
            self.all_data.append({
                "depth": data.get("depth", "Unknown"),
                "lat": data.get("lat", "Unknown"),
                "lng": data.get("lng", "Unknown"),
                "location": (lambda text, limit: text[:text.find(limit)] if text.find(limit) != -1 else text)(data.get("lokasyon", "Unknown").strip(), "REVIZE"),
                "magnitude": data.get("mag", "Unknown"),
                "day": data.get("name", "Unknown").split()[0],
                "time": data.get("name", "Unknown").split()[1]
            })
