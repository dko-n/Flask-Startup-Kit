from wtforms import Form, StringField, PasswordField, SubmitField, validators
from . CSRFBaseForm import CSRFBaseForm

class CustomSubmitField(SubmitField):
    """
    SubmitFieldのname属性を変更するための上書きクラス
    """
    def __init__(self, label='', validators=None, _name='', **kwargs):
        super(SubmitField, self).__init__(label, validators, _name='', **kwargs)
        override_name = "send_name"
        override_id = "send_id"
        self.name = override_name
        self.id = override_id

class SignInForm(CSRFBaseForm):
    name = StringField('Name:', [validators.Length(min=4, max=50), validators.required()], _name="name")
    password = PasswordField('Password:', [validators.Length(min=8, max=50), validators.required()], _name="password")
    submit = CustomSubmitField('SignIn')