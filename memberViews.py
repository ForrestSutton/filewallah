#!/usr/bin/python
#
import os
import jinja2
import webapp2
from models import Member
from views import MainPage
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


class Member(BaseHandler):
    def get(self):
        self.render('member.html')

    def post(self):
    	name      = self.request.get('name')
        email     = self.request.get('email')
        ext		  = self.request.get('ext')
        funFact   = self.request.get('funFact')
        startDate = self.request.get('startDate')




        title = self.request.get('title')
        link = self.request.get('link')
        comment = self.request.get('comment')

        file_post = File(title=title, link=link, comment=comment)
        file_post.put()
        self.redirect('/')     
