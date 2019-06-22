from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2=PasswordField(
        'Repeat Password',validators=[DataRequired(),EqualTo('password')]
    )
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use different user name')
        
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('PLease use diff. email')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self,original_username,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.original_username = original_username
    
    def validate_username(self,username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('please use diff. user name')

class PostForm(FlaskForm):
    post = TextAreaField(
        'write somethoing',
        validators=[DataRequired(),Length(min=1,max=140)]    
    )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField(
        'write comment here',
        validators=[DataRequired(),Length(min=1,max=64)]
    )
    submit = SubmitField('send')