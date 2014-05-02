#models.py
#http://django-appengine.com/

from google.appengine.ext import ndb

class files(db.Model):
    """Models an individual files entry with an original author, content, and date."""
    users = ....
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def get_key_from_name(cls, file_name=None):
        return db.Key.from_path('Files', guestbook_name or 'default_files')