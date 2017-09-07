
from http.server import HTTPServer, CGIHTTPRequestHandler
import time
port = 8080
timer1 = time.time()
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
timer2 = time.time()
print("Starting httpd on port: " + str(httpd.server_port) + ", used", str(round(timer2-timer1, 2)) + " second(s)..")
httpd.serve_forever()
