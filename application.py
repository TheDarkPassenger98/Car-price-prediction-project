from flask import Flask, render_template
import os
import pandas as pd
print("Current working dir:", os.getcwd())
print("Templates path exists:", os.path.exists("templates/index.html"))
app = Flask(__name__, template_folder="static/templates")
car = pd.read_csv("Cleaned Car data.csv")

@app.route("/")
def home():
    companies = sorted(car["company"].unique())
    car_models = sorted(car["name"].unique())
    year = sorted(car["year"].unique(), reverse= True)
    fuel_type = car["fuel_type"].unique()
    return render_template("index.html", companies = companies, years = year, car_models = car_models,
                           fuel_type = fuel_type)
    
if __name__ == "__main__":
    app.run(debug = True)
