import javax.swing.*;

public class RouterNode {
  private int myID;
  private GuiTextArea myGUI;
  private RouterSimulator sim;
  private int[] costs = new int[RouterSimulator.NUM_NODES];
  private int[] myCosts;
  private int totalNodes;
  private int[] myForward;

  //--------------------------------------------------
  public RouterNode(int ID, RouterSimulator sim, int[] costs) {
    myCosts = costs;
    totalNodes = RouterSimulator.NUM_NODES;
    myForward = new int[totalNodes*2];
    for(int i=0; i<totalNodes; i++)
    {
      myForward[i+totalNodes] = costs[i];
      if (myCosts[i] == 999)
        myForward[i] = 999;
      else
        myForward[i] = i;
    }

    myID = ID;
    this.sim = sim;
    myGUI =new GuiTextArea("  Output window for Router #"+ ID + "  ");
    sendUpdate();
    System.arraycopy(costs, 0, this.costs, 0, RouterSimulator.NUM_NODES);
  }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
    myGUI.println("recv update");
  // recive info about the connecting neighbours
  boolean forwardFlagg = false;
  for (int i=0; i< totalNodes ; i++){
      int costToRoute = myForward[pkt.sourceid+totalNodes]+pkt.mincost[i+totalNodes];
      if (myForward[i+totalNodes]>costToRoute){
        if(myForward[pkt.sourceid] == pkt.sourceid){
          myForward[i] = pkt.sourceid;
        }
          myForward[i] = myForward[pkt.sourceid];
        myForward[i+totalNodes] = costToRoute;
        forwardFlagg = true;
      }
    }
// updating myForward depending on RouterPacket mincost
  if(forwardFlagg){
    sendUpdate();
  }

  }


  //--------------------------------------------------
  private void sendUpdate() {
    myGUI.println("send update");
    for (int i = 0;i<totalNodes ;i++ ) {
      if ((costs[i] != 999 ) && (i != myID)) {
        RouterPacket myPacket = new RouterPacket(myID,i,myForward);
        myPacket.mincost = myForward;
        sim.toLayer2(myPacket);
      }
    }
    //Update RouterPacket mincost with help from updated myForward
  }


  //--------------------------------------------------
  public void printDistanceTable() {
  //Print the info about info we know about network so far
	  myGUI.println("Current table for " + myID +
			"  at time " + sim.getClocktime());
    for (int i = 0;i<totalNodes ;i++ ) {
      myGUI.println("Fastest route to " + i + " is through " +myForward[i] + " with cost " + myForward[i+totalNodes]);
    }
  }

  //--------------------------------------------------
  public void updateLinkCost(int dest, int newcost) {

    myGUI.println("updateLinkCost");
    costs[dest] = newcost;
  // recive info about the connecting neighbours
    bool forwardFlagg = false;
    int oldCost = myForward[dest+totalNodes];
    if(newcost < oldCost){
      myForward[dest] = dest;
      myForward[dest+totalNodes] = newcost;
      forwardFlagg = true;
    }
    // updating myForward depending on RouterPacket mincost
  if(forwardFlagg){
    sendUpdate();
  }
  }

}
