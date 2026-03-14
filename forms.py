<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, SubmitField, EmailField
from wtforms import validators
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Maestros, Curso, Alumno

class UserForm(FlaskForm): 
    id = IntegerField('id')
    nombre = StringField('nombre', [validators.DataRequired(message='El nombre es obligatorio'),validators.Length(min=4, max=20, message='Requiere entre 4 y 20 caracteres')])
    apellidos = StringField('apellidos', [validators.DataRequired(message='El apellido es requerido')])
    telefono = StringField('telefono', [validators.DataRequired(message='El teléfono es requerido')])
    email = EmailField('correo', [validators.DataRequired(message='El correo es requerido'),validators.Email(message='Ingresa un correo válido')])
    
    submit = SubmitField('Enviar')

class MaestrosForm(FlaskForm): 
    matricula = IntegerField('id')
    nombre = StringField('nombre', [validators.DataRequired(message='El nombre es obligatorio'),validators.Length(min=4, max=20, message='Requiere entre 4 y 20 caracteres')])
    apellidos = StringField('apellidos', [validators.DataRequired(message='El apellido es requerido')])
    especialidad = StringField('especialidad', [validators.DataRequired(message='La especialidad es requerida')])
    email = EmailField('correo', [validators.DataRequired(message='El correo es requerido'),validators.Email(message='Ingresa un correo válido')])
    
    submit = SubmitField('Enviar')

class CursosForm(FlaskForm):
    id = IntegerField('id')
    nombre = StringField('Nombre del Curso', [validators.DataRequired(message='El nombre es obligatorio'),validators.Length(min=4, max=50)])
    descripcion = StringField('Descripción', [validators.DataRequired(message='La descripción es requerida'),validators.Length(min=10, max=200)])
    
    maestro = QuerySelectField(
        'Asignar Maestro',
        query_factory=lambda: Maestros.query.all(), 
        get_label='nombre',
        allow_blank=True,
        blank_text='-- Selecciona un Maestro --'
    )
    submit = SubmitField('Enviar')

class InscripcionForm(FlaskForm):
    id = IntegerField('id', [validators.Optional()])
    
    alumno = QuerySelectField(
        'Alumno', 
        query_factory=None, 
        get_label=lambda a: f"{a.nombre} {a.apellidos}",
        allow_blank=True,
        blank_text='-- Selecciona un Alumno --'
    )
    
    curso = QuerySelectField(
        'Curso',
        query_factory=None,
        get_label='nombre',
        allow_blank=True,
        blank_text='-- Selecciona un Curso --'
    )
    
    fecha_inscripcion = StringField('Fecha de Inscripción', [
        validators.DataRequired(message='La fecha es obligatoria')
    ])
    
    submit = SubmitField('Inscribir Alumno')
=======
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(FlaskForm):
    id = IntegerField('id', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])

    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])

    apellidos = StringField('apellidos', [
        validators.DataRequired(message='El apellido es requerido')
    ])

    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])

    telefono = StringField('telefono', [
        validators.DataRequired(message='El telefono es requerido'),
        validators.Length(min=10, max=15, message='Telefono invalido')
    ])

class MaestroForm(FlaskForm):
    matricula = IntegerField('matricula', [
        validators.number_range(min=1, max=20, message='valor no valido')
    ])

    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])

    apellidos = StringField('apellidos', [
        validators.DataRequired(message='El apellido es requerido')
    ])

    especialidad = StringField('especialidad', [
        validators.DataRequired(message='La especialidad es requerida'),
    ])

    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
>>>>>>> 5d0e5cb02d7b8789d994332094f5671803e63677
