"""Initializes app."""

from flask import Flask

from instance.config import config

from manage import init_db

from app.api_2_0 import VERSION_TWO as v_2

from app.api_2_0.error_handlers import ERROR_HANDLERS


def create_app(configuration):
    """Set up app.
    args:
        configuration(str): name of configuration to use for current instace
    returns:
        app(object): app instance
    """
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False

    # configure app
    app.config.from_object(config[configuration])
    db_config = config[configuration].db
    init_db(db_config)

    # register blueprints
    app.register_blueprint(v_2)
    app.register_blueprint(ERROR_HANDLERS)

    return app
