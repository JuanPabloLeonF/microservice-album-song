import os
from flask import Flask
from dotenv import load_dotenv
from app.infrastructure.exceptions.ResponseErrorsHandlersGlobal import responseErrorsHandlersGlobal
from app.infrastructure.outputs.mysql.configurations.DatabaseConfiguration import init_app_db, db

load_dotenv()
app = Flask(__name__)

init_app_db(app=app, DATABASE_URL=os.getenv('DATABASE_URL'))

responseErrorsHandlersGlobal(app)

if __name__ == '__main__':
    from app.infrastructure.inputs.rest.SongRestController import songRoute
    from app.infrastructure.inputs.rest.AlbumRestController import albumRoute
    app.register_blueprint(albumRoute)
    app.register_blueprint(songRoute)
    with app.app_context():
        db.create_all()

    app.run(debug=os.getenv('DEBUG'), host=os.getenv('HOST'), port=os.getenv('PORT'))