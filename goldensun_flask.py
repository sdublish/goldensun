"""Golden Sun App which runs in a webapp, based off Flask"""

from flask import Flask, render_template, request
import goldensun as gs

app = Flask(__name__)

djinn_dict = gs.create_djinn_dict("djinn.txt")
char_dict = gs.create_char_dict("characters.txt")


@app.route("/")
def show_homepage():
    return render_template("homepage.html")


@app.route("/results", methods=["POST"])
def show_results():
    char = request.form.get("character")
    character = char_dict[char]
    return render_template("results.html", character=character)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
