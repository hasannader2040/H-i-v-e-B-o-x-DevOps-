from flask import Flask, jsonify

version_number = 2

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        response = jsonify({"msg": "Welcome to Hasan api"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    @app.route("/version")
    def version():
        response = jsonify({"msg": f"the version is {version_number}"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    @app.route("/temperature")
    def temperature():
        temperature_celsius = 36
        response = jsonify({"temperature": f"The temperature is {temperature_celsius} degree celcius"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    return app
