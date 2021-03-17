from flask import Flask, jsonify, request
import overpass

api = overpass.API()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return ' Hello World ! '

@app.route("/api/")
def newapi():
    return jsonify({"restos":"http://127.0.0.1:5000/api/restos"})

@app.route("/api/restos/")
def apirestos():
    return "Hello la famille"

@app.route("/api/restos/<ville>", methods=["GET"])
def magasin(ville):
    if request.method == "GET":
        response = api.get (f"""area[name="{ville}"]; node[amenity=restaurant](area);""")
        return response