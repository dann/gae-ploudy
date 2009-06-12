
class BaseController(object):
  def __init__(self, route, handler):
    self.route = route 
    self.handler = handler

