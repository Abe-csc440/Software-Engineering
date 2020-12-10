"""
    Forms
    ~~~~~
"""
from flask_wtf import Form
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms import TextField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError

from wiki.core import clean_url
from wiki.web import current_users
from wiki.web import current_wiki


class URLForm(Form):
    url = TextField('', [InputRequired()])

    def validate_url(form, field):
        if current_wiki.exists(field.data):
            raise ValidationError('The URL "%s" exists already.' % field.data)

    def clean_url(self, url):
        return clean_url(url)


class SearchForm(Form):
    term = TextField('', [InputRequired()])
    ignore_case = BooleanField(
        description='Ignore Case',
        # FIXME: default is not correctly populated
        default=True)


class EditorForm(Form):
    title = TextField('', [InputRequired()])
    body = TextAreaField('', [InputRequired()])
    tags = TextField('')


class LoginForm(Form):
    name = TextField('', [InputRequired()])
    password = PasswordField('', [InputRequired()])

    def validate_name(form, field):
        user = current_users.get_user(field.data)
        if not user:
            raise ValidationError('This username does not exist.')

    def validate_password(form, field):
        user = current_users.get_user(form.name.data)
        if not user:
            return
        if not user.check_password(field.data):
            raise ValidationError('Username and password do not match.')


class RegisterForm(Form):
    #username = TextField('', [InputRequired()])
    name = TextField('', [InputRequired()])
    password = PasswordField('', [InputRequired()])
    fullName = TextField('', [InputRequired()])
    email = TextField('', [InputRequired()])

    def validate_name(form, field):
        user = current_users.get_user(field.data)
        if user:
            raise ValidationError('This username exists')

class UnregisterForm(Form):
    name = TextField('', [InputRequired()])

    def validate_name(form, field):
        user = current_users.get_user(field.data)
        if not user:
            raise ValidationError('This username does not exist.')
