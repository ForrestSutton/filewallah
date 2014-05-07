import os
import jinja2
import webapp2

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
        self.render('index.html')

    def post(self):
        title = self.request.get('title')
        link = self.request.get('link')
        comment = self.request.get('comment')
        self.write(title)
        self.write("<br />")
        self.write(link)
        self.write("<br />")
        self.write(comment)

class About(BaseHandler):
    def get(self):
        self.render('about.html')


app = webapp2.WSGIApplication([('/', MainPage), ('/about', About), ], debug=True)

