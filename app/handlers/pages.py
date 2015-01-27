import _base
from google.appengine.ext import ndb

class MainPage(_base.BaseHandler):
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

class AboutPage(_base.BaseHandler):
    def get(self):
        self.render('about.html')
