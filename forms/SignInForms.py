from wtforms import Form, StringField, PasswordField, SubmitField, validators
from . CSRFBaseForm import CSRFBaseForm

class SignInForm(CSRFBaseForm):
    name = StringField('Name:', [validators.Length(min=4, max=50), validators.required()], _name="name")
    password = PasswordField('Password:', [validators.Length(min=8, max=50), validators.required()], _name="password")
    submit = SubmitField('SignIn')