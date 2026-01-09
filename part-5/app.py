"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Sneha Chaudhari',
    'title': 'Web Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'snehachaudhari556@gmail.com',
    'github': 'https://github.com/snehachaudhari556-dot',
    'linkedin': 'https://linkedin.com/in/sneha-chaudhari-642b4034a/',
}

SKILLS = [
    {'name': 'Python', 'level': 60},
    {'name': 'HTML-CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'Javascript', 'level': 70},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {
        'id': 3,
        'name': 'Student Management System',
        'description': 'A system to manage student records, courses, and performance.',
        'tech': ['Python', 'HTML-CSS', 'SQL'],
        'status': 'Completed'
    }
]



# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO, skills=SKILLS)



@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

# ===================== Blog Data =====================
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Learning Flask Basics',
        'summary': 'A quick guide to starting with Flask for web development.',
        'content': 'Flask is a lightweight web framework in Python. It allows you to build web apps easily...',
        'date': '2026-01-08'
    },
    {
        'id': 2,
        'title': 'Building a Personal Website',
        'summary': 'Steps to create your own portfolio website using Flask.',
        'content': 'In this post, we will create a personal website with multiple pages...',
        'date': '2026-01-07'
    },
    {
        'id': 3,
        'title': 'Understanding Jinja2 Templates',
        'summary': 'How to use Jinja2 for dynamic HTML rendering.',
        'content': 'Jinja2 allows you to insert Python variables, loops, and conditionals directly into HTML...',
        'date': '2026-01-06'
    },
]

# ===================== Routes =====================
@app.route('/blog')
def blog():
    return render_template('blog.html', info=PERSONAL_INFO, posts=BLOG_POSTS)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = None
    for p in BLOG_POSTS:
        if p['id'] == post_id:
            post = p
            break
    return render_template('blog_post.html', info=PERSONAL_INFO, post=post)

@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    # Filter projects that use the given skill (case-insensitive)
    filtered_projects = [p for p in PROJECTS if skill_name.lower() in [t.lower() for t in p['tech']]]
    
    return render_template(
        'skill_projects.html',
        info=PERSONAL_INFO,
        skill=skill_name.capitalize(),
        projects=filtered_projects
    )



if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
