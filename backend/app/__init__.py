from flask import Flask
from flask_cors import CORS

from .api.admin import admin_bp
from .api.auth import auth_bp
from .api.courses import courses_bp
from .api.health import health_bp
from .api.ide import ide_bp
from .api.progress import progress_bp
from .config import Config
from .extensions import init_mongo, jwt


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=app.config["CORS_ORIGINS"])
    jwt.init_app(app)
    init_mongo(app.config["MONGO_URI"])

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(courses_bp, url_prefix="/api")
    app.register_blueprint(progress_bp, url_prefix="/api")
    app.register_blueprint(ide_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api")

    return app
