from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es obligatorio')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es obligatorio')])
    remember_me = BooleanField('Recordarme')
    enviar = SubmitField('Ingresar')

class IngresarPersonalForm(FlaskForm):
    fecha = StringField('Fecha', validators=[DataRequired('Este campo es requerido')])
    nombre = StringField('Nombre', validators=[])
    apellido = StringField('Apellido', validators=[])
    dni = StringField('DNI', validators=[DataRequired('Este campo es requerido')])
    motivo = StringField('Motivo', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Agregar nuevo personal')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})