from flask import Blueprint
from .routes import maestros

maestros = Blueprint(
    'maestros',
    __name__,
    template_folder='templates',
    static_folder='static'
)
from . import routes