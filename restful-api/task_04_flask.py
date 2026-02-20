#!/usr/bin/python3
"""
A simple Flask API to manage user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames in JSON format."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the operational status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the full object for a specific username.
    Returns 404 if the user is not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handles POST requests to add a new user.
    Validates JSON integrity, existence of username, and duplicates.
    """
    # 1. Check if the request is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check if 'username' is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Check if 'username' already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add user to the dictionary and return 201 Created
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
