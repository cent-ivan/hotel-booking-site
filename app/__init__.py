from flask import Flask


def create_app():
    from .configs.flask_configs import DevelopmentConfig, ProductionConfig
    from .configs.login_manager_config import LoginManagerConfig

    app = Flask(__name__, template_folder='blueprints/templates')
    app.config.from_object(ProductionConfig())


    from .blueprints.models import all_models
    from .extensions import db, Session, login_manager
    db.init_app(app)
    Session(app)

    login_manager.init_app(app)
    LoginManagerConfig.configure_login(login_manager)
    

    from .blueprints import all_blueprints
    for blueprint, prefix in all_blueprints: #register all blueprints
        app.register_blueprint(blueprint=blueprint, url_prefix=prefix )

    return app