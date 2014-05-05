from google.appengine.ext import db
import datetime

class Books(db.Model):
title = db.StringProperty(required=True)
author = db.StringProperty(required=True)
copyright_year = db.IntegerProperty()
author_birthdate = db.DateProperty()

obj = Books(title='The Grapes of Wrath',
author='John Steinbeck')
obj.copyright_year = 1939
obj.author_birthdate = datetime.date(1902, 2, 27)

obj.put()
