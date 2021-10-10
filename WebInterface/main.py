from flask import render_template
from WebInterface.ColorTheme import ColorTheme
from flask import Flask, request, redirect, url_for
import json

from flask import Request
from pysondb import db

Theme = ColorTheme.from_json("Themes/default-theme.json")
template_folder = r"templates/"
app = Flask(__name__, template_folder=template_folder)

DB = db.getDb("worlds.json")


@app.route("/")
def index():
    worlds = [item['name'] for item in DB.getAll()]
    return render_template("index.html", Theme=Theme, worlds=worlds)


@app.route("/<world>/dashboard")
def dashboard(world):
    worlds = DB.getAll()
    names = [item["name"] for item in worlds]
    if world not in names:
        DB.deleteAll()
        worlds.append({'name': world, 'timeline': {'len': 0, 'events': []}})
        DB.addMany(worlds)
    with open("Parts/dashboard-parts.json", "r") as file:
        parts = json.load(file)
    return render_template("Dashboard/dashboard.html", Theme=Theme, parts=parts)


@app.route("/<world>/dashboard/history")
def history(world):
    with open("Parts/history-parts.json", "r") as file:
        parts = json.load(file)

    return render_template("Dashboard/dashboard.html", Theme=Theme, parts=parts)


@app.route("/<world>/dashboard/history/timeline")
def timeline(world):
    if request.method == "GET" or request.method == "get":
        if len(request.args.to_dict()) > 0:
            return redirect(f"/{world}/dashboard/history/timeline")
    tl = DB.getByQuery({"name": world})
    tl = tl[0]["timeline"]
    return render_template("Dashboard/History/timeline.html", Theme=Theme, timeline=tl)


@app.route("/<world>/dashboard/history/timeline/add-event", methods=["POST"])
def add_event(world):
    d = request.json
    tl = DB.getByQuery({"name": world})
    l = tl[0]["timeline"]["len"] + 1
    tl = tl[0]["timeline"]["events"]
    tl.append(d)
    DB.updateByQuery({"name": world}, {"timeline": {"len": l, "events": tl}})
    print(DB.getAll())
    return request.json


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
