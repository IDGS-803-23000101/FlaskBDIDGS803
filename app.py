from wtforms import form

from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g 


import forms
from models import db
from models import Alumnos
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")


@app.route("/",methods =['GET','POST'])
@app.route("/index")
def index():
	create_form=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("index.html",form=create_form,alumno=alumno)

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    create_form = forms.UserForm(request.form)
    if request.method=='POST':
        alum = Alumnos(nombre=create_form.nombre.data,
                       apaterno=create_form.apaterno.data,
                       email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("alumnos.html", form=create_form)

@app.route("/detalles", methods=['POST', 'GET'])
def detalles():
    # 1. Instanciar el formulario (necesario para el CSRF y campos)
    create_form = forms.UserForm(request.form)
    
    # 2. Obtener el ID de la URL
    id = request.args.get('id')
    alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()

    if alumn:
        nombre = alumn.nombre
        apaterno = alumn.apaterno
        amaterno = alumn.amaterno
        correo = alumn.email
    else:
        # Si no hay alumno, redirigir o manejar el error
        return redirect(url_for('index'))

    # 3. Pasar 'form' al template para evitar el UndefinedError
    return render_template(
        "detalles.html",
        form=create_form,
        nombre=nombre,
        apaterno=apaterno,
        amaterno=amaterno,
        correo=correo
    )

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()