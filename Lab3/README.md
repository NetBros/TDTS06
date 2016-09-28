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
 * When was the ACK for each segment received?
   * [566; 0.0539], [2026; 0.0772], [3486; 0.1240], [4946; 0.1691], [6406; 0.2172], [7866; 0.2678]
 * Given the difference between when each TCP segment was sent, and when its acknowledgement was received, what is the RTT value for each of the six segments?
   * [0.0274], [0.0355], [0.07], [0.1145], [0.1398], [0.1896]
 * What is the EstimatedRTT value (see page 277 in text) after the receipt of each ACK? Assume that the value of the EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 277 for all subsequent segments.
   * [0.0274, 0.0274, 0.0284125, 0.0336109375, 0.0437220703125, 0.05573181152343751, 0.07246533508300781]
8. What is the length of each of the first six TCP segments?
 * [565 1460 1460 1460 1460 1460]
9. What is the minimum amount of available buffer space advertised at the receiver for the entire trace?
    * 5840
 * Does the lack of receiver buffer space ever throttle the sender?
   * Yes, after packadge 31237 the buffer is stagnant and can't increase more 
10. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?
 * No, we checked so that all bytes where transmitted in order
11. How much data does the receiver typically acknowledge in an ACK? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 on page 285 in the text).
 * 1460
 * Yes, No 162-170 is a clear example of this
12. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.
 * 64Kb/s througput = (sender window size)/RTT
13. Use the Time-Sequence-Graph (Stevens) plotting tool to view the sequence number versus time plot of segments being sent from the client to the server (Figure 2a and Figure 2b). For each of the two traces, can you identify where TCP's slow start phase begins and ends, and where congestion avoidance takes over? If you can, explain how. If not, explain why not. To better identify these phases, you may need to find the number of unacknowledged packets (or bytes) at different times and plot the unacknowledged packets (y-axis) as a function of time (x-axis). Note that the number of unacknowledged packets at different times can be found by comparing the number of packets that have been sent with the number of packets that have been acknowledged. After plotting the number of unacknowledged packets versus time, comment on ways in which the measured data differs from the idealized behavior of TCP that we've studied in the text.
 * bka
14. Explain the relationship between (i) the congestion window, (ii) the receiver advertised window, (iii) the number of unacknowledged bytes, and (iv) the effective window at the sender.
 * bha
15. Is it generally possible to find the congestion window size (i.e. cwnd) and how it changes with time, from the captured trace files?If so, please explain how. If not, please explain when and when not. Motivate your answer and give examples. Your answer may also benefit from trying to describe and discuss your answer in the context of the two prior questions, for example.
 * hdj
 
