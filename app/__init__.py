from flask import Flask
from flask_session import Session

from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__, template_folder='blueprints/templates')
    app.config.from_object(DevelopmentConfig())

    from .extensions import db
    #db.init_app(app)

    from .blueprints import all_blueprints
    for blueprint, prefix in all_blueprints: #register all blueprints
        app.register_blueprint(blueprint=blueprint, url_prefix=prefix )

    return app