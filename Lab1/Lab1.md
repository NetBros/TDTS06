# TDST06, Lab 1
## alepo020, miljo274
## Labborations assistent Hans-Filip Elo

1. Is your browser running HTTP version 1.0 or 1.1? What version of HTTP is the server running?
 * 1.1 
2. What languages (if any) does your browser indicate that it can accept to the server? In the captured session, what other information (if any) does the browser provide the server with regarding the user/browser?
 * text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
 * en,en-GB;q=0.8
3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?
  * Me (Source:) 130.236.77.55
  * Server (Destination:) 128.119.245.12
4. What is the status code returned from the server to your browser?
  * 304 "not modified"
5. When was the HTML file that you are retrieving last modified at the server?
  * If-Modified-Since: Wed, 31 Aug 2016 05:59:01 GMT\r\n
6. How many bytes of content are being returned to your browser?
  * Frame 3: 502 bytes on wire (4016 bits), 502 bytes captured (4016 bits) on interface 0
7. By inspecting the raw data in the "packet bytes" pane, do you see any http headers within the data that are not displayed in the "packet details" pane? If so, name one.
 * Nej
8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
 * Nej
9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?
 * Första 200 för ok och andra 304 för "not modified"
10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET? If so, what information follows the “IF-MODIFIED-SINCE:” header?
 * If-Modified-Since: Wed, 31 Aug 2016 05:59:01 GMT\r\n
11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.
 * 304 "not modified"
12. How many HTTP GET request messages were sent by your browser?
 * 1
13. How many data-containing TCP segments were needed to carry the single HTTP response?
 * 4
14. What is the status code and phrase associated with the response to the HTTP GET request?
 * 200 "OK"
15. Is there any HTTP header information in the transmitted data associated with TCP segmentation? For this question you may want to think about at what layer each protocol operates, and how the protocols at the different layers interoperate
 * Det finns information om IP-adress och vilken port den ska till.
16. How many HTTP GET request messages were sent by your browser? To which Internet addresses were these GET requests sent?
 * 2 get requests till en en IP-adress och två till en annan.
17. Can you tell whether your browser downloaded the two images serially, or whether they were downloaded from the two web sites in parallel? Explain.
 * Seriellt då nedladningarna är i två olika get-requests och börjar vid olika tidpunkter.

18. What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?
 * 401 "Unauthorized"
19. When your browser sends the HTTP GET message for the second time, what new field is included in the HTTP GET message?
 * Authorization

20. What does the "Connection: close" and "Connection: Keep-alive" header field imply in HTTP protocol? When should one be used over the other?
 * Skillnaden i connection close och connection keep-alive verkar vara att connection close görs efter något hämtas från en en annan    server än den man besöker så som en bild eller fil som finns på den sidan man besöker. Connection keep-alvie är på den sidan man     besöker.

# Summary part A
Första kollade vi lite grundläggande och kollade på IP-adresser. Lärde sig lite om HTTP , vad varje del av GET var och vad för information som fanns i varje subdel.
# Summary part B
Andra delen kollade vi på två HTTP-requests efter varandra och jämförde dem , vad som skillde sig och varför. Till exempel så hämta den inte hem en fil om den redan fanns i cashen.
# Summary part C
Tredje delen så kollade vi på TCP-kommunikationen och se att meddelandet och hämtningen delades upp i flera små segment.
# Summary part D
I fjärde delen så kollar vi på hur det görs när bilder på en sida måste hämtas från andra sidor.
# Summary part E
Femte delen så kollar vad som händer när en hemsida är lösenordsskyddad vad som skickas i get-request mm.
# Summary part E+
Connection close kommer användas då en sida som enligt uppgift inte får hämtas, istället för att ladda in sidan så används connection close. Sidor som är godkände ska då tsället ha connection keep-alive. 



