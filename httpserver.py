from http.server import BaseHTTPRequestHandler,HTTPServer
import json
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pass
    def do_POST(self):
        print('hh')
        print(self.command)
        print(self.client_address)
        print(self.path)
        try:
            data={'error':'a','sql':"select ..."}
            data=json.dumps(data)
            query=self.rfile.read(int(self.headers['content-length']))
            print(query)
            query=json.loads(query)
            print(query)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin','*')
            self.send_header('Content-type','application/json')

            self.end_headers()
            self.wfile.write(data.encode(encoding='utf-8'))
        except ConnectionError:
            self.send_error(404,'error')
def main():
    ip=""
    port=8001
    try:
        server=HTTPServer((ip,port),MyHandler)
        print('Start HttpServer')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shut Down Serve')
        server.socket.close()
if __name__=="__main__":
    main()



