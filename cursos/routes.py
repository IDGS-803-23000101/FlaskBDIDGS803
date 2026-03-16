from flask import Blueprint, render_template, flash, redirect, request, url_for
from models import db, Curso, Alumno, Maestro
from forms import InscripcionForm, CursoForm
import forms

cursos = Blueprint('cursos', __name__)

@cursos.route('/cursos')
def lista_cursos():
	create_form=forms.UserForm(request.form)
	cursos=Curso.query.all()
	return render_template("cursos/cursos.html",form=create_form,cursos=cursos)

@cursos.route('/<int:curso_id>/alumnos', methods=['GET'])
def alumnos_por_curso(curso_id):
    curso = Curso.query.get_or_404(curso_id)
    return render_template('cursos/alumnos_curso.html', curso=curso, alumnos=curso.alumnos)

@cursos.route('/inscribir', methods=['GET', 'POST'])
def inscribir():
    form = InscripcionForm()
    
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apellidos}") for a in Alumno.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]

    if request.method == 'POST' and form.validate_on_submit():
        alumno = Alumno.query.get(form.alumno_id.data)
        curso = Curso.query.get(form.curso_id.data)
        
        if alumno in curso.alumnos:
            flash('El alumno ya está inscrito en este curso.', 'warning')
        else:
            curso.alumnos.append(alumno) 
            db.session.commit()
            return redirect(url_for('alumnos.lista_alumnos')) 
            
    return render_template('cursos/inscripcion.html', form=form)

@cursos.route('/crear', methods=['GET', 'POST'])
def crear_curso():
    form = CursoForm()
    
    
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestro.query.all()]

    if request.method == 'POST' and form.validate_on_submit():
    
        nuevo_curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
    
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.lista_cursos'))

    return render_template('cursos/crear_curso.html', form=form)