from flask import Flask, render_template, request, redirect, url_for, session
from game.game_controller import GameController
from leaderboard.leaderboard import Leaderboard

app = Flask(__name__)
app.secret_key = "secret123"

game = None

def get_game():
    global game
    if game is None:
        game = GameController()
    return game

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    username = request.form["username"]
    session["user"] = username
    get_game().load_user(username)
    return redirect(url_for("play"))


@app.route("/play")
def play():
    raw_data = get_game().get_level_and_theme_data()

    # convert int keys → string keys
    data = {str(k): v for k, v in raw_data.items()}

    return render_template("play.html", data=data)


@app.route("/questions", methods=["POST"])
def questions():
    level = int(request.form["level"])
    theme = request.form["theme"]
    get_game().prepare_round(level, theme)
    questions = get_game().get_questions()
    return render_template("questions.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    answers = request.form.to_dict()
    story, score = get_game().finish_round(answers)
    return render_template("result.html", story=story, score=score)

@app.route("/leaderboard")
def leaderboard():
    data = Leaderboard.get_top()
    return render_template("leaderboard.html", data=data)

@app.route("/progress")
def progress():
    data = get_game().get_progress()
    return render_template("progress.html", data=data)

# if __name__ == "__main__":
    # app.run(debug=True)
