from locations import get_locations_js

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/javascript')]

    start_response(status, headers)

    ret = get_locations_js()
    return ret
