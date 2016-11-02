import javax.swing.*;

public class RouterNode {
  private int myID;
  private GuiTextArea myGUI;
  private RouterSimulator sim;
  private int[] costs = new int[RouterSimulator.NUM_NODES];
  private int totalNodes;
  private int[][] myForwardTable = new int[RouterSimulator.NUM_NODES][RouterSimulator.NUM_NODES];
  private int[] myForwardVia = new int[RouterSimulator.NUM_NODES];

  //--------------------------------------------------
  public RouterNode(int ID, RouterSimulator sim, int[] costs) {
    totalNodes = RouterSimulator.NUM_NODES;
    myID = ID;
    this.sim = sim;
    myGUI =new GuiTextArea("  Output window for Router #"+ ID + "  ");
    System.arraycopy(costs, 0, this.costs, 0, RouterSimulator.NUM_NODES);
    for (int col=0;col<totalNodes ;col++ ) {
      for (int row=0;row<totalNodes ;row++ ) {
        if (row == col) {
          myForwardTable[row][col] = 0;
        }
        else if (row == myID) {
          myForwardTable[row][col] = 999;
        }
        else if (col == myID ){
          myForwardTable[row][col] = costs[row];
        }
        else{
          myForwardTable[row][col] = 999;
        }
        if (myForwardTable[row][myID]<999) {
            myForwardVia[row] = row;
        }
        else{
          myForwardVia[row] = 999;
        }
      }

      }
      update(false);
      sendUpdate();
    }
    
    //----------------------------------------
  private boolean update(boolean linkChange){
    boolean updated = false;
     for (int nodeWeWant2=0;nodeWeWant2<totalNodes ;nodeWeWant2++ ) {
	 if(nodeWeWant2 != myID){
	     int old_cost = myForwardTable[nodeWeWant2][myID];
	     int old_node = myForwardVia[nodeWeWant2];
	     int new_cost_temp =  999;
	     int new_route_temp = old_node;
	     for (int nodeWeWant3=0;nodeWeWant3<totalNodes ;nodeWeWant3++ ) { 
		 if((myForwardVia[nodeWeWant3]<999) && (nodeWeWant3 != myID)){
		     int cost2forwardNode = costs[myForwardVia[nodeWeWant3]];
		     int costFromForward2node = myForwardTable[nodeWeWant2][myForwardVia[nodeWeWant3]];
		     int new_cost = cost2forwardNode + costFromForward2node;
		     int route = nodeWeWant3;
		     if(new_cost<new_cost_temp){
			 new_cost_temp = new_cost;
			 new_route_temp = myForwardVia[route];
		     }
		 }
	     }

	     // is there a cheaper way to noode we want through with alternative route?
	     int temp3 = 999;
	     int temp4 = 0;
	     for(int i= 0;i<totalNodes;i++){
		 if(i!=myID){
		 int temp1 = costs[i];
		 int temp2 = myForwardTable[nodeWeWant2][i];
		 if((temp1+temp2)<temp3){
		     temp3 = temp1+temp2;
		     temp4=i;
		 }
		 }
	     }
	     if(temp3<new_cost_temp){
		 new_cost_temp = temp3;
		 new_route_temp = temp4;
	     }
	     
	     if ((new_cost_temp!=old_cost) || ((new_cost_temp<999)&&(old_node == 999))) {
		 myGUI.println("Updating cost");
		 updated = true;
		 old_cost = new_cost_temp;
		 old_node = new_route_temp;
	     }
	     myForwardTable[nodeWeWant2][myID] = old_cost;
	     myForwardVia[nodeWeWant2] = old_node;
	 }
    }
    return (updated || linkChange);
    }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
    myGUI.println("recv update");
    // updating myForward depending on RouterPacket mincost
    for (int node=0;node<totalNodes ;node++ ) {
     myForwardTable[node][pkt.sourceid] = pkt.mincost[node];
    }
  if(update(false)){
    sendUpdate();
  }
  }


  //--------------------------------------------------
  private void sendUpdate() {
  myGUI.println("send update");
    for (int nodeWeWant2=0;nodeWeWant2<totalNodes ;nodeWeWant2++ ) {
      if((costs[nodeWeWant2] != 999) && (nodeWeWant2 != myID)){
        int[] myMinCost = new int[totalNodes];
        for (int node=0;node<totalNodes ;node++ ) {
	    if((myForwardVia[node] == nodeWeWant2) && true){
            myMinCost[node] = 999;
          }
          else{
            myMinCost[node] = myForwardTable[node][myID];
          }
        }
        RouterPacket myPacket = new RouterPacket(myID,nodeWeWant2,myMinCost);
        sim.toLayer2(myPacket);
      }
    }

    }
    //Update RouterPacket mincost with help from updated myForward


  //--------------------------------------------------

  public void printDistanceTable() {
  	  myGUI.println("Current table for " + myID +
  			"  at time " + sim.getClocktime());

      String toPrint;

      myGUI.println("\nDistancetable:");
      printHeader();
      toPrint = "\tcost\t|";
      for (int j = 0;j<totalNodes ;j++ ) {
        for(int i=0; i<RouterSimulator.NUM_NODES; i++){
          toPrint += "\t" + myForwardTable[j][i];
        }
        toPrint += "\n\t\t|";
      }
      myGUI.println(toPrint);

      myGUI.println("\nOur distance vector and routes:");
      printHeader();
      toPrint = "\tcost\t|";
      for(int i=0; i<RouterSimulator.NUM_NODES; i++){
        toPrint += "\t" + myForwardTable[i][myID];
      }
      myGUI.println(toPrint);

      toPrint = "\troute\t|";
      for(int i=0; i<RouterSimulator.NUM_NODES; i++){
        if(myForwardVia[i] == RouterSimulator.INFINITY){
          toPrint += "\t-";
        }else{
          toPrint += "\t" + myForwardVia[i];
        }
      }
      myGUI.println(toPrint);
    }

  //---------------help fuction to clean up print code -----------
    private void printHeader() {
      String toPrint;
      toPrint = "\tdst\t|";
      for(int i=0; i<RouterSimulator.NUM_NODES; i++){
        toPrint += "\t" + i;
      }
      myGUI.println(toPrint);
      toPrint = printLine(45 + 23*RouterSimulator.NUM_NODES);
      myGUI.println(toPrint);

    }
    //---------help to print -----------------

    private String printLine(int num){
      String toPrint = "";
      for(int i=0; i<num; i++){
        toPrint += "-";
      }
      return toPrint;
    }

  //--------------------------------------------------
  public void updateLinkCost(int dest, int newcost) {
    myGUI.println("updating LinkCost");
    for (int i=0;i<totalNodes ;i++ ) {
	if (myForwardVia[i]==dest){
	    myForwardTable[i][myID]+= (newcost-costs[dest]);
      }
    }
    costs[dest] = newcost;
    if(update(true)){
	sendUpdate();
    }
  }
}
