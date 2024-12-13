# SurfsUp- SQLAlchemy Challenge

## Project Overview
This project, titled **SurfsUp**, explores climate data for Honolulu, Hawaii, using Python, SQLAlchemy, Pandas, Matplotlib, and Flask. The goal is to analyze climate patterns and design a Flask API to provide insights for trip planning.

## Features
### Part 1: Climate Analysis
Using the `hawaii.sqlite` database, the analysis includes:
1. **Precipitation Analysis**
   - Retrieved the last 12 months of precipitation data.
   - Visualized results with a time-series plot.
   - Generated summary statistics for precipitation.

2. **Station Analysis**
   - Identified the total number of stations.
   - Determined the most active station and calculated its min, max, and average temperatures.
   - Queried and visualized temperature observations for the most active station as a histogram.

### Part 2: Flask API
Developed API routes based on the analysis:
- `/` : Lists all available routes.
- `/api/v1.0/precipitation` : Returns the last 12 months of precipitation data as JSON.
- `/api/v1.0/stations` : Provides a JSON list of all stations.
- `/api/v1.0/tobs` : Returns temperature observations for the most active station over the past year as JSON.
- `/api/v1.0/<start>` : Calculates min, avg, and max temperatures from a given start date to the dataset end.
- `/api/v1.0/<start>/<end>` : Calculates min, avg, and max temperatures for a specified date range.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Brendan838/SurfsUp.git
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Access the API locally at `http://127.0.0.1:5000/`.


