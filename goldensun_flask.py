"""Golden Sun App which runs in a webapp, based off Flask"""

from flask import Flask, render_template
import goldensun as gs

app = Flask(__name__)


@app.route("/")
def show_homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
