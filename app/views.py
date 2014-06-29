#!/usr/bin/python

import os
import jinja2
import webapp2
import basehandlers
from models import File
from datetime import datetime
from google.appengine.ext import ndb

template_dir=os.path.join(os.path.dirname(__file__),"templates")
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainPage(BaseHandler):
    def get(self):
	files = ndb.gql("SELECT * FROM File LIMIT 10")
	file_dic = {"files": files }
        self.render('index.html', **file_dic)

    def post(self):
        title = self.request.get('title')
        link = self.request.get('link')
        comment = self.request.get('comment')
        self.write(title)
        self.write("<br />")
        self.write(link)
        self.write("<br />")
        self.write(comment)

class New(BaseHandler):
    pass
#     def get(self):
#         self.render('new.html')
  
#     def post(self):
#         title = self.request.get('title')
#         link = self.request.get('link')
#         comment = self.request.get('comment')
        
#         file_post = File(title=title, link=link, comment=comment)
#         file_post.put()
#         self.redirect('/')    

class About(BaseHandler):
    def get(self):
        self.render('about.html')
