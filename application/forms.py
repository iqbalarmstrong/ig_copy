from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email 

from application.utils import exists_email, not_exists_email, exists_username


class LoginFrom(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Login")
    
class SingupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8), exists_username])
    fullname = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email = PasswordField("email", validators=[DataRequired(), Email(), exists_email])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("sing up")

class EditProfile(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8), exists_username])
    Email = PasswordField("Email", validators=[DataRequired(), Email(), exists_email])
    edit_pic = StringField("Edit_pic", validators=[FileAllowed(["jpg","png", "jpeg"])])
    password = PasswordField("password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("change")
    
class ResetPasswordForm(FlaskForm):
    old_password = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("reset password")
    
class ForgotPasswordForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), not_exists_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("send link verivication to email")
 
class VerivicationPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")
    
class CreatePost(FlaskForm):
    photo = StringField("Photo", validators=[DataRequired(), FileAllowed(["jpg","png","jpeg"])])
    bio = TextAreaField("Bio")
    submit = SubmitField("Confirm")

class EditPost(FlaskForm):
    edit_bio = StringField("Edit_bio")
    submit = SubmitField("Change")