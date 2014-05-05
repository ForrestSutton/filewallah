import os
import jinja2
import urllib
import webapp2

from google.appengine.ext ndb


jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+ "/templates"),
   extensions=['jinja2.ext.autoescape'],  autoescape=True)

class MainPage(webapp2.RequestHandler):
  def get(self):
      template_values = {
                         'welcome': 'welcome to the page'
       }	
      template = jinja_environment.get_template('index.html')
      self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
