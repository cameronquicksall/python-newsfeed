from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# `engine` variable manages the overall connection to the db
# `Session` variable generates temporary connections for preforming CRUD operations
# `Base` class variable helps us map the models to real MySQL tables

def init_db(app):
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)
# Whenever the preceding function is called, it returns a new session-connection object. 
# Other modules in the app can import Session directly from the db package, but using a function means that
# we can perform additional logic before creating the database connection.
# In this case, The get_db() function now saves the current connection on the g object, if it's not already there. 
# Then it returns the connection from the g object instead of creating a new Session instance each time.
def get_db():
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()

        return g.db
# The pop() method attempts to find and remove db from the g object. If db exists (that is, db doesn't equal None), then db.close() will end the connection.
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()