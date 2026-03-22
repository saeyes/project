# app.py

from flask import Flask, render_template, request
import random

from matchmaking import Player, matchmaking
from model import predict_win
from translations import translations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    lang = request.args.get("lang", "ko")
    text = translations.get(lang, translations["ko"])

    result = None

    if request.method == "POST":
        players = [Player(f"P{i}", random.randint(1500, 2500)) for i in range(10)]
        matches = matchmaking(players)

        teams = []
        for p1, p2 in matches:
            win_prob = predict_win(p1.mmr, p2.mmr)

            teams.append({
                "p1": p1.name,
                "p2": p2.name,
                "mmr1": p1.mmr,
                "mmr2": p2.mmr,
                "win_prob": round(win_prob, 2)
            })

        result = teams

    return render_template("index.html", result=result, t=text, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)