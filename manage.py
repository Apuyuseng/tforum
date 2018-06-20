import os
import tornado.ioloop
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie('is_auth'):
            self.set_secure_cookie('is_auth','ok')
        self.render("index.html", title="主页")

def make_app():
    from setting import settings
    return tornado.web.Application([
        (r"/", MainHandler),
    ],**settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()