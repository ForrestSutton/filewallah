#!/usr/bin/env python
# encoding: utf-8
"""
public_forms.py
"""

from wtforms import Form, TextField, TextAreaField, BooleanField, validators


class fileForm(Form):
	title   = TextField(u'file title', validators=[validators.required()])   
    link    = TextField(u'link', validators=[validators.required()])
    comment = TextAreaField(u'Comment')
    adddate = ndb.DateTimeProperty(auto_now_add=True) 

class MemberForm(Form):
    name      = TextField(u'link', validators=[validators.required()]) 
    email     = TextField(u'link', validators=[validators.required()])
    ext		  = TextField(u'link', validators=[validators.required()])	
    funFact   = TextAreaField(u'fun fact') 
    startDate = ndb.DateTimeProperty()   

	
	# cumstom validation code 
	# def validate_company(form, field):
	# 	founder = form.founder.data
	# 	if founder:
	# 		if not field.data:
	# 			raise validators.ValidationError('If you are Founder, Company Domain is Required')