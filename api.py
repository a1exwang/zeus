import thunder
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/tasks", methods=["POST"])
def tasks():
	url = request.json['url']
	data = {"status": "ok", "return": thunder.call_thunder_bt_default(url)}
	return jsonify(data)


app.run(host="0.0.0.0", port=8000)