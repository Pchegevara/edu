from cgi import parse_qs

def app(environ, start_response):
        #business logic
        
        data = parse_qs(environ['QUERY_STRING'])
        
        i=1
        s='\n'
        body = str()
        
        for key, value in data.items():
            if i!=len(data):
                body+=key + '=' + ''.join(value) + '\n'
            else: 
                body+=key + '=' + ''.join(value)
        
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, headers)
        return iter([body.encode()])
