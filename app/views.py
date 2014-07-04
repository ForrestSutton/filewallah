#!/usr/bin/python
from base import BaseHandler
from google.appengine.ext import ndb        


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
    def get(self):
        self.render('new.html')
  
    def post(self):
        title = self.request.get('title')
        link = self.request.get('link')
        comment = self.request.get('comment')
        
        file_post = File(title=title, link=link, comment=comment)
        file_post.put()
        self.redirect('/')    

class About(BaseHandler):
    def get(self):
        self.render('about.html')
