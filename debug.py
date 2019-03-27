from google.appengine.ext import ndb


class DBDEBUG(ndb.Model):
    msg = ndb.StringProperty()


def log(text):
    dbm = DBDEBUG()
    dbm.msg = text
    dbm.put()
