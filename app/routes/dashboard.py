from flask import Blueprint, render_template

# This time, using the url_prefix argument, we prefix every route in the blueprint with /dashboard.
# The routes then become /dashboard and /dashboard/edit/<id> when registered with the app.
# Like home.py, this dashboard.py file is a module. Every variable or function belongs to the module and can be imported elsewhere.

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')