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
db = SQLAlchemy(app)
app.static_folder = 'static'

from app import routes, models

app.run(port=8080, debug=True)
