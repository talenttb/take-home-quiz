# -*- coding: utf-8 -*-
# # from app import create_app

# app = create_app()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from app import create_app
import logging
from flask_script import Manager, Shell, Server

server = Server(host="0.0.0.0", threaded=True)
app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("server", server)


if __name__ == '__main__':
    manager.run()
