# Lab 2

This is a simple web proxy server writen in python which should have the following functionalities:

1. The proxy should support both HTTP/1.0 and HTTP/1.1.
2. Handles simple HTTP GET interactions between client and server
3. Blocks requests for undesirable URLs, using HTTP redirection to display this error page instead
4. Detects inappropriate content bytes within a Web page before it is returned to the user, and redirecting to this error page
5. Imposes no limit on the size of the transferred HTTP data
6. Is compatible with all major browsers (e.g. Internet Explorer, Mozilla Firefox, Google Chrome, etc.) without the requirement to tweak any advanced feature
7. Allows the user to select the proxy port (i.e. the port number should not be hard coded)
8. Is smart in selection of what HTTP content should be searched for the forbidden keywords. For example, you probably agree that it is not wise to search inside compressed or other non-text-based HTTP content such as graphic files, etc.
9. (Optional) Supporting file upload using the POST method
10. You do not have to relay HTTPS requests through the proxy

## Preparation questions
* How will you transfer text data over a socket? How will you transfer binary data like image files over socket? You can assume the context of language that you plan to use for performing the assignment (i.e., c, c++, or java).
 * socket.send(data)?
* What does the "Connection: close" and "Connection: Keep-alive" header field imply in HTTP protocol. When should one be used over the other? [See question 20 in assignment 1.] For this question you may also want to go back to the traces used in assignment 1 and see if you can find either (or both) of these types of connections.
 * close så får vi all data, keep-alive måste vi ligga och vänta tills connection timar ut
* Consider the use of a proxy server, through which the client sends its request. Briefly explain (using a block diagram) the HTTP request-response interaction between a client, proxy, and server. Pay careful attention to the TCP port numbers as you will use a similar setup in this assignment. [See optional question 20 in assignment 21.]
 * [firefox]---->[server socket    [Proxy server]      client socket]---->[web server]
* Please outline a high-level algorithm that describes how you plan to implement your version of NetNinny.
  * Port = my_port
  * server_socket.listen(my_port)
  * 
