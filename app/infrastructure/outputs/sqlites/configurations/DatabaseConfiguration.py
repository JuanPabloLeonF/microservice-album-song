from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app_db(app):
    DATABASE_URI = "conexion a la base de datos del contenedor mysql"
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)