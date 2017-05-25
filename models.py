from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

class Post(db.Model):
    teacher = db.StringProperty(required = True)
    student = db.StringProperty(required = True)
    lessondate = db.StringProperty(required = False)
    body = db.TextProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)
    author = db.ReferenceProperty(required = True) 


