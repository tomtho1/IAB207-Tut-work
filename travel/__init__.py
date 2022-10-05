from distutils.log import Log
from ensurepip import bootstrap
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)
UPLOAD_FOLDER = '/static/image'

def create_app(): #pythonic way of writing function names usually has _ for spaces
    bootstrap = Bootstrap5(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_db.sqlite'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.debug=True
    app.secret_key = 'jivwnopeutnowevrnu'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #add blueprints
    from . import views #import contents of views.py #creates circular reference as views and init are at the same heirachy 
    app.register_blueprint(views.mainbp)
    
    from . import destinations
    app.register_blueprint(destinations.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
        return render_template("404.html")


    return app
