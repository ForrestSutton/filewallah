import os
import jinja2
import webapp2

template_dir = os.path.realpath(os.path.join(
  os.path.dirname(__file__), "../templates"
)

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir),
  autoescape=True
)

def render_str(template, **params):
    return jinja_env.get_template(template).render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
