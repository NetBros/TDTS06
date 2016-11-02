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
      update();
      sendUpdate();
    }

  private boolean update(){
    boolean updated = false;
    for (int nodeWeWant2=0;nodeWeWant2<totalNodes ;nodeWeWant2++ ) {
      int old_cost = myForwardTable[nodeWeWant2][myID];
      int old_node = myForwardVia[nodeWeWant2];
      for (int nodeWeWant3=0;nodeWeWant3<totalNodes ;nodeWeWant3++ ) {
        if((myForwardVia[nodeWeWant3]<999) && (nodeWeWant3 != myID)){
          int cost2forwardNode = myForwardTable[myForwardVia[nodeWeWant3]][myID];
          int costFromForward2node = myForwardTable[nodeWeWant2][myForwardVia[nodeWeWant3]];
          int new_cost = cost2forwardNode + costFromForward2node;

          myGUI.println("Wewant2 " + nodeWeWant2 + "\tWewant3  " + nodeWeWant3 + "\tRoute "+ myForwardVia[nodeWeWant3]);
          myGUI.println("cost from " + myForwardVia[nodeWeWant3] + " to " + nodeWeWant2 +" is " + myForwardTable[nodeWeWant2][nodeWeWant3]);
          myGUI.println("cost from " + myID +" to " +myForwardVia[nodeWeWant3]+ " is " + myForwardTable[myForwardVia[nodeWeWant3]][myID]);
          myGUI.println("old_cost: "+old_cost);
          myGUI.println("new_cost: " +new_cost);
        if ((new_cost<old_cost) || ((new_cost<999)&&(old_node == 999))) {
          myGUI.println("Updating cost");
          updated = true;
          old_cost = new_cost;
          old_node = myForwardVia[nodeWeWant3];
        }
        }
      }
      myForwardTable[nodeWeWant2][myID] = old_cost;
      myForwardVia[nodeWeWant2] = old_node;
    }
    return updated;
    }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
    myGUI.println("recv update");
    // updating myForward depending on RouterPacket mincost
    for (int node=0;node<totalNodes ;node++ ) {
     myForwardTable[node][pkt.sourceid] = pkt.mincost[node];
    }
  if(update()){
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
          if(myForwardVia[node] == nodeWeWant2){
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
    for (int i=0;i<totalNodes ;i++ ) {
      if (myForwardVia[i]==dest)
        myForwardTable[dest][myID]+= (newcost-costs[dest]);
      }
    costs[dest] = newcost;
    sendUpdate();

}
}
