#!/usr/bin/env python
from google.appengine.ext.webapp.util import run_wsgi_app
import ploudy

def main():
  application = ploudy.setup(__file__) 
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
