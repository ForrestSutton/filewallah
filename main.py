#!/usr/bin/python

import os
import webapp2
from models import File
#from views import MainPage, About, New, Member
#from memberView import Member
#import app.views 
from app.views import MainPage, About, New

app = webapp2.WSGIApplication([('/', MainPage), ('/about', About),('/new', New), ], debug=True)
