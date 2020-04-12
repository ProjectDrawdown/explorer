import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web

tornado.options.define('port', default=8888, help='port to listen on')

class RenderMain(tornado.web.RequestHandler):
    def get(self):
        self.render("mock.html")

def main():
    """Start the tornado application."""
    app = tornado.web.Application([
        ('/', RenderMain),
        (r'/(.*\.(json|png|svg))', tornado.web.StaticFileHandler, {'path': './'}),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
