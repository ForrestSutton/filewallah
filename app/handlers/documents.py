import _base

 from app.models import File

class NewDocument(_base.BaseHandler):
    def get(self):
        self.render('new.html')

    def post(self):
        title = self.request.get('title')
        link = self.request.get('link')
        comment = self.request.get('comment')

        file_post = File(title=title, link=link, comment=comment)
        file_post.put()
        self.redirect('/')
