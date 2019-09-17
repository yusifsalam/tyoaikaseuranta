from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.projects.models import Project
from application.projects.forms import ProjectForm


@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template("projects/list.html", projects=Project.query.all())


@app.route("/projects/new")
@login_required
def projects_form():
    return render_template("projects/new.html", form=ProjectForm())


@app.route("/projects/", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)
    if not form.validate():
        return render_template("projects/new.html", form=form)
    new_project = Project(form.name.data)
    new_project.account_id = current_user.id

    db.session().add(new_project)
    db.session().commit()
    return redirect(url_for("projects_index"))
