import random


maxiumumHopDistance = 100

class Node:
    def __init__(self, x, y, name):
        self.isBeacon = False
        self.Position = (x, y)
        self.nodeName = name
        self.localizedPosition = (0, 0)
        self.DistanceTable = {}

        print("Initializing")

    def addBeaconPosition(self, beaconPosition, beaconName):
        print("adding Beacon")

    # def trilaterate(self):
    #     if not(self.)

    def getName(self):
        return self.nodeName

    def getPosition(self):
        return self.Position

    def setAsBeacon(self):
        self.isBeacon = True

    def getBeacon(self):
        return self.isBeacon



    
if __name__ == "__main__":
    NodeList = []

    # create 100 nodes with random positions in 100x100 grid
    for i in range(0, 100): 
        nodeName = "node " + str(i) 
        xPos = random.randint(1, 100)
        yPos = random.randint(1, 100)

        NodeList.append(Node(xPos, yPos, nodeName))

    # generate 10 random beacons for nodes
    for i in range(0, 10):
        randomIndex = random.randint(0, len(NodeList))  # get random index of node list

        NodeList[randomIndex].setAsBeacon()

    # check node List
    for Node in NodeList:
        print("Node: ", Node.getName(), " Position: ", Node.getPosition()[0], " ", Node.getPosition()[1], " is Beacon: ", Node.getBeacon())
