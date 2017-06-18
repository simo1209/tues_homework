import uuid

from flask import (
    Flask, render_template, request, redirect, url_for
)

from todo import *


app = Flask(__name__)

tasks = []


@app.route('/')
def todos():
    result_tasks = tasks
    status = request.args.get('status')
    if status == 'completed':
        result_tasks = get_completed(result_tasks)
    elif status == 'uncompleted':
        result_tasks = get_uncompleted(result_tasks)
    tag = request.args.get('tag')
    if tag:
        result_tasks = filter_by_tag(result_tasks, tag)
    order = request.args.get('order')
    if order == 'priority':
        result_tasks = order_by_priority(result_tasks)
    elif order == 'deadline':
        result_tasks = order_by_deadline(result_tasks)

    query = {}
    for k in ('status', 'tag', 'order'):
        if locals()[k] is not None:
            query[k] = locals()[k]

    return render_template(
        'index.html',
        tasks=result_tasks,
        tags=TAGS,
        priorities=PRIORITIES.keys(),
        query=query
    )


@app.route('/tasks/create', methods=['POST'])
def create():
    add_task(
        tasks,
        uuid.uuid4().hex,
        request.form['title'],
        request.form['deadline'],
        request.form['priority'],
        request.form.getlist('tags')
    )
    return redirect(url_for('todos'))


@app.route('/tasks/clear', methods=['POST'])
def clear():
    clear_completed(tasks)
    return redirect(url_for('todos'))


@app.route('/tasks/<id>/remove', methods=['POST'])
def remove(id):
    remove_task(tasks, id)
    return redirect(url_for('todos'))


@app.route('/tasks/<id>/complete', methods=['POST'])
def complete(id):
    complete_task(tasks, id)
    return 'ok'


@app.route('/tasks/<id>/uncomplete', methods=['POST'])
def uncomplete(id):
    uncomplete_task(tasks, id)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
