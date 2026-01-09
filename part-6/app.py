from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - in-memory task list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High', 'due_date': '2026-01-10'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium', 'due_date': '2026-01-12'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low', 'due_date': '2026-01-15'}
]

# Home page - display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS, search_query='')

# Search task
@app.route('/search')
def search():
    query = request.args.get('search', '').lower()  # match input name="search"
    results = [task for task in TASKS if query in task['title'].lower()]
    return render_template('index.html', tasks=results, search_query=query)

# Edit task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next(t for t in TASKS if t['id'] == id)

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        task['due_date'] = request.form['due_date']
        return redirect(url_for('index'))

    return render_template('edit.html', task=task)

# Add new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_id = max([task['id'] for task in TASKS], default=0) + 1
        TASKS.append({
            'id': new_id,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority'],
            'due_date': request.form['due_date']
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
