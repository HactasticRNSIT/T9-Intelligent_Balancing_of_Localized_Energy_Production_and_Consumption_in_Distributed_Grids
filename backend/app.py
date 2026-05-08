from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    prediction = model.predict([[
        data["time"],
        data["solar_output"],
        data["battery_level"],
        data["temperature"]
    ]])

    return jsonify({
        "predicted_demand": prediction[0]
    })

app.run(debug=True)