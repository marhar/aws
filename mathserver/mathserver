#!/usr/bin/python
"""
mathserver -- simple math server for AWS experimentation
"""

import BaseHTTPServer
import urlparse
import cgi

class GetHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        return
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)

        try:
            d = cgi.parse_qs(parsed_path.query)
            op=d.get('op',None)[0]
            x=int(d.get('x',None)[0])
            y=int(d.get('y',None)[0])
            print op,x,y

            if   op == 'add': z = x + y
            elif op == 'sub': z = x - y
            elif op == 'mul': z = x * y
            elif op == 'div': z = x / y

            self.send_response(200)
            self.end_headers()
            self.wfile.write('%s\n'%(z))
        except Exception,e:
            print e
            self.send_response(500)
            self.end_headers()
            self.wfile.write('internal error\n')

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer(('localhost', 8888), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
