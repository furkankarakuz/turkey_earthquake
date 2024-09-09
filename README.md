# 🌍 Turkey Earthquake Visualization Project
Welcome to the Turkey Earthquake Visualization Project! 🚀 This project aims to provide an interactive and insightful view of earthquake data across Turkey using Streamlit and Folium. 📊🗺️
<br><br>

## 📊 Data Source
The earthquake data used in this project is obtained from **Boğaziçi University Kandilli Observatory and Earthquake Research Institute**. For more information about the data, you can visit their official [website](http://www.koeri.boun.edu.tr/sismo).
<br><br>

## 📚 Overview
This project visualizes earthquake data from Turkey, including details such as magnitude, depth, and location. It offers various visualization options like markers, clusters, and heatmaps to help users understand earthquake patterns and trends. 🏔️🔥
<br><br>

## 🎥 Live Demo
Want to see the project in action? Click [here](https://turkey-earthquake.streamlit.app) to view the live demo! 🚀🌐
<br><br>

## 🚀 Features
- **Interactive Visualizations**: Choose between markers, clusters, and heatmaps to view earthquake data.
- **Dynamic Filters**: Filter data by depth, magnitude, and location.
- **Custom Date Range**: Select the date range for which you want to visualize the data.
- **Responsive Design**: Adjusts to fit various screen sizes and resolutions.
<br><br>

## 📈 How It Works
1. **Data Retrieval**: The project fetches earthquake data from an external source.
2. **Data Filtering**: Users can filter data based on depth, magnitude, and location.
3. **Visualization**: The data is visualized using interactive maps with different visualization types.
<br><br>


## 💻 Getting Started
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/furkankarakuz/turkey_earthquake.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd turkey_earthquake
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    streamlit run main.py
    ```
<br><br>

## 🛠️ Dependencies
The project requires the following Python libraries:
- `beautifulsoup4==4.12.3`
- `folium==0.17.0`
- `pandas==2.2.2`
- `requests==2.32.3`
- `streamlit==1.38.0`
- `lxml==5.3.0`
<br><br>

## 📂 Project Structure
- `main.py`: The main Streamlit application file.
- `data_process.py`: Contains data processing functions.
- `request_process.py`: Handles data retrieval from external sources.
- `map_visualization_process.py`: Manages map visualizations.
- `streamlit_tools.py`: Manages Streamlit sidebar tools and user inputs.
- `requirements.txt`: Lists all project dependencies.
<br><br>

## 🤔 Contributing
Feel free to contribute to this project! Open an issue or submit a pull request if you have suggestions or improvements.
