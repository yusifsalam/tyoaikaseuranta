from application import db, app
from flask import render_template, redirect, request, url_for
from flask_login import login_required, current_user
from application.tasks.forms import TaskForm
from application.tasks.models import Task
from application.projects.models import Project
from application.auth.models import User


@app.route('/projects/<int:project_id>/tasks')
@login_required
def tasks_index(project_id):
    project = Project.query.get(project_id)
    tasks = project.tasks
    return render_template('tasks/task_list.html', tasks=tasks)


@app.route('/projects/<int:project_id>/tasks/new')
@login_required
def tasks_form(project_id):
    return render_template('tasks/new_task.html', form=TaskForm(), project_id=project_id)


@app.route('/projects/<int:project_id>/new_task', methods=['POST'])
@login_required
def tasks_create(project_id):
    project = Project.query.get(project_id)
    form = TaskForm(request.form)
    if not form.validate():
        return render_template('tasks/new_task.html', form=form, project_id=project_id)
    new_task = Task(form.category.data, form.hours.data, form.description.data)
    new_task.project_id = project.id
    new_task.account_id = current_user.id
    current_user.tasks.append(new_task)
    project.tasks.append(new_task)
    db.session().add(new_task)
    db.session().add(current_user)
    db.session().add(project)
    db.session().commit()
    return redirect(url_for('tasks_index', project_id=project_id))
