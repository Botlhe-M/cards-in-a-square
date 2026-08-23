from app.config import DevelopmentConfig, TestingConfig ,ProductionConfig
from app.utils.logging_config import configure_logging
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    from app.routes import main
    app.register_blueprint(main)

    # Use DevelopmentConfig for local development
    app.config.from_object(DevelopmentConfig)

    # Configure logging for the application
    configure_logging(app)

    app.logger.info("Flask application created and configured.")
    app.logger.info("Registered blueprints: main.")
    return app
