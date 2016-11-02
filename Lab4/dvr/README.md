# Lab 4 Distance Vector Routing
  1. Distance vector routing protocoll handles packages to take the cheapest route in a network of routers. To do this it takes the information it has from
from its neighbours and makes a table from the information. When packeges goes thourgh the network the table for every node updates with the 
information from its neighbours, with updated tables from its neighbours the node knows which node it is gonna route through to get to the node it wants to
by the cheapest price.
  2.  We implemented the table for the cost for every node and the routing-table where the routing to the other nodes where. We also 
implemented poisson reverse by sending that the cost was the infinyty to all the neighbours and the nodes going through the neighbours.

  3. If a route has more then 2 hops to come to a node poission reverse may fail, in this case it can create in some cases a infinite loop
anyways.
  4 To prevent this you can use Split Horizon whisch is prohibiting a router from advertising a route back onto the interface from which it was learned.
Other ways is to have a timeout , meaby not the most effecive way, but can solve the problem.. But the most coomon way to solve the problem
is to not use distance vector routing in large system, only in routing between big networks.

## References
  https://en.wikipedia.org/wiki/Split_horizon_route_advertisement
  
