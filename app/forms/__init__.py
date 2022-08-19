from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es obligatorio')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es obligatorio')])
    remember_me = BooleanField('Recordarme')
    enviar = SubmitField('Ingresar')

