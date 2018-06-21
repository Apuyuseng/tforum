import tornado.ioloop
import tornado.web
from tornado.options import define, options
from ven import app,load_app
define("port", default=8000, help="run on the given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    load_app()
    app.Application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()