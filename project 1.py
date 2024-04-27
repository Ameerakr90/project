from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHTTPHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()

