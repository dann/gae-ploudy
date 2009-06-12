import re
import sys
import os
from google.appengine.ext import webapp
from ploudy import dispatcher

def setup(app_base_dir):
  setup_app_home(app_base_dir)
  app = setup_application()
  app = setup_middlewares(app);
  return app

def setup_application():
  app = webapp.WSGIApplication([
      (r'.*', RequestHandler),
    ], debug=True)
  return app

def setup_middlewares(app):
  return app

def setup_app_home(app_base_dir):
  sys.path.append(os.path.dirname(app_base_dir))
  sys.path.append(os.path.join(os.path.dirname(app_base_dir), 'app'))

class RequestHandler(webapp.RequestHandler):
  def get(self, *args):
    self._handle_request()

  def post(self, *args):
    self._handle_request()

  def head(self, *args):
    self._handle_request()

  def options(self, *args):
    self._handle_request()

  def put(self, *args):
    self._handle_request()

  def delete(self, *args):
    self._handle_request()

  def trace(self, *args):
    self._handle_request()

  def _handle_request(self):
    dispatcher.dispatch(self)

