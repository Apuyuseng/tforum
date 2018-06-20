import tornado.web
from importlib import import_module
from inspect import signature

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie('is_auth'):
            self.set_secure_cookie('is_auth','ok')
        self.render("index.html", title="主页")

def get_view(path='app'):
    import_module('app')


def make_app():
    from setting import settings
    return tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)