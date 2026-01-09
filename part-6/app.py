from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - in-memory task list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# Home page - display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)

# Add new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_id = max([task['id'] for task in TASKS], default=0) + 1

        TASKS.append({
            'id': new_id,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority']
        })
        return redirect(url_for('index'))

    return render_template('add.html')

# View single task
@app.route('/task/<int:id>')
def task_detail(id):
    task = next((task for task in TASKS if task['id'] == id), None)
    return render_template('task.html', task=task)

# Delete task
@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    TASKS = [task for task in TASKS if task['id'] != id]
    return redirect(url_for('index'))

# About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
