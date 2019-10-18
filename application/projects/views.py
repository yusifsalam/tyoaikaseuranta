from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application.projects.models import Project
from application.leads.models import Lead
from application.auth.models import User
from application.projects.forms import ProjectForm


@app.route("/projects", methods=['GET', 'POST'])
def projects_index():
    if request.method == 'POST':
        value = request.form.getlist('ownCheckbox')
        if value:
            return render_template("projects/list.html", projects=current_user.projects)
    return render_template("projects/list.html", projects=Project.query.all())


@app.route("/projects/<int:project_id>", methods=['GET'])
@login_required
def project_view_one(project_id):
    project = Project.query.get(project_id)
    leads = [lead.user_id for lead in project.leads]
    print(leads)
    return render_template("projects/single.html", project=project, leads=leads)


@app.route("/projects/<int:project_id>/users", methods=['GET'])
@login_required
def project_user_list(project_id):
    project = Project.query.get(project_id)
    users = project.accounts
    leads = [lead.user_id for lead in project.leads]
    return render_template("projects/user_list.html", project=project, users=users, leads=leads)


@app.route("/projects/<int:project_id>/add_user", methods=['GET'])
@login_required
def project_add_user(project_id):
    project = Project.query.get(project_id)
    project_users = project.accounts
    project_user_ids = [user.id for user in project_users]
    users = User.query.filter(User.id.notin_(project_user_ids)).all()
    leads = [lead.user_id for lead in project.leads]
    return render_template('/projects/add_user.html'.format(project_id), project=project, users=users, leads=leads)


@app.route("/projects/<int:project_id>/add_user/<int:user_id>", methods=['POST'])
@login_required
def project_add_user_by_id(project_id, user_id):
    project = Project.query.get(project_id)
    user = User.query.get(user_id)
    project.accounts.append(user)
    db.session().commit()
    return redirect(url_for('project_add_user', project_id=project_id))


@app.route("/projects/<int:project_id>/make_lead/<int:user_id>", methods=['POST'])
@login_required
def project_make_lead(project_id, user_id):
    project = Project.query.get(project_id)
    user = User.query.get(user_id)
    leads = [lead.user_id for lead in project.leads]
    if user.id not in leads:
        lead = Lead(project.id, user.id)
        db.session().add(lead)
        db.session().commit()
    return redirect(url_for('project_user_list', project_id=project_id))


@app.route("/projects/<int:project_id>/remove_lead/<int:user_id>", methods=['POST'])
@login_required
def project_remove_lead(project_id, user_id):
    lead_id = Lead.findByProjectAndUser(project_id, user_id)
    if lead_id:
        lead = Lead.query.get(lead_id)
        db.session().delete(lead)
        db.session().commit()

    return redirect(url_for('project_user_list', project_id=project_id))


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
    new_lead = Lead(new_project.id, current_user.id)
    new_project.leads.append(new_lead)
    new_project.account_id = current_user.id
    current_user.projects.append(new_project)
    db.session().add(new_project)
    db.session().add(current_user)
    db.session().add(new_lead)
    db.session().commit()
    return redirect(url_for("projects_index"))


@app.route('/projects/<project_id>/modify', methods=['POST'])
@login_required
def project_modify(project_id):
    project = Project.query.get(project_id)
    project.completed = not project.completed
    db.session.commit()
    return redirect(url_for('project_view_one', project_id=project_id))


@app.route('/projects/<project_id>/remove', methods=['POST'])
@login_required
def projects_delete(project_id):
    project = Project.query.get(project_id)
    for lead in project.leads:
        db.session.delete(lead)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('projects_index'))

