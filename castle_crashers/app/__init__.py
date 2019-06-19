# Quote from The Flask Mega Tutorial:
# In Python, a sub-directory that includes a
# __init__.py file is considered a package, and can
# be imported. When you import a package, the
# __init__.py executes and defines what symbols the
# package exposes to the outside world.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mematicisthebest'
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'mematicisthebest'
db = SQLAlchemy(app)
app.static_folder = 'static'

#Error Handler
#def create_app(config_filename):
#    app = Flask(__name__)
#    app.register_error_handler(404, page_not_found)
#    return app

from app import routes, models

app.run(port=8080, debug=True)

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.secret_key = 'hellothereoldsport'
#WTF_CSRF_ENABLED = True
#WTF_CSRF_SECRET_KEY = 'hE110_Th3r3_0Ld_Sp0rT'
#db = SQLAlchemy(app)
