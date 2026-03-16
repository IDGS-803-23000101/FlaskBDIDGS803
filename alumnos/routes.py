from flask import Blueprint, render_template, request, redirect, url_for, flash
import forms
from models import db, Alumno

alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/alumnos')
def lista_alumnos():
	create_form=forms.UserForm(request.form)
	alumno=Alumno.query.all()
	return render_template("alumnos/index.html",form=create_form,alumno=alumno)


@alumnos.route('/agregar', methods=['GET','POST'])
def agregar_alumno():

    create_form = forms.UserForm(request.form)
    if request.method=='POST':
        alum = Alumno(nombre=create_form.nombre.data,
                       apellidos=create_form.apellidos.data,
                       telefono=create_form.telefono.data,
                       email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.lista_alumnos'))
    return render_template("alumnos/alumnos.html", form=create_form)


@alumnos.route("/modificar", methods=['POST', 'GET'])
def modificar():
    create_form = forms.UserForm(request.form)
    
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumno).filter(Alumno.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.telefono.data=alum1.telefono
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum1=db.session.query(Alumno).filter(Alumno.id==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellidos=create_form.apellidos.data
        alum1.telefono=create_form.telefono.data
        alum1.email=create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.lista_alumnos'))
    return render_template("alumnos/modificar.html",form=create_form)


@alumnos.route("/detalles", methods=['POST', 'GET'])
def detalles():
    
    create_form = forms.UserForm(request.form)
    
    
    id = request.args.get('id')
    alumn = db.session.query(Alumno).filter(Alumno.id == id).first()

    if alumn:
        nombre = alumn.nombre
        apellidos = alumn.apellidos
        telefono = alumn.telefono
        correo = alumn.email
    else:
    
        return redirect(url_for('alumnos.lista_alumnos'))

    
    return render_template(
        "alumnos/detalles.html",
        form=create_form,
        nombre=nombre,
        apellidos=apellidos,
        telefono=telefono,
        correo=correo
    )


@alumnos.route("/eliminar", methods=['POST', 'GET'])
def eliminar():
    create_form = forms.UserForm(request.form)
    
    if request.method=='GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumno).filter(Alumno.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.telefono.data=alum1.telefono
        create_form.email.data=alum1.email
    if request.method=='POST':
        id=create_form.id.data
        alum=Alumno.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('alumnos.lista_alumnos'))
    return render_template("alumnos/eliminar.html",form=create_form)

@alumnos.route('/cursos_inscritos/<int:id>', methods=['GET'])
def cursos_alumno(id):
    
    alumno = Alumno.query.get_or_404(id)
    
    return render_template('alumnos/cursos_alumno.html', alumno=alumno)