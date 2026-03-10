from flask_wtf import FlaskForm  # Cambiar esta importación
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(FlaskForm): # Cambiar Form por FlaskForm
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
    
class MaestroForm(FlaskForm): # Cambiar Form por FlaskForm
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