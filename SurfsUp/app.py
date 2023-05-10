# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end dateformat should be 2017-08-23"

    )


"""Convert the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary."""
@app.route('/api/v1.0/precipitation')
def get_precipitation():
    
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    converted_date = (dt.datetime.strptime(most_recent_date, "%Y-%m-%d")).date()
    year_from_recent =  converted_date - dt.timedelta(days=365)
    data_precip_scores = session.query(Measurement.date, Measurement.prcp).\
            filter((Measurement.date>=year_from_recent) & (Measurement.date<=converted_date)).all()
    
    dict_percip = {}
    for key, value in data_precip_scores:
        dict_percip[key] = value
    return jsonify(dict_percip)

"""Return a JSON list of stations from the dataset"""
@app.route('/api/v1.0/stations')
def get_stations():
    stations = session.query(Station.name).all()
    #print(stations)
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)


"""Query the dates and temperature observations of the most-active station for the previous year of data.
"""
@app.route('/api/v1.0/tobs')
def get_tobs():
    
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    converted_date = (dt.datetime.strptime(most_recent_date, "%Y-%m-%d")).date()
    year_from_recent =  converted_date - dt.timedelta(days=365)
    
    temp_date_station = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').\
    filter((Measurement.date>=year_from_recent) & (Measurement.date<=converted_date)).all()
    USC00519281 = list(np.ravel(temp_date_station))

    return jsonify(USC00519281)

@app.route('/api/v1.0/<start>')
def get_temp_start(start):

    start_date = (dt.datetime.strptime(start, "%Y-%m-%d")).date()
    results = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter((Measurement.date>=start_date)).all()
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)

@app.route('/api/v1.0/<start>/<end>')
def get_temp_srat_end(start, end):

    start_date = (dt.datetime.strptime(start, "%Y-%m-%d")).date()
    end_date = (dt.datetime.strptime(end, "%Y-%m-%d")).date()
    results = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter((Measurement.date>=start_date) & (Measurement.date<=end_date)).all()

    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)


session.close()

if __name__ == '__main__':
    app.run(debug=True)