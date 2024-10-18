from flask import Flask, jsonify
import logging

version_number = 2


def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.DEBUG)

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
        app.logger.debug("Entering /temperature endpoint")
        try:
            temperature_celsius = 36
            response = jsonify({"temperature": f"The temperature is {temperature_celsius} degree celsius"})
            app.logger.debug(f"Temperature data: {response.get_json()}")
        except Exception as e:
            app.logger.error(f"Error in /temperature endpoint: {e}")
            response = jsonify({"error": str(e)}), 500
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)