from flask import Flask, jsonify, render_template, redirect, request, url_for
import config
from utils import StartupProfit

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("Welcome to Startup Profit Prediction")
    return render_template("home.html")

@app.route("/Profit", methods = ["GET","POST"])
def prediction():
    if request.method == "POST":
        data = request.form

        print("Data :", data)

        profit_ins = StartupProfit(data)
        profit = profit_ins.get_predicted_profit()

        print("Profit :",profit)

        # return jsonify({"Profit :": f"{profit} $"})
        return render_template("home.html", prediction_text = profit)

if __name__ =="__main__":
    app.run(debug=True)