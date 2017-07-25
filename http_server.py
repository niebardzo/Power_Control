import http.server
from dbsenderhttp import dbsenderhttp
import urllib.parse


class SimpleHTTPRequestHandler1(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        bits = urllib.parse.urlparse(self.path)
        print(self.command, bits)
        buff = bits.query.split('&')
        buffer = []
        for i in buff:
            a = i.split('=')
            buffer.append(a[1])
        dbsenderhttp(buffer)
        return super(SimpleHTTPRequestHandler1, self).do_GET()


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler1):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()