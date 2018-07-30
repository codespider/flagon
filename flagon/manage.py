#!/usr/bin/env python
from flask_script import Manager
from flagon.app import create_app
from flagon.extensions import db
from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()