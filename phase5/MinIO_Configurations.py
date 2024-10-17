from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_caching import Cache
from prometheus_client import Counter, generate_latest
import boto3
import json
from datetime import datetime, timedelta
import redis
import os

app = Flask(__name__)

# Valkey/Redis Cache configuration
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'

cache = Cache(app)

# MinIO configuration
MINIO_ENDPOINT = 'YOUR_MINIO_ENDPOINT'
MINIO_ACCESS_KEY = 'YOUR_MINIO_ACCESS_KEY'
MINIO_SECRET_KEY = 'YOUR_MINIO_SECRET_KEY'
MINIO_BUCKET_NAME = 'YOUR_BUCKET_NAME'

# Initialize S3 client
s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
)

# Data to be stored periodically
data_to_store = {
    "temperature": "22.5",
    "humidity": "60%"
}

# Prometheus Metrics
store_counter = Counter('manual_store_trigger_count', 'Count of /store endpoint calls')


# Function to store data
def store_data():
    """Store data into MinIO periodically"""
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    file_name = f"data_{current_time}.json"
    file_content = json.dumps(data_to_store)

    s3_client.put_object(
        Bucket=MINIO_BUCKET_NAME,
        Key=file_name,
        Body=file_content
    )
    # Cache the last store time
    cache.set('last_store_time', current_time)
    print(f"Data stored at {current_time}")


# Scheduler configuration
scheduler = BackgroundScheduler()
scheduler.add_job(store_data, 'interval', minutes=5)
scheduler.start()


@app.route('/store', methods=['POST'])
def store():
    store_data()
    store_counter.inc()  # Increment counter for Prometheus metrics
    return "Data stored manually.", 200


@app.route('/metrics', methods=['GET'])
def metrics():
    # Generate and return Prometheus metrics
    return generate_latest(), 200


@app.route('/readyz', methods=['GET'])
def readyz():
    # Check if 50% of senseBoxes are accessible (Example logic)
    sense_boxes_status = [True, True, False, False]
    accessible_boxes = sum(sense_boxes_status)
    total_boxes = len(sense_boxes_status)

    last_store_time = cache.get('last_store_time')
    if last_store_time:
        last_store_time = datetime.strptime(last_store_time, '%Y-%m-%dT%H:%M:%SZ')
        if (datetime.utcnow() - last_store_time) > timedelta(minutes=5):
            cache_old = True
        else:
            cache_old = False
    else:
        cache_old = True

    if accessible_boxes <= total_boxes // 2 and cache_old:
        return "Service Unavailable", 503
    return "Ready", 200


@app.route('/')
def index():
    return "Flask application with MinIO, APScheduler, Redis Cache and Prometheus"


if __name__ == "__main__":
    app.run(debug=True)


#  should I use this or something like that ? export FLASK_APP=app.py
# flask run