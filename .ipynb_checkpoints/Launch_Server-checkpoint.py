import subprocess
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from ipywidgets.embed import embed_minimal_html


PORT = 7000
HOST = '127.0.0.1'
SERVER_ADDRESS = '{host}:{port}'.format(host=HOST, port=PORT)
FULL_SERVER_ADDRESS = 'http://' + SERVER_ADDRESS


def TemproraryHttpServer(page_content_type, raw_data):
    """
    A simpe, temprorary http web server on the pure Python 3.
    It has features for processing pages with a XML or HTML content.
    """

    class HTTPServerRequestHandler(BaseHTTPRequestHandler):
        """
        An handler of request for the server, hosting XML-pages.
        """

        def do_GET(self):
            """Handle GET requests"""

            # response from page
            self.send_response(200)

            # set up headers for pages
            content_type = 'text/{0}'.format(page_content_type)
            self.send_header('Content-type', content_type)
            self.end_headers()

            # writing data on a page
            self.wfile.write(bytes(raw_data, encoding='utf'))

            return

    if page_content_type not in ['html', 'xml']:
        raise ValueError('This server can serve only HTML or XML pages.')

    page_content_type = page_content_type

    # kill a process, hosted on a localhost:PORT
    subprocess.call(['fuser', '-k', '{0}/tcp'.format(PORT)])

    # Started creating a temprorary http server.
    httpd = HTTPServer((HOST, PORT), HTTPServerRequestHandler)

    # run a temprorary http server
    httpd.serve_forever()


def run_html_server(html_data=None):

    if html_data is None:
        html_data = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        </body>
        </html>
        """
      
    # open in a browser URL and see a result
    webbrowser.open(FULL_SERVER_ADDRESS)

    # run server
    TemproraryHttpServer('html', html_data)
    
    
from tempfile import NamedTemporaryFile
tmp = NamedTemporaryFile()
m.save(tmp.name)
#embed_minimal_html('tmp.name', views=[w], title='Widgets export')
with open(tmp.name) as f:
    #embed_minimal_html('f', views=[w], title='Widgets export')
    folium_map_html = f.read()


