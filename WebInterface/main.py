from flask import render_template
from WebInterface.ColorTheme import ColorTheme
from flask import Flask, request,redirect,url_for
import json
from modules.timeline import timeline as tl
from modules.timeline import event as eve
from flask import Request

TIME_LINE = tl.Timeline()
TIME_LINE.add_event(eve.Event("Genesis", "Creation Of the World!", 0))
TIME_LINE.add_event(eve.Event("Genesis", "Creation Of the World!", -1))
TIME_LINE.add_event(eve.Event("Genesis", "Creation Of the World!", 1))
template_folder = r"templates/"
Theme = ColorTheme.from_json("Themes/default-theme.json")

app = Flask(__name__, template_folder=template_folder)


@app.route("/")
def index():
    return render_template("index.html", Theme=Theme)


@app.route("/dashboard")
def dashboard():

    with open("Parts/dashboard-parts.json", "r") as file:
        parts = json.load(file)

    return render_template("Dashboard/dashboard.html", Theme=Theme, parts=parts)


@app.route("/dashboard/history")
def history():

    with open("Parts/history-parts.json", "r") as file:
        parts = json.load(file)

    return render_template("Dashboard/dashboard.html", Theme=Theme, parts=parts)


@app.route("/dashboard/history/timeline")
def timeline():
    global TIME_LINE
    if request.method=="GET" or request.method=="get" :
        if len(request.args.to_dict()) >0:
            return redirect("/dashboard/history/timeline")
    return render_template("Dashboard/History/timeline.html", Theme=Theme, timeline=TIME_LINE)


@app.route("/add-event", methods=["POST"])
def add_event():
    global TIME_LINE
    d = request.json
    TIME_LINE.add_event(eve.Event(d["name"], d["description"], int(d["year"])))
    return request.json


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
