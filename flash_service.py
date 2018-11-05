from flask import Flask, jsonify, request
import math
import requests
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
  """
  Returns the string "Hello, world" to the caller
  """
  return_dict = {"name": "Deepthi Nacharaju"}
  return jsonify(return_dict)


@app.route("/hello/<name>", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  return_dict = {"message": "Hello, there {}".format(name)}
  return jsonify(return_dict) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well


@app.route("/distance", methods=["POST"])
def dist():
  r = request.get_json() # parses the POST request body as JSON
  s = math.sqrt((r["a"][1] - r["b"][1]) ** 2 + (r["a"][0] - r["b"][0]) ** 2) # adds JSON dict parameter "a" and "b" together
  r["distance"] = s
  return jsonify(r)


if __name__ == "__main__":
  app.run(host="127.0.0.1")
