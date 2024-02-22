from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astro_id = StringField('ID астронавта', validators=[DataRequired()])
    asto_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('Логин капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
