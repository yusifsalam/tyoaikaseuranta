from application import app, db
from flask import render_template, request, redirect, url_for
from application.projects.models import Project

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all())

@app.route("/projects/new")
def projects_form():
    return render_template("projects/new.html")

@app.route("/projects/", methods=["POST"])
def projects_create():
    new_project = Project(request.form.get("name"))
    db.session().add(new_project)
    db.session().commit()
    return redirect(url_for("projects_index"))    