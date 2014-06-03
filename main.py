import webapp2
import os
from models import File
from views import MainPage, About, New

app = webapp2.WSGIApplication([('/', MainPage), ('/about', About),('/new', New), ], debug=True)
