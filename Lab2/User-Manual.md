# User Manual for Net Ninny web proxy

The Net Ninny web proxy is a python program which can be used to block web pages with certain words.

## Specification

* supports HTTP/1.0 and HTTP/1.1
* Handles simple HTTP GET interactions between client and server
* Blocks requests for undesirable URLs, using HTTP redirection to display this error page instead
* Detects inappropriate content bytes within a Web page before it is returned to the user, and redirecting to this error page Imposes no limit on the size of the transferred HTTP data
* Is compatible with all major browsers (e.g. Internet Explorer, Mozilla Firefox, Google Chrome, etc.) without the requirement to tweak any advanced feature
Allows the user to select the proxy port, default is 8000
Is smart in selection of what HTTP content should be searched for the forbidden keywords.
Requirements

Python 3
Git
Linux terminal emulator
Webbrowser with customable http port
Installation

This is a Linux program. It has only been tested in Elementary and ubuntu bash for windows 10. If using with other operationg systems program relaiablility can not be guaranteed.

Get source files "git clone git@github.com:NetBros/TDTS06.git"
Change directory to the folder where the proxy server is located "cd TDTS06/Lab2"
Make the server executable "chmod +x simple_proxy.py"
How to run?

Configure a web browser to listen to a specific port.
Run by "./simple_proxy.py"
Browse your browser
Features

Custom port "./simple_proxy.py 8433" changes the port the server listens to from 8000 to 8433
we do not support posting.

## Testing

The server can not handle https requests in the regard that https requests are not sent through the server.
Example webpages that works

http://www.ida.liu.se/~TDTS04/labs/2011/ass2/goodtest1.txt http://www.ida.liu.se/~TDTS04/labs/2011/ass2/goodtest2.html http://www.ida.liu.se/~TDTS04/labs/2011/ass2/SpongeBob.html http://www.ida.liu.se/~TDTS04/labs/2011/ass2/SpongeBob.html http://www.ida.liu.se/~TDTS04/labs/2011/ass2/badtest1.html http://www.stackoverflow.com/ http://www.aftonbladet.se/ http://www.svd.se/ http://www.liu.se/ http://www.qz.com/ http://www.bbc.com/
Examples of webpages that don't work

http://www.dailymotion.com/
Features maped to code

Feature 2 simple get request
conn, addr = server_socket.accept()
byte_get_request = self.conn.recv(self.BUFFER_SIZE)
server_request = client_socket.recv(BUFFER_SIZE)
self.conn.send(server_request)
Feature 3 Block url
def check_ban(data,usage,ban_list):
data = data.lower()
data = data.strip()
for word in ban_list:
if(not -1 == data.find(word)):
raise My_Error(usage,word)


try:
check_ban(get_dict["GET"],1,self.ban_list)
except My_Error as e:
print("[!] ERROR found ",e.word," in url, redirecting")
get_dict["Host"] = "www.ida.liu.se"
temp_get = get_dict["GET"].split(" ")
get_dict["GET"] = "http://www.ida.liu.se/~TDTS04/labs/2011/ass2/error1.html" + " " + temp_get[1]
Feature 7 custom port
if len(sys.argv) > 1:
PORT = sys.argv[1]
else:
PORT = 8000
Feature 8 smart body search
TYPE_FLAGG = 0
ENCODING_FLAGG = 0
for key in header_dict:
if key == "Content-Type":
TYPE_FLAGG = 1
if TYPE_FLAGG:
if not -1 == header_dict["Content-Type"].find("text/html"):
