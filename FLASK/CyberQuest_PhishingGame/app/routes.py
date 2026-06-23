from flask import render_template, redirect, url_for, request, session
from app import app
from app.scenarios import SCENARIOS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start")
def start_game():
    session["score"] = 0
    session["answers"] = []

    return redirect(url_for("show_scenario", scenario_id=1))


@app.route("/scenario/<int:scenario_id>", methods=["GET", "POST"])
def show_scenario(scenario_id):
    scenario = next(
        (item for item in SCENARIOS if item["id"] == scenario_id),
        None
    )

    if scenario is None:
        return redirect(url_for("result"))

    if request.method == "POST":
        choice_index = int(request.form["choice_index"])
        selected_choice = scenario["choices"][choice_index]

        session["score"] = session.get("score", 0) + selected_choice["score"]

        answers = session.get("answers", [])
        answers.append({
            "scenario_title": scenario["title"],
            "topic": scenario["topic"],
            "choice": selected_choice["text"],
            "score": selected_choice["score"],
            "feedback": selected_choice["feedback"],
        })
        session["answers"] = answers

        next_scenario_id = scenario_id + 1

        if next_scenario_id > len(SCENARIOS):
            return redirect(url_for("result"))

        return redirect(url_for("show_scenario", scenario_id=next_scenario_id))

    return render_template(
        "scenario.html",
        scenario=scenario,
        total_scenarios=len(SCENARIOS),
    )


@app.route("/result")
def result():
    score = session.get("score", 0)
    answers = session.get("answers", [])
    max_score = len(SCENARIOS) * 2

    if score >= 8:
        rating = "Cyber Guardian"
        advice = "You made strong cyber safety decisions. Keep checking suspicious messages, protecting your accounts, and thinking carefully about your digital footprint."
    elif score >= 5:
        rating = "Cyber Apprentice"
        advice = "You made some safe choices, but there are areas to improve. Focus on checking links, protecting MFA codes, and limiting unnecessary data sharing."
    else:
        rating = "Needs More Training"
        advice = "You may need more practice identifying cyber risks. Remember to slow down, check before clicking, and ask for help when something seems suspicious."

    return render_template(
        "result.html",
        score=score,
        max_score=max_score,
        rating=rating,
        advice=advice,
        answers=answers,
    )