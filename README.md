Alayacare Python skill test
===========================

#### Essa é uma aplicação de teste de backend utilizando Flask, apenas adaptei para Django
#### <a href='https://github.com/AlayaCare/backend-python-test/tree/master'>Projeto original</a>

### Application
The TODO App allows a user to add reminders of thing he needs to do. Here are the requirement for the app.
* Users can add, delete and see their todos.
* All the todos are private, users can't see other user's todos.
* Users must be logged in order to add/delete/see their todos.

### Requirements
* python 5.7
* virtualenv
* sqlite3
* A github account

### Installation
**/!\ You need to fork this repository. See [How to submit your work?](#how-to-submit-your-work)**
```sh
virtualenv .
bin/pip install -r requirements.txt
bin/python main.py initdb
bin/python main.py
```

### Instructions

You will be asked to improve the code of this app with the following tasks.

You can complete the tasks in any order.

Separate your commits by task and use the following format for your commit messages: TASK-{task number}: {meaningful message}

### Tasks
* TASK 1: As a user I can't add a todo without a description.
* TASK 2: As a user I can mark a todo as completed.
    - Write a database migration script in `resources/`
* TASK 3: As a user I can view a todo in a JSON format.
    - Ex: /todo/{id}/json => {id: 1, user_id: 1, description: "Lorem Ipsum"}
* TASK 4: As a user I can see a confirmation message when I add/delete a todo.
* TASK 5: As a user I can see my list of todos paginated.
* TASK 6: Implement an ORM database access layer so we don’t have SQL in the controller code.

Extra tasks:
- Fix any bug you may find.
- Fix any security issue you may find.


And you're done!


More documentation on Github:
* https://help.github.com/articles/fork-a-repo/
* https://help.github.com/articles/using-pull-requests/