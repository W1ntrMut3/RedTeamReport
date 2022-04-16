from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from RedTeamReport.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=30)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Login")

class AddNewIssueForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = StringField("Description", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField("Add Issue")

class AddNewEngagementForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    description = StringField("Description", validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField("Add Engagement")


