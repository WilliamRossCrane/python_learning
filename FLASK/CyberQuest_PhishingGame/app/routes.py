from flask import render_template, redirect, url_for
from app import app
from app.scenarios import SCENARIOS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start_game():
    return redirect(url_for("show_scenario", scenario_id=1))


@app.route("/scenario/<int:scenario_id>")
def show_scenario(scenario_id):
    scenario = next(
        (item for item in SCENARIOS if item["id"] == scenario_id),
        None
    )

    if scenario is None:
        return redirect(url_for("result"))

    return render_template(
        "scenario.html",
        scenario=scenario,
        total_scenarios=len(SCENARIOS),
    )


@app.route("/result")
def result():
    return render_template("result.html")