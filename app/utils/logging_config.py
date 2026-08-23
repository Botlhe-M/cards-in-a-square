"""
Application logging configuration.

This module controls how logs are handled throughout
the Hidden Leaf Mission Archive application.

Logging destinations:
1. Console
   - Useful during development.
   - Visible when running Flask locally or Docker.

2. File
   - Keeps a history of application events.
   - Useful when debugging deployed challenges.
"""

import logging
import os

from logging.handlers import RotatingFileHandler


def configure_logging(app):
    """
    Configure application-wide logging.

    This function is called once when the Flask
    application starts.

    Args:
        app:
            Flask application instance.
    """

    # Create logs directory if it does not exist.
    #
    # Keeping logs outside the source code makes it
    # easier to ignore them in version control.
    log_directory = os.path.join(
        app.root_path,
        "..",
        "logs"
    )

    os.makedirs(
        log_directory,
        exist_ok=True
    )


    log_file = os.path.join(
        log_directory,
        "cards-in-a-square.log"
    )


    # Standard format used by all application logs.
    #
    # Example:
    #
    # 2026-08-04 14:00:00 INFO Hidden Leaf application started
    #
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


    # File handler.
    #
    # Rotating files prevents logs from growing forever.
    #
    # maxBytes:
    #   Maximum size before creating a new file.
    #
    # backupCount:
    #   Number of old logs to keep.
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10240,
        backupCount=5
    )

    file_handler.setFormatter(
        formatter
    )


    # Console handler.
    #
    # Shows logs while developing.
    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )


    # Configure Flask's default logger.
    app.logger.setLevel(
        logging.INFO
    )


    app.logger.addHandler(
        file_handler
    )

    app.logger.addHandler(
        console_handler
    )


    app.logger.info(
        "Hidden Leaf Mission Archive logging initialized."
    )