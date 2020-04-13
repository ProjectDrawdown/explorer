import os
import urllib

import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web

tornado.options.define('port', default=8888, help='port to listen on')
tornado.options.define('path', default='./', help='filesystem path')

class RenderMain(tornado.web.RequestHandler):
    def get(self):
        self.render("mock.html")

def main():
    """Start the tornado application."""
    tornado.options.parse_command_line()
    root = os.getenv('JUPYTERHUB_SERVICE_PREFIX', default='/')
    url = os.getenv('JUPYTERHUB_SERVICE_URL', default=None)
    if url is not None:
        u = urllib.parse.urlparse(url)
        tornado.options.options.port = u.port

    app = tornado.web.Application([
        (root, RenderMain),
        (root + r'(.*\.(json|png|svg))', tornado.web.StaticFileHandler,
            {'path': tornado.options.options.path}),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
