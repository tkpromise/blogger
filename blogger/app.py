from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)    

    from blogger.page.views import page
    from blogger.user.views import user_page
    app.register_blueprint(page)
    app.register_blueprint(user_page)

    return app

