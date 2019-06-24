from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField,SubmitField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from app.models import User

#Edit profile
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

#to post
class PostForm(FlaskForm):
    post = TextAreaField(
        'write somethoing',
        validators=[DataRequired(),Length(min=1,max=140)]    
    )
    submit = SubmitField('Submit')

#to comment
class CommentForm(FlaskForm):
    comment = TextAreaField(
        'write comment here',
        validators=[DataRequired(),Length(min=1,max=64)]
    )
    submit = SubmitField('send')
    