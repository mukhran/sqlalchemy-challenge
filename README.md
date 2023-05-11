# sqlalchemy-challenge. 
## A climate analysis in Honolulu, Hawaii.

- climate_starter.ipynb - climate analysis and visualization
- app.py - Flask web
- Resources -  csv files and sqlite data base file

## Part 1: Analyze and Explore the Climate Data
Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database were used. SQLAlchemy ORM queries, Pandas, and Matplotlib were used. 

## Part 2: Design Your Climate App
A Flask API, based on the queries from part 1, was designed.

/
Start at the homepage.
List of all the available routes.

/api/v1.0/precipitation
Convert the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of a dictionary.

/api/v1.0/stations
Return a JSON list of stations from the dataset.

/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start>
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

/api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
