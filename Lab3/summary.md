## Summary 1-12 
TCP is a way for two computers to comunicate over a network. The first thing that happens is a handshake. Then packet transmission is started. The window size depends on packadge loss, buffer size at the reciver and sender aswell as congestion avoidance. Transmission starts with slow start and after a threshold it increases linearly. It increases untill buffersizes are met or untill packadge loss accurs.

RTT determines how fast we can send more packadges. High RTT means that we ahve to wait a long time to send new packadges since we might fill upp the reciver bufffer if we send them to quickly even if we have a high windows size and low congestion. 
