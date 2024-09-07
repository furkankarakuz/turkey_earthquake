import folium
import pandas as pd
from folium import plugins


class MapVisualizationProcess():
    """
    A class to visualize geographic data using Folium on a map.

    Attributes:
        zoom (int): The initial zoom level of the map.
        m (folium.Map): The Folium map object to which visualizations are added.
    """

    def __init__(self, zoom: int = 5) -> None:
        """
        Initializes the MapVisualizationProcess class with a given zoom level.

        Args:
            zoom (int, optional): Initial zoom level for the map (default is 5).
        """
        self.zoom = zoom
        self.m = folium.Map(location=[40, 32], zoom_start=self.zoom)

    def map_visualization(self, df: pd.DataFrame, viz_type: str = "Marker") -> None:
        """
        Adds geographic data to the map in different formats such as markers, clusters, or heatmaps based on the provided visualization type.

        Args:
            df (pandas.DataFrame): The DataFrame containing the geographic data.
                Must include 'lat' and 'lng' columns for latitude and longitude.
                Optionally, include 'location' for popup text and 'magnitude' for the size or intensity of markers.
            viz_type (str, optional): The type of visualization to be applied.
                Options include:
                - "Marker": Adds regular markers and circle markers (default).
                - "Cluster": Groups markers into clusters.
                - "HeatMap": Visualizes the data as a heatmap based on location.

        Returns:
            None: The map is saved as an HTML file ('map.html').
        """

        if viz_type == "Marker":
            df.apply(lambda row: folium.Marker(location=[row['lat'], row['lng']], popup=row['location']).add_to(self.m), axis=1)
            df.apply(lambda row: folium.CircleMarker(location=[row['lat'], row['lng']], radius=row['magnitude'] * 5, fill_color='red', fill=True, fill_opacity=0.6).add_to(self.m), axis=1)
        elif viz_type == "Cluster":
            marker_cluster = plugins.MarkerCluster().add_to(self.m)
            df.apply(lambda row: folium.Marker(location=[row['lat'], row['lng']], popup=row['location']).add_to(marker_cluster), axis=1)
        elif viz_type == "HeatMap":
            folium.plugins.HeatMap(list(zip(df["lat"], df["lng"], df["magnitude"]))).add_to(self.m)

        self.m.save('map.html')
