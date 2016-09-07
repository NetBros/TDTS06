# Lab 2

This is a simple web proxy server writen in python which should have the following functionalities:

1. The proxy should support both HTTP/1.0 and HTTP/1.1.
2. Handles simple HTTP GET interactions between client and server
3. Blocks requests for undesirable URLs, using HTTP redirection to display this error page instead
4 .Detects inappropriate content bytes within a Web page before it is returned to the user, and redirecting to this error page
5. Imposes no limit on the size of the transferred HTTP data
6.Is compatible with all major browsers (e.g. Internet Explorer, Mozilla Firefox, Google Chrome, etc.) without the requirement to tweak any advanced feature
7. Allows the user to select the proxy port (i.e. the port number should not be hard coded)
8. Is smart in selection of what HTTP content should be searched for the forbidden keywords. For example, you probably agree that it is not wise to search inside compressed or other non-text-based HTTP content such as graphic files, etc.

## Preparation questions

