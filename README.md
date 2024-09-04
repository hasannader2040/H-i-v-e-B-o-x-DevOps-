# restful-opensensemap-Api

## [🚀 Project Purpose](#project-purpose)

## [🧩 Components](#components)

## [📑 Endpoints](#endpoints)

## [Current Version](#current-version)

## [🏷️ How to Run](#how-to-run)

## [⚙️ Setup](#setup)

## [🖼️ Photos](#photos)

## [💡 Contributing](#contributing)

## [📄 License](#license)




 # 🌡️ SenseBox API #

## 🚀 Project Purpose ## 
<a name="project-purpose"></a>

The SenseBox API is a project designed to simulate a simple environment monitoring system. It provides basic endpoints to retrieve temperature data and expose metrics for monitoring the health of the application. This project serves as a demonstration of how to build a RESTful API using Flask in Python, along with integrating Prometheus for metrics collection.




## 🧩 Components ## 
<a name="components"></a>
The project consists of the following key components:

**Flask Application**: A lightweight Python web framework used to create RESTful routes for interacting with the simulated environment data.
**Prometheus Client**: A library used to expose metrics that can be scraped by Prometheus for monitoring the application's performance and usage.
**Temperature Simulation**: A simple function that generates random temperature data to simulate the SenseBox environment.


## 📑 Endpoints##
<a name="endpoints"></a>

**🔍 /metrics**

**Description**: Returns default Prometheus metrics about the application.
**Method**: GET
**Response**: Prometheus-formatted metrics data, including the request count, memory usage, and more.

**🌡️/temperature**
**Description**: Retrieves simulated temperature data and provides an assessment of the current status based on the average temperature.
**Method**: GET
Response: JSON object containing the average temperature and a status message ("Too Cold", "Good", "Too Hot").

## Current Versio ## 
<a name="current-version"></a>

**Version**: 1.0.0




## 🏷️ How to Run ## 
<a name="how-to-run"></a>

**📋Prerequisites**
**Python 3.12** or higher
**Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

 ## ⚙️Setup ##
 <a name="setup"></a>

Clone the repository:

# Clone the repository

```console
git clone https://github.com/yourusername/sensebox-api.git
```

# Change directory to the project folder
```console
cd sensebox-api
```

# Create and activate a virtual environment:


**python3 -m venv myenv**
```console
source myenv/bin/activate
```

**Install dependencies**:

```console
pip install -r requirements.txt
```

**Run the Flask application**:

```console
python app.py
```

Access the application:

Navigate to http://127.0.0.1:5000/metrics for Prometheus metrics.
Navigate to http://127.0.0.1:5000/temperature to get the temperature data.


## 🖼️Photos ## 
<a name="photos"></a>
 

## 💡 Contributing##
<a name="contributing"></a>

Feel free to contribute to this project by forking the repository and creating pull requests. Any improvements or suggestions are welcome. 🛠️

## 📄 License ##
<a name="license"></a>
This project is licensed under the MIT License. See the LICENSE file for more details.




