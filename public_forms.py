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
    name      = TextField(u'name', validators=[validators.required()]) 
    email     = TextField(u'email', validators=[validators.required()])
    ext		  = TextField(u'ext', validators=[validators.required()])	
    funFact   = TextAreaField(u'fun fact') 
    startDate = ndb.DateTimeProperty()   

	
	# cumstom validation code 
	# def validate_field(form, field):
	# 	sfield = form.sfield.data
	# 	if sfield:
	# 		if not field.data:
	# 			raise validators.ValidationError('If you are sfield, reasons ')