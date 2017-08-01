from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class AdminLogin(Form):

    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me", default=False)


class NewPost(Form):

    title = StringField("title", validators=[DataRequired()])
    body = TextAreaField("body", validators=[DataRequired()])

