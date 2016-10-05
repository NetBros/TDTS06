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
    //myForward = zero to me, cost to known and inf to others
    myID = ID;
    this.sim = sim;
    myGUI =new GuiTextArea("  Output window for Router #"+ ID + "  ");

    System.arraycopy(costs, 0, this.costs, 0, RouterSimulator.NUM_NODES);

  }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
  // recive info about the connecting neighbours

// updating myForward depending on RouterPacket mincost

  }


  //--------------------------------------------------
  private void sendUpdate(RouterPacket pkt) {
    sim.toLayer2(pkt);
    //Update RouterPacket mincost with help from updated myForward
  }


  //--------------------------------------------------
  public void printDistanceTable() {
  //Print the info about info we know about network so far
	  myGUI.println("Current table for " + myID +
			"  at time " + sim.getClocktime());
  }

  //--------------------------------------------------
  public void updateLinkCost(int dest, int newcost) {
  }

}
