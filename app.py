from wtforms import form

from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g 
from flask_migrate import Migrate
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos


import forms
from models import db
from models import Alumno, Maestro, Curso
app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_muy_secreta_123'
csrf=CSRFProtect(app)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
migrate = Migrate(app, db)


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")


@app.route("/")
@app.route("/index")
def index():
	return render_template("bienvenida.html")



if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()