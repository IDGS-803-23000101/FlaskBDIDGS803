from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms import EmailField
from wtforms import validators
from wtforms.validators import DataRequired

class UserForm(FlaskForm): 
    id = IntegerField('Id')
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingrese nombre valido')])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='El campo es requerido')])
    telefono = StringField('Telefono', [
        validators.DataRequired(message='El campo es requerido')])
    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])
    
class MaestroForm(FlaskForm):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='La matricula es requerida')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='Ingrese nombre valido')
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='El campo es requerido')
    ])
    especialidad = StringField('Especialidad', [
        validators.DataRequired(message='La especialidad es requerida')
    ])
    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])
    
class InscripcionForm(FlaskForm):
    alumno_id = SelectField('Seleccionar Alumno', coerce=int, validators=[DataRequired()])
    curso_id = SelectField('Seleccionar Curso', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Inscribir')
    
class CursoForm(FlaskForm):
    nombre = StringField('Nombre del Curso', validators=[DataRequired()])
    descripcion = StringField('Descripción')
    # Este menú desplegable mostrará a los maestros registrados
    maestro_id = SelectField('Maestro que lo imparte', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Crear Curso')