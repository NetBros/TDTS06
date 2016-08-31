# Lab 1

1. Is your browser running HTTP version 1.0 or 1.1? What version of HTTP is the server running?
 * 1.1 
2. What languages (if any) does your browser indicate that it can accept to the server? In the captured session, what other information (if any) does the browser provide the server with regarding the user/browser?
 * text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
 * en,en-GB;q=0.8
3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?
  * Me (Source:) 10.255.137.7
  * Server (Destination:) 128.119.245.12
4. What is the status code returned from the server to your browser?
  * We don't have one
5. When was the HTML file that you are retrieving last modified at the server?
  * If-Modified-Since: Wed, 31 Aug 2016 05:59:01 GMT\r\n
6. How many bytes of content are being returned to your browser?
  * 502 and 509 depending on computer
7. By inspecting the raw data in the "packet bytes" pane, do you see any http headers within the data that are not displayed in the "packet details" pane? If so, name one.
 * Nej
8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?
10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET? If so, what information follows the “IF-MODIFIED-SINCE:” header?
11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.



