from config import app, db

from apps.index import apps
from users.controller import users
from errors.index import not_found

db.create_all()

# Error handlers register
app.register_error_handler(404, not_found)

# Routes register
app.register_blueprint(apps, url_prefix='/v1')
app.register_blueprint(users, url_prefix='/v1')

if __name__ == '__main__':
    app.run(
        host= app.config['HOST'],
        port= app.config['PORT'],
        debug= app.config['DEBUG']
    )