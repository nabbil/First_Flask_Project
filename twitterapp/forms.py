from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[
                                 DataRequired(), EqualTo('password')])
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()

    def __repr__(self):
        return "{}".format(self.username)

    def __repr__(self):
        return "{}".format(self.username)


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()])
    submit = SubmitField()

