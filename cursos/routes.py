from flask import Blueprint, render_template, request, redirect, url_for
from models import Curso, Alumnos, db
from . import cursos

@cursos.route("/cursos")
def index():
    cursos = Curso.query.all()
    return render_template("cursos/cursos.html", cursos=cursos)
    
@cursos.route("/cursos/<int:id>/alumnos")
def alumnos_curso(id):
    curso = Curso.query.get_or_404(id)
    return render_template("cursos/alumnos_curso.html", curso=curso)

@cursos.route("/cursos/<int:curso_id>/inscribir/<int:alumno_id>")
def inscribir(curso_id, alumno_id):

    curso = Curso.query.get_or_404(curso_id)
    alumno = Alumnos.query.get_or_404(alumno_id)

    curso.alumnos.append(alumno)
    db.session.commit()

    return redirect(url_for("cursos.alumnos_curso", id=curso_id))