# Here we import the functions Blueprint() and render_template() from the Flask module
from flask import Blueprint, render_template
# this preceding code lets us consolidate routes onto a single bp object that the parent app can register later.
# this corresponds to using the `Router` middleware of express.js
bp = Blueprint('home', __name__, url_prefix='/')
# here we define 2 functions index() and login() it is important to note that whatever the function returns is what becomes the response
# the `@bp.route()` decorator is added before the function to turn it into a route
@bp.route('/')
def index():
    # render_template() function responsds with a template instead of a string
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')
# this route uses a parameter, <id> resprents the parameter. To capture the value, we include it as a function parameter which is `single(id)`
@bp.route('/post/<id>')
def single(id):
    return render_template('single-post.html')