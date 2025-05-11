from flask import Flask

from src.extensions.app_config import initialize_app
from src.extensions.extensions import db, cors, mail

import json
import os

from src.routes.mail_routes import mail_blueprint

import logging

from src.routes.access_log_routes import access_log_blueprint

if __name__ == '__main__':
    initialize_app()

    logger = logging.getLogger(__name__)
    logger.info("initializing app instance")

    app = Flask(__name__)
    app.config.from_file("extensions//configs.json", load=json.load)
    app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')

    db.init_app(app)
    cors.init_app(app)
    mail.init_app(app)

    logging.info("registering blueprints")

    app.register_blueprint(mail_blueprint)
    app.register_blueprint(access_log_blueprint)

    with app.app_context():
        logging.info("initializing database instance")
        db.create_all()

    logging.info("finished initializing app instance")
    logging.info("starting the app")
    app.run(debug=True, port=9999)
