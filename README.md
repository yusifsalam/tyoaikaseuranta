# Projektin työaikaseuranta (Project hours follow-up tool)

The goal of this project is to create a Flask web application that allows for tracking of project hours and tasks. Users within the projects have different roles: project lead (or instructor) can see the summaries from all users within a project on weekly, user or task-related basis. Project users record their hours, what type of work was done (from predefined categories) and a short description of what was done. Project users can see their own hours and summaries, but not other users' hours or summaries. 
The emphasis of this project is on the functionality of the database(s). 

Features to be implemented:

* Logging in
* Logging hours
* Creating a new project
* Adding a user to a project
* Removing a user from a project
* Summaries (reports)

## Instructions for users
You can read the user manual [here](https://github.com/yusifsalam/tyoaikaseuranta/blob/master/documentation/manual.md).


## Deployment
The project is being continuosly deployed to Heroku via the Heroku GitHub integration. 

Heroku [link](https://shrouded-hamlet-09298.herokuapp.com/). 

You need to register to use the application! Alternatively, you can build your own instance from source. 

## Hosting your own app
You will need to have these on your system:
* Python 3
* PostgreSQL

Follow these steps:
1. Clone the repo
2. cd into the cloned repository directory
3. create a new python virtual environment 
```python
python3 -m venv venv
```
4. activate the newly created virtual environment `source venv/bin/activate` (use an appropriate command if you're using ZSH or Fish shell)
5. install the requirements
```python
pip install -r requirements.txt
```
6. start the application, it will run on port 5000
```python
python run.py
```

## DB Diagram 
![diagram](https://raw.githubusercontent.com/yusifsalam/tyoaikaseuranta/master/documentation/db_diagram.png)
