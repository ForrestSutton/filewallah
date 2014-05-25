from google.appengine.ext import ndb
import datetime

class File(ndb.Model):
    title   = ndb.StringProperty()   
    link    = ndb.StringProperty()
    comment = ndb.StringProperty()
    adddate = ndb.DateTimeProperty(auto_now_add=True)



class Member(ndb.Model):
   name      = ndb.StringProperty()   
   email     = ndb.StringProperty()
   ext		  = ndb.StringProperty()	
   funFact   = ndb.StringProperty()
   startDate = ndb.DateTimeProperty()