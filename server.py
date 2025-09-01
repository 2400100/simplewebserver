from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!DOCTYPE html>
<html>
<head>
    <title>HTML Table Example</title>
</head>
<body>
    <h2>list of protocols in TCP/IP protocol suite</h2>

    <table border="1">
        <tr>
            <th>s.no</th>
            <th>name of layers</th>
            <th>name of the protocol</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Application layer</td>
            <td>HTTP,FTP,DNS,Telnet&SSH</td>
        
        </tr>
        <tr>
             <td>2</td>
             <td>Transport layer</td>
             <td>TCP/UDP</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Network layer</td>
            <td>IPV4,IPV6</td>
        </tr>
         <tr>
            <td>4</td>
            <td>Link layer layer</td>
            <td>Ethernet</td>
        </tr>

           
    </table>


</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()