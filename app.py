from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "527dc3a20df6eba1582053de6a2e3ccf" # Replace with your API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url).json()
            if response.get("main"):
                weather_data = {
                    "city": city,
                    "temperature": response["main"]["temp"],
                    "description": response["weather"][0]["description"].title(),
                    "icon": response["weather"][0]["icon"]
                }
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
