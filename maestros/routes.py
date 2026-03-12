from flask import Blueprint, render_template, request, redirect, url_for, flash
import forms
from models import db, Maestros

maestros = Blueprint('maestros', __name__)

@maestros.route("/maestros", methods=['GET', 'POST'])
def lista_maestros():
    create_form = forms.MaestroForm(request.form)
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros_list)

@maestros.route("/maestros/crear", methods=['GET', 'POST'])
def crear_maestros():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST' and create_form.validate():
        maes = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
    return render_template("maestros/crearMaes.html", form=create_form)

@maestros.route("/maestros/detalles", methods=['GET'])
def detalles():
    matricula = request.args.get('matricula')
    maes = Maestros.query.filter_by(matricula=matricula).first()
    if not maes:
        return redirect(url_for('maestros.lista_maestros'))
    
    form = forms.MaestroForm(obj=maes)
    
    return render_template("maestros/detallesMaes.html", 
                           maestro=maes, 
                           form=form, 
                           nombre=maes.nombre, 
                           apellidos=maes.apellidos, 
                           especialidad=maes.especialidad, 
                           correo=maes.email)

@maestros.route("/maestros/modificar", methods=['GET', 'POST'])
def modificar():
    
    matricula = request.args.get('matricula') or request.form.get('matricula')
    maes1 = Maestros.query.filter_by(matricula=matricula).first()
    
    if not maes1:
        return redirect(url_for('maestros.lista_maestros'))

    
    create_form = forms.MaestroForm(request.form)
    
    if request.method == 'GET':
    
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email
            
    if request.method == 'POST' and create_form.validate():
    
        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.especialidad = create_form.especialidad.data
        maes1.email = create_form.email.data
        
        db.session.add(maes1) 
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
        
    return render_template("maestros/modificarMaes.html", form=create_form)

@maestros.route("/maestros/eliminar", methods=['GET', 'POST'])
def eliminar():
    matricula = request.args.get('matricula') or request.form.get('matricula')
    maes = Maestros.query.filter_by(matricula=matricula).first()
    
    if not maes:
        return redirect(url_for('maestros.lista_maestros'))

    
    form = forms.MaestroForm(request.form, obj=maes)
    
    
    if request.method == 'POST':
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.lista_maestros'))
            
    return render_template("maestros/eliminarMaes.html", form=form, maestro=maes)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"