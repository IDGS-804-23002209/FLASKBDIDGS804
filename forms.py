from flask_wtf import Form
from wtforms import Form, StringField, IntegerField, SubmitField, EmailField
from wtforms import validators

class UserForm(Form): 
    id = IntegerField('id', [validators.NumberRange(min=1, max=20, message='Valor no válido')])
    nombre = StringField('nombre', [validators.DataRequired(message='El nombre es obligatorio'),validators.Length(min=4, max=20, message='Requiere entre 4 y 20 caracteres')])
    apaterno = StringField('apaterno', [validators.DataRequired(message='El apellido es requerido')])
    email = EmailField('correo', [validators.DataRequired(message='El correo es requerido'),validators.Email(message='Ingresa un correo válido')])
    
    submit = SubmitField('Enviar')