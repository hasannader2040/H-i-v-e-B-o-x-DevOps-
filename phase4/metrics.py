import os
import random  # Simulating senseBox data fetch
from flask import Flask, Response, jsonify
from prometheus_client import generate_latest, Counter # type: ignore

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'

REQUEST_COUNT = Counter('request_count', 'App Request Count')

@app.route('/metrics')
def metrics():
    REQUEST_COUNT.inc()
    return Response(generate_latest(), mimetype='text/plain')

def fetch_temperature_data():
    # Simulated data; replace with actual data fetching logic
    return [random.uniform(5, 40) for _ in range(10)]

@app.route('/temperature')
def temperature():
    temps = fetch_temperature_data()
    avg_temp = sum(temps) / len(temps)
    if avg_temp < 10:
        status = "Too Cold"
    elif 10 <= avg_temp <= 36:
        status = "Good"
    else:
        status = "Too Hot"
    
    return jsonify({
        "average_temperature": avg_temp,
        "status": status
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


# /////

# print(prometheus_client.__version__)
