from wtforms import form

from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g 
from flask_migrate import Migrate
from maestros.routes import maestros


import forms
from models import db
from models import Alumnos
app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_muy_secreta_123'
csrf=CSRFProtect(app)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
app.register_blueprint(maestros)
migrate = Migrate(app, db)


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
                       apellidos=create_form.apellidos.data,
                       telefono=create_form.telefono.data,
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
        apellidos = alumn.apellidos
        telefono = alumn.telefono
        correo = alumn.email
    else:
        # Si no hay alumno, redirigir o manejar el error
        return redirect(url_for('index'))

    # 3. Pasar 'form' al template para evitar el UndefinedError
    return render_template(
        "detalles.html",
        form=create_form,
        nombre=nombre,
        apellidos=apellidos,
        telefono=telefono,
        correo=correo
    )
    
@app.route("/modificar", methods=['POST', 'GET'])
def modificar():
    create_form = forms.UserForm(request.form)
    
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.telefono.data=alum1.telefono
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellidos=create_form.apellidos.data
        alum1.telefono=create_form.telefono.data
        alum1.email=create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("modificar.html",form=create_form)

@app.route("/eliminar", methods=['POST', 'GET'])
def eliminar():
    create_form = forms.UserForm(request.form)
    
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.telefono.data=alum1.telefono
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("eliminar.html",form=create_form)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()