from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.secret_key='somerandomvalue'
    UPLOAD_FOLDER = 'website\static\img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///website.sqlite'
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view='user.login'
    login_manager.init_app(app)
    from .models import user  
    @login_manager.user_loader
    def load_user(user_id):
        return user.query.get(int(user_id))
    #blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import users
    app.register_blueprint(users.bp)
    return app
