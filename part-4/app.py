from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# ---------------- HOME (ORIGINAL + SEARCH) ----------------
@app.route('/', methods=['GET', 'POST'])
def home():
    # Original home data
    category_name = 'electronics'
    product_id = 1
    product = {'name': 'Mobile Phone', 'price': 15000}

    search_query = None

    # Handle search
    if request.method == 'POST':
        search_query = request.form.get('query')

    return render_template(
        'index.html',
        show_category_product=True,
        category_name=category_name,
        product_id=product_id,
        product=product,
        search_query=search_query
    )

# ---------------- ABOUT ----------------
@app.route('/about/')
def about():
    return render_template('about.html')

# ---------------- USER PROFILE ----------------
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

# ---------------- POST ----------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post_id=post_id, post=post)

# ---------------- USER POST ----------------
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)

# ---------------- LINKS (url_for demo) ----------------
@app.route('/links')
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
        'product_1': url_for('category_product', category_name='electronics', product_id=1),
    }
    return render_template('links.html', links=links)

# ---------------- PRODUCT PAGES ----------------
@app.route('/product')
def product_default():
    product = {'name': 'Laptop', 'price': 55000}
    product_id = 1
    return render_template('product.html', product=product, product_id=product_id)

@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 55000},
        2: {'name': 'Mobile', 'price': 20000},
        3: {'name': 'Headphones', 'price': 2500},
    }
    product = products.get(product_id)
    return render_template('product.html', product=product, product_id=product_id)

@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    products = {
        'electronics': {
            1: {'name': 'Laptop', 'price': 55000},
            2: {'name': 'Mobile', 'price': 20000},
        },
        'accessories': {
            3: {'name': 'Headphones', 'price': 2500},
        }
    }

    category = products.get(category_name.lower())
    product = None

    if category:
        product = category.get(product_id)

    return render_template(
        'index.html',
        category_name=category_name,
        product_id=product_id,
        product=product,
        show_category_product=True
    )


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
