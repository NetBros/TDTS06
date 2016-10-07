import javax.swing.*;

public class RouterNode {
  private int myID;
  private GuiTextArea myGUI;
  private RouterSimulator sim;
  private int[] costs = new int[RouterSimulator.NUM_NODES];

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

    System.arraycopy(costs, 0, this.costs, 0, RouterSimulator.NUM_NODES);

  }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
  // recive info about the connecting neighbours
  for (int i=0; i< totalNodes ; i++)
    {
      costToRoute = myForward[pkt.sourceid+totalNodes]+pkt.mincosts[i+totalNodes];
      if (myForward[i+totalNodes]>(costToRoute){
        myForward[i] = pkt.sourceid;
        myForward[i+totalNodes] = costToRoute;
      }
    }
// updating myForward depending on RouterPacket mincost

  }


  //--------------------------------------------------
  private void sendUpdate(RouterPacket pkt) {
    pkt.mincosts = myForward;
    sim.toLayer2(pkt);
    //Update RouterPacket mincost with help from updated myForward
  }


  //--------------------------------------------------
  public void printDistanceTable() {
  //Print the info about info we know about network so far
	  myGUI.println("Current table for " + myID +
			"  at time " + sim.getClocktime() + myForward);
  }

  //--------------------------------------------------
  public void updateLinkCost(int dest, int newcost) {
  }

}
