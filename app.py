from flask import Flask
from application.database import db
import os

app = None
rootDir = os.path.abspath(os.path.dirname('file'))

database_uri = f"sqlite:///{os.path.join(rootDir, 'instance', 'mad1_project.sqlite3')}"
print(database_uri)

def create_app():
  app = Flask(__name__)
  app.debug = True
  app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
  app.app_context().push()
  db.init_app(app)

  return app

app = create_app()

from application.controllers import *


if __name__ == '__main__':
  app.run()