from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.projects.models import Project
from application.projects.forms import ProjectForm


@app.route("/projects", methods=['GET', 'POST'])
def projects_index():
    if request.method == 'POST':
        value = request.form.getlist('ownCheckbox')
        if value:
            return render_template("projects/list.html", projects=current_user.projects)
        else:
            return render_template("projects/list.html", projects=Project.query.all())
    else:
        return render_template("projects/list.html", projects=Project.query.all())


@app.route("/projects/<int:project_id>", methods=['GET'])
@login_required
def project_view_one(project_id):
    project = Project.query.get(project_id)
    return render_template("projects/single.html", project=project)


@app.route("/projects/<int:project_id>/users", methods=['GET', 'POST'])
@login_required
def project_user_list(project_id):
    project = Project.query.get(project_id)
    users = project.accounts
    print(users)
    return render_template("projects/user_list.html", project=project, users=users)


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
    current_user.projects.append(new_project)
    db.session().add(new_project)
    db.session().add(current_user)
    db.session().commit()
    return redirect(url_for("projects_index"))


@app.route('/projects/<project_id>/modify', methods=['POST'])
@login_required
def project_modify(project_id):
    project = Project.query.get(project_id)
    project.completed = True
    db.session.commit()
    return redirect(url_for('projects_index'))


@app.route('/projects/<project_id>/remove', methods=['POST'])
@login_required
def projects_delete(project_id):
    project = Project.query.get(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('projects_index'))

