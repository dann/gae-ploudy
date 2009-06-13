from ploudy import controller

class RootController(controller.BaseController):
  def index(self):
    print 'hello'

class HelloController(controller.BaseController):
  def index(self):
    print 'hello world'
