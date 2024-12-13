# Importing the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#set
# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
# Save reference to the table

Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`


measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#showing api options on root url

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date"
        f"/api/v1.0/start_date/end_date"

    )
    
#showing precitipation values for last full year

@app.route("/api/v1.0/precipitation")
def precipitation():
   
    session = Session(engine)
    last_12 = session.query(measurement.date,measurement.prcp).filter((measurement.date >= '2016-08-23') & (measurement.date <= '2017-08-23')).all()
    data = {}
    for r in last_12:
        data[str(r.date)] = r.prcp

    session.close()

    return jsonify(data)

#showing list of stations

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    station_names = session.query(station.name).all()
    data = []
    for s in station_names:
        data.append(s.name)
    session.close()
    return jsonify(data)

#listing temperatures observed for the most active station

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)
    tobs = session.query(measurement.tobs).filter((measurement.date >= '2016-08-23') & (measurement.date <= '2017-08-23') & (measurement.station == 'USC00519281'))
    data = [t.tobs for t in tobs]
    session.close()
    return jsonify(data)


#Dynamic Routes
#taking in <start> and <start>/<end> dates in the URL as arguments in our declared functions, and putting them as variables inside our session.query().filter()
#Returning a small dictionary of min, max, and average values

@app.route("/api/v1.0/<start>")
def start(start):

    session = Session(engine)
    aggs = session.query(func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.date >= start).all()
    arr = [a for a in aggs[0]]
    data = {
        "TMIN": round(arr[0],2),
        "TMAX": round(arr[1],2),
        "TAVG": round(arr[2],2)

    }
    session.close()
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    s = start
    e = end if end else '2017-08-23'

    session = Session(engine)
    aggs = session.query(func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter((measurement.date >= s) & (measurement.date <= e)).all()
    arr = [a for a in aggs[0]]
    data = {
        "TMIN": round(arr[0],2),
        "TMAX": round(arr[1],2),
        "TAVG": round(arr[2],2)

    }
    session.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)




# Start at the homepage.

# List all the available routes.

# /api/v1.0/precipitation

# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

# Return the JSON representation of your dictionary.

# /api/v1.0/stations

# Return a JSON list of stations from the dataset.
# /api/v1.0/tobs

# Query the dates and temperature observations of the most-active station for the previous year of data.

# Return a JSON list of temperature observations for the previous year.

# /api/v1.0/<start> and /api/v1.0/<start>/<end>

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

# Hints
# Join the station and measurement tables for some of the queries.

# Use the Flask jsonify function to convert your API data to a valid JSON response object.

