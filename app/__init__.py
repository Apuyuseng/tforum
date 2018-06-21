from tornado.web import RequestHandler
from ven import app

@app.route
class MainHandler(RequestHandler):
    URL = '/'
    def get(self):
        if not self.get_secure_cookie('is_auth'):
            self.set_secure_cookie('is_auth','ok')
        self.render("index.html", title="主页")

