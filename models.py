from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    # RELACIÓN MUCHOS A MUCHOS (Apunta a la tabla intermedia)
    cursos = db.relationship('Curso', secondary='inscripciones', back_populates='alumnos')

class Maestro(db.Model):
    __tablename__ = 'maestros'
    matricula = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    
    cursos = db.relationship('Curso', back_populates='maestro')

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    
    
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.matricula'), nullable=False)
    maestro = db.relationship('Maestro', back_populates='cursos')
    
    
    alumnos = db.relationship('Alumno', secondary='inscripciones', back_populates='cursos')

class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, server_default=db.func.now())

    
    __table_args__ = (
        db.UniqueConstraint('alumno_id', 'curso_id', name='uq_alumno_curso'),
    )