# Configuration file, this is here to provide
# all the config required by the site, which is
# stored in the Config object, and transferred
# to Flask's configuration when the web app starts

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'load_of-o!d*s0cks'
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "content.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# NB: The 'SECRET_KEY' attribute is to allow Flask
# to encrypt certain transactions.  This is not a
# great password - check this doc page for more
# information about how to create a safe one:
# http://flask.pocoo.org/docs/1.0/quickstart/#sessions

# The SQL path is with respect to the root of the
# drive its stored on, hence the 'basedir' part.
# And the track modifications part is just to
# turn off warnings about something that will
# eventually disappear from the package, and is
# not used anyway.
