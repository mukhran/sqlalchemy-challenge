# sqlalchemy-challenge 
## A climate analysis in Honolulu, Hawaii.

- climate_starter.ipynb - climate analysis and visualization
- app.py - Flask web
- Resources -  csv files and sqlite data base file

## Part 1: Analyze and Explore the Climate Data
Python, SQLAlchemy ORM queries, Pandas, and Matplotlib were used to do a basic climate analysis and data exploration of climate database. 

## Part 2: Design Your Climate App
A Flask API, based on the queries from part 1, was designed.

/
Start at the homepage.
List of all the available routes.

<img width="417" alt="Screenshot 2023-05-10 at 10 16 43 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/8aa9fabc-c89c-4fa4-ae7e-14f8b457c01f">

/api/v1.0/precipitation
Convert the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
Return the JSON representation of a dictionary.

<img width="408" alt="Screenshot 2023-05-10 at 10 23 48 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/04f3a093-ce17-400b-9766-df81167f1443">


/api/v1.0/stations
Return a JSON list of stations from the dataset.

<img width="409" alt="Screenshot 2023-05-10 at 10 24 07 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/d76015e7-3de3-4f76-9081-50c2723be977">


/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.
Return a JSON list of temperature observations for the previous year.

<img width="381" alt="Screenshot 2023-05-10 at 10 24 27 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/a278f4ca-f7b6-4ba8-9009-4c5fd787e853">


/api/v1.0/<start>
For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
  
  <img width="413" alt="Screenshot 2023-05-10 at 10 25 09 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/0f8e7a3b-2ed5-4c12-936c-cffa933e14a4">


/api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
  
  <img width="524" alt="Screenshot 2023-05-10 at 10 26 20 PM" src="https://github.com/mukhran/sqlalchemy-challenge/assets/30066145/8a953713-9a2e-4c55-8e20-72cf7dbe167f">

