# here we import `home` directly from the newly created `routes` package
# .routes indicates that `routes` belongs to the parent `app` package
from .routes import home, dashboard
# Here we use a from...import statement to import the Flask() function
from flask import Flask

# Then we use the `def` keyword to define a `create_app()` function
def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )
    # here we have an inner function that returns a string
    # However, in the preceding line, the decorator `@app.route('/hello`) turns the
    # hello() function into a route. The functions return statement then becomes the routes response
    @app.route('/hello')
    def hello():
        return 'hello world'

    # register our routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app