from app.models import Post
from app.db import get_db
# Here we import the functions Blueprint() and render_template() from the Flask module
from flask import Blueprint, render_template
# this preceding code lets us consolidate routes onto a single bp object that the parent app can register later.
# this corresponds to using the `Router` middleware of express.js
bp = Blueprint('home', __name__, url_prefix='/')
# here we define 2 functions index() and login() it is important to note that whatever the function returns is what becomes the response
# the `@bp.route()` decorator is added before the function to turn it into a route
@bp.route('/')
def index():
    # get all posts // The get_db() function returns a session connection that's tied to this route's context. We then use the query() method on the 
    # connection object to query the Post model for all posts in descending order, and we save the results in the posts variable.
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()
    # render_template() function responds with a template instead of a string
    return render_template(
        'homepage.html',
        posts=posts
        )

@bp.route('/login')
def login():
    return render_template('login.html')

# this route uses a parameter, <id> resprents the parameter. To capture the value, we include it as a function parameter which is `single(id)`
@bp.route('/post/<id>')
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        'single-post.html',
        post=post
    )