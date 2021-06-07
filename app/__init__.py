from flask import Flask
from config import DevConfig, Config_options
from flask_bootstrap import Bootstrap

#initializing application
app = Flask(__name__,instance_relative_config = True)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # create the app configurations
    app.config.from_object(Config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    #  Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app
