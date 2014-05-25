import webapp2
from models import File
from views import MainPage, About, New
from memberView import Member



app = webapp2.WSGIApplication([('/', MainPage), ('/about', About),('/new', New), ('/member', Member), ], debug=True)
