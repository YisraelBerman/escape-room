from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Stage1Form(FlaskForm):
    answer1 = SubmitField('4')  # Correct answer
    answer2 = SubmitField('5')  # Incorrect answer

class Stage2Form(FlaskForm):
    answer1 = SubmitField('6')  # Correct answer
    answer2 = SubmitField('7')  # Incorrect answer

class Stage3Form(FlaskForm):
    answer1 = SubmitField('8')  # Correct answer
    answer2 = SubmitField('9')  # Incorrect answer

class Stage4Form(FlaskForm):
    answer1 = SubmitField('10')  # Correct answer
    answer2 = SubmitField('11')  # Incorrect answer

class Stage5Form(FlaskForm):
    answer1 = SubmitField('12')  # Correct answer
    answer2 = SubmitField('13')  # Incorrect answer
