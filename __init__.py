from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


#define a new databse:
db = SQLAlchemy()
#database name:
DB_NAME = "database.db"

def create_app():
    #initialize the app
    app = Flask(__name__)
    
    #encrypt/secure cookies of our session data related to website
    app.config['SECRET_KEY'] = 'Alohilani'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
   
    #initialize database:
    with app.app_context():
        db.init_app(app)

    #registering blueprints to flask. importing these files
    from .views import views
    from .auth import auth

    #register:
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    #check if database was already created:
    from .models import User, Note

    create_database(app) #actually calling the create_database

    #login_manager = LoginManager()
    #where do we need to go if we're not logged in?
    #flask will redirect to 'auth.login' where login is required.
    #login_manager.login_view = 'auth.login'
    #tell login manager what app we are using
    #login_manager.init(app)

    #@login_manager.user_loader
    #def load_user(id):
        #return User.query.get(int(id))
    
    # HERE
    login_manager = LoginManager()
    #needs to be in this format:
    login_manager.login_view = 'auth.login'
    #init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app 

    #imported because we want to make sure models.py runs the classes 
    #are defined before we actually create the database 
    #could also just do import .models
    #creating database:
def create_database(app):
    #check if database already exists. if it doesn't it will create it
    #if it does, we don't want to override it. 
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()  
        print('Created database!')           


