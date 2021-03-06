# -*- coding: utf-8 -*-

import os
from enjoycms import create_app, db
from enjoycms.models import EnjoycmsUser
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, EnjoycmsUser=EnjoycmsUser)
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()