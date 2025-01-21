import os
from flask import Flask
from dotenv import load_dotenv
from app.infrastructure.exceptions.ResponseErrorsHandlersGlobal import responseErrorsHandlersGlobal
from app.infrastructure.outputs.sqlites.configurations.DatabaseConfiguration import init_app, db

load_dotenv()
app = Flask(__name__)
init_app(app)

responseErrorsHandlersGlobal(app)

if __name__ == '__main__':
    from app.infrastructure.inputs.rest.SongRestController import songRoute
    from app.infrastructure.inputs.rest.AlbumRestController import albumRoute
    app.register_blueprint(albumRoute)
    app.register_blueprint(songRoute)

    app.run(debug=os.getenv('DEBUG'), host=os.getenv('HOST'), port=os.getenv('PORT'))
    with app.app_context():
        db.create_all()