import json
import urllib.request
def application(environ, start_response):
    req = urllib.request.urlopen('http://words.bighugelabs.com/api/2/8d3479c49640d29f2222950de32e83ff/word/json')
    reqbytes = req.read()
    reqdec = reqbytes.decode("utf8")
    status = '200 OK'
   
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(reqdec)))]
    start_response(status, response_headers)

    return [reqdec]
