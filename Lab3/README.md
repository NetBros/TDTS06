# Lab 3 
1. What are the first and last packets for the POST request?
  * Sequence number 1 first and 163769 is the last sequence number
2. What is the IP address and the TCP port used by the client computer (source) that is transferring the file to gaia.cs.umass.edu?
  * 192.168.1.102 ist the IP-adress of the sorce with port 1161
3. What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection?
  * 128.119.254.12 and Port 80
4. What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? What is it in the segment that identifies the segment as a SYN segment?
  * 0
5. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is the value of the ACKnowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value? What is it in the segment that identifies the segment as a SYNACK segment?
  * 0,1,
6. What is the sequence number of the TCP segment containing the HTTP POST command?
  * 164041
7. Consider the TCP segment containing the HTTP POST as the first segment in the TCP connection. What are the sequence numbers of the first six segments in the TCP connection (including the segment containing the HTTP POST)? At what time was each segment sent?
  * format [sequence nmb; time sent] [1; 0.0265], [566; 0.0417], [2026; 0.0540], [3486; 0.0546], [4946; 0.0774], [6406; 0.0782]
  * Time 0 == Aug 21, 2004 15:44:20.570381000
8. 
 * When was the ACK for each segment received?
  * [566; 0.0539], [2026; 0.0772], [3486; 0.1240], [4946; 0.1691], [6406; 0.2172], [7866; 0.2678]
 * Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments?
  * [0.0275], [0.0232], [0.0694], [0.0917], [0.1391]
 * What is the EstimatedRTT value (see page 277 in text) after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 277 for all subsequent segments.
9. What is the length of each of the first six TCP segments?
10. What is the minimum amount of available buffer space advertised at the receiver for the entire trace? Does the lack of receiver       buffer space ever throttle the sender?
11. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?
12. How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 on page 285 in the text).
13. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.
