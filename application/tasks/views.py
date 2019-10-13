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
