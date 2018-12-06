"""Initializes app."""

from flask import Flask

from instance.config import config

from manage import init_db


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

    return app
