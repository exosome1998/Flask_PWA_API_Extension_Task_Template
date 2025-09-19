"""Flask API for PWA extensions."""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import database_manager as dbHandler

api = Flask(__name__)
CORS(api)
limiter = Limiter(
    get_remote_address, app=api, default_limits=["200 per day", "50 per hour"]
)


@api.route("/", methods=["GET"])
def get():
    """Retrieve all extensions as JSON."""
    content = dbHandler.list_extension()
    return jsonify(content), 200


@api.route("/add_extension", methods=["POST"])
@limiter.limit("10 per minute")
def post():
    """Add a new extension via JSON."""
    data = request.get_json()
    if data and "name" in data:
        hyperlink = data.get("hyperlink", "http://default.com")
        about = data.get("about", "Default description")
        image = data.get("image", "default.jpg")
        language = data.get("language", "Python")
        dbHandler.insert_extension(data["name"], hyperlink, about, image, language)
        return jsonify({"message": "Added"}), 201
    return jsonify({"error": "Invalid data"}), 400


if __name__ == "__main__":
    api.run(debug=True, host="0.0.0.0", port=3000)
