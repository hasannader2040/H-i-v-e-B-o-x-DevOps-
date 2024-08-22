# restful-opensensemap-Api


 🌡️ # SenseBox API # 

## sProject Purpose
The SenseBox API is a project designed to simulate a simple environment monitoring system. It provides basic endpoints to retrieve temperature data and expose metrics for monitoring the health of the application. This project serves as a demonstration of how to build a RESTful API using Flask in Python, along with integrating Prometheus for metrics collection.




Components
The project consists of the following key components:



Flask Application: A lightweight Python web framework used to create RESTful routes for interacting with the simulated environment data.
**Prometheus Client**: A library used to expose metrics that can be scraped by Prometheus for monitoring the application's performance and usage.
**Temperature Simulation**: A simple function that generates random temperature data to simulate the SenseBox environment.


## Endpoints

**/metrics**

**Description**: Returns default Prometheus metrics about the application.
**Method**: GET
**Response**: Prometheus-formatted metrics data, including the request count, memory usage, and more.
/temperature
**Description**: Retrieves simulated temperature data and provides an assessment of the current status based on the average temperature.
Method: GET
Response: JSON object containing the average temperature and a status message ("Too Cold", "Good", "Too Hot").
Current Version
Version: 1.0.0




How to Run
Prerequisites
Python 3.12 or higher
Virtual Environment: It's recommended to use a virtual environment to manage dependencies.


