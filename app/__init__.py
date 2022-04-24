from app.routes import home, dashboard

# set entry point of our app to /app so Flask knows where to start server
# __init__.py is the python equivalent of index.js
from flask import Flask;

# def to create a function
def create_app(test_config=None):
    # app config info
    # app serves static resources from root directory '/'
    app = Flask(__name__, static_url_path='/')
    # trailing slashes are optional (allow /home = /home/)
    app.url_map.strict_slashes = False
    # what key to use when creating server-side sessions
    app.config.from_mapping(
        SECRET_KEY='SECRET'
    )

    # this turns the following function into a route
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # python equivalent of app.use(routes)
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app
