# Sold Price Map

## Overview

This project is a Flask web application that visualizes house prices on a 100x100 grid. The prices are categorized into different ranges, and each range is represented with a different color on the map.

## Requirements

- Python 3.7+
- Flask
- Matplotlib
- NumPy

## How to Run

1. Install the dependencies:
   ```bash
   pip install Flask matplotlib numpy
    ```

Run the application:
   ```bash
python app.py
```
Open your web browser and go to http://127.0.0.1:5000/ to view the map.

## How to Run
To ensure everything is working correctly, run the unit tests:

## Project Structure

app.py: Contains the Flask application, API endpoints, and logic for generating the plot.
templates/index.html: The HTML template used to display the plot.
test_app.py: Unit tests for the Flask application.

## Notes
The application is designed to be simple and demonstrate the use of Flask and Matplotlib.
The data is color-coded based on the percentiles of house prices, ensuring an effective visual representation.