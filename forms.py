from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators

def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')

class CommentForm(Form):
    username = StringField('Username',
                [ 
                    validators.Required(message='El username es requerido.'),
                    validators.length(min=4, max=25, message='Ingrese un username valido!')
                ])
    email = EmailField('Correo electronico',
                [
                    validators.Required(message='El email es requerido.'),
                    validators.Email(message='Ingrese un Email valido.')
                ])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [lenght_honeypot])

class LoginForm(Form):
    username = StringField('Username',
                [
                    validators.Required(message='El username es requerido.'),
                    validators.length(min=4, max=25, message='Ingrese un username valido.')
                ])
    password = PasswordField('Password',
                [
                    validators.Required('El password es requerido.')
                ])

class CreateForm(Form):
    username = StringField('Username',
                [ 
                    validators.Required(message='El username es requerido.'),
                    validators.length(min=4, max=25, message='Ingrese un username valido!')
                ])
    password = PasswordField('Password',
                [
                    validators.Required('El password es requerido.')
                ])            
    email = EmailField('Correo electronico',
                [
                    validators.Required(message='El email es requerido.'),
                    validators.Email(message='Ingrese un Email valido.')
                ])