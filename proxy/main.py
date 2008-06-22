import wsgiref.handlers
from google.appengine.ext import webapp

from hello import MainPage
from fetch import Fetch

def main():
  application = webapp.WSGIApplication(
                                       [('/proxy/', MainPage),
                                        ('/proxy/fetch',Fetch),],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
