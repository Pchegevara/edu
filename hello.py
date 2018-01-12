def app(environ, start_response):
        #business logic
        
      	body =	environ['QUERY_STRING'].replace('&','\n')
	
  
        
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, headers)
        return iter([body.encode()])
