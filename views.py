# import jinja2
# import os
# import webapp2
# from datetime import datetime
# from google.appengine.ext import db

# from models import Books

# TEMPLATE_DIR = os.path.join(os.path.dirname(__file__)+ '/templates')
# jinja_environment = \
#     jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

# # class MainPage(webapp2.RequestHandler):
# #     def get(self, *args, **kwargs):
# #     q = db.GqlQuery("SELECT * FROM Books")
# #     bookss = q.fetch(20)
# #     utils.render_template(self, 'index.html', 'books':books) 


# #	template = jinja_evironment.get_template('index.html')
# #	self.render_template('index.html', {'books': books})
