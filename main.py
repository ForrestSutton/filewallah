import os
import jinja2
import webapp2

#from google.appengine.ext ndb
#from google.appengine.api import users


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

class About(webapp2.RequestHandler):
  def get(self):
      template_values = {
                         'about': 'welcome to the about page'
      }
      template = jinja_environment.get_template('about.html')
      self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage), ('/about', About), ], debug=True)

