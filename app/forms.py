from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Email

class SubscriberForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
class ContactForm(FlaskForm):
    fname=StringField('First Name', validators=[DataRequired()], description='Please enter your first name.')
    lname=StringField('Last Name', validators=[DataRequired()], description='Please enter your last name.')
    email=StringField('E-mail', validators=[DataRequired(), Email()], description='Please enter your email address.')
    subject=StringField('Subject', validators=[DataRequired()], description='Please enter the subject for your complaint.')
    message=TextAreaField('Message', validators=[DataRequired()], description='Please enter the complaint below.')

    # def __init__(self):
    #     pass
        # self.fname=StringField('First Name', validators=[DataRequired()], description='Please enter your first name.')
        # self.lname=StringField('Last Name', validators=[DataRequired()], description='Please enter your last name.')
        # self.email= StringField('E-mail', validators=[DataRequired(), Email()], description='Please enter your e-mail address.')
        # self.subject=StringField('Subject', validators=[DataRequired()], description='Please enter the subject for you message.')
        # self.message=TextAreaField('Message', validators=[DataRequired()], description='Please enter the message you would like to send.')

    def set_fname(self,fname):
        self.fname=fname

    def get_fname(self):
        return self.fname

    def set_lname(self,lname):
        self.lname=lname
        
    def get_lname(self):
        return self.lname

    def set_email(self,email):
        self.email=email

    def get_email(self):
        return self.email

    def set_subject(self,subject):
        self.subject=subject

    def get_subject(self):
        return self.subject

    def set_message(self,message):
        self.message=message
        
    def get_message(self):
        return self.message