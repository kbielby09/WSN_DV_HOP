import random
import math
import numpy
import matplotlib.pyplot as plt

maxiumumHopDistance = 20
averageHopSize      = 15

class Node:
    def __init__(self, x, y, name):
        self.isBeacon = False
        self.isContamination = False
        self.isDead = False
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

    def setAsContamination(self):
        self.isContamination = True

    def getContamination(self):
        return self.isContamination

    def setAsDead(self):
        self.isDead = True

    def getDead(self):
        return self.isDead

    def sendHopMessage(self, Node, breaconName, beaconPosition, hopCount):
        print(self.getName(), " sending hop message")

        Node.receiveHopMessage(beaconName, beaconPosition, hopCount)
    

    def receiveHopMessage(self, nodeName, position, hopCount):
        print(self.getName(), " receiving hop message from ", nodeName)

        # add node to hop table
        self.DistanceTable[nodeName] = (position, hopCount)

        # display distance table test
        print(self.getName(), " distance table: ", self.DistanceTable)


        # self.trilaterate()


def find(vector,value,operator):
    indicies = [] 
    for i in range(0,len(vector)):
        if operator == "g":
            if(vector[i] > value):
                indicies = indicies + [i]
        elif operator == "l":
            if(vector[i] < value):
                indicies = indicies + [i]
    return indicies

def NodeInRange(SendNode, ReceiveNode):
    # get actual distance to receiving node
    recvPosition = ReceiveNode.getPosition()

    sendPosition = SendNode.getPosition()

    # check if receiving node is within range
    recvDistance = math.sqrt(math.pow((sendPosition[0] - recvPosition[0]), 2) + 
                   math.pow((sendPosition[1] - recvPosition[1]), 2)) 

    if recvDistance <= maxiumumHopDistance:
        return True

    return False

    
if __name__ == "__main__":
    NodeList = []
    numNodes = 100

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

    # perform dvhop starting with beacon nodes
    for SendNode in NodeList:
        hopCount = 0

        # check if node is beacon
        if SendNode.getBeacon():
            beaconName     = SendNode.getName()
            beaconPosition = SendNode.getPosition()
            # send hop message to all nodes in network
            for ReceiveNode in NodeList:
                if SendNode.getName() == ReceiveNode.getName():
                    continue
                else:
                    # send message to all nodes in network
                    
                    if NodeInRange(SendNode, ReceiveNode):
                        hopCount += 1
                        SendNode.sendHopMessage(ReceiveNode, beaconName, beaconPosition, hopCount)
                        SendNode = ReceiveNode
            
        else:
            # send hop message 
            print("TODO")


    # check node List
    # for Node in NodeList:
    #     print("Node: ", Node.getName(), " Position: ", Node.getPosition()[0], " ", Node.getPosition()[1], " is Beacon: ", Node.getBeacon())

    # numContaminations = 1
    # contaminationList = []
    # for i in range(0,numContaminations):

    #     nodeName = "Contamination 1" + str(i)
    #     xPos = random.randint(1, 100)
    #     yPos = random.randint(1, 100)

    #     contNode = Node(xPos, yPos, nodeName)
    #     contNode.setAsContamination()

    #     contaminationList.append(contNode)

    # # check node List
    # for Node in contaminationList:
    #     print("Node: ", Node.getName(), " Position: ", Node.getPosition()[0], " ", Node.getPosition()[1], " is Beacon: ", Node.getBeacon()," is Contamination: ", Node.getContamination())

    # # Create Wienbull PDF #
    # alpha = 5.40347  # Parameter alpha
    # beta = 1.57327  # Parameter beta
    # delta = 0.01  # The amount of change
    # d = numpy.arange(0,3,delta)  # dose
    # # Compute pdf
    # f = [0] * len(d) 
    # for i in range(0,len(d)):
    #     f[i] = alpha * pow(1/beta,alpha) * pow(d[i],(alpha - 1)) * math.exp(-1*pow((d[i] / beta),alpha)) 
    # # Create Wienbull PDF #

    # nodeRadDist = [0.0]*numNodes
    # iter = 0
    # for Node in NodeList:
    #     xPos,yPos = Node.getPosition()
    #     contXPos,contYPos = contaminationList[0].getPosition()
    #     # Calculate radius to radiation source from each node
    #     nodeRadDist[iter] = math.sqrt(pow((xPos - contXPos),2) + pow((yPos - contYPos),2)) 
    #     if(nodeRadDist[iter] == 0):
    #         nodeRadDist[iter] = 0.01
    #     iter += 1

    # # Establish the node rate and a vector for the cumulative radiation does
    # # and node status (0 -> alive, 1 -> dead
    # doseRate = numpy.divide(2*1e-2,numpy.square(nodeRadDist)) 
    # doseTotal = [0.0] * numNodes 
    # nodeStatus = [0] * numNodes 
    # iter = 0
    # for Node in NodeList:
    #     if Node.getDead():
    #         nodeStatus[iter] = 1 
    #     else:
    #         nodeStatus[iter] = 0 
    #     iter += 1

    # # Sample the status of nodes every update rate
    # updateRate = 1 
    # simulationTime = 14 * 3600 
    # for t in range(0,simulationTime,updateRate):
    #     # Check all living nodes
    #     for i in find(nodeStatus,1,"l"):
    #         # Calculate total dosage received
    #         dExp = int(min(round(doseTotal[i]*100),len(f))) 
    #         # Integrate over Weibull pdf for cumulative probability of node
    #         # death
    #         cumulativeProbDead = sum(f[0:dExp + 1])*delta 
    #         # Flip a weighted coin based on weibull cdf for death
    #         if(cumulativeProbDead > numpy.random.uniform(0,1)):
    #             nodeStatus[i] = 1 
    #             NodeList[i].setAsDead()
    #     # Add to the dose totl for the next iteration
    #     doseTotal = numpy.add(doseTotal,numpy.multiply(updateRate,doseRate)) 
    #     plt.cla()
    #     for Node in NodeList:
    #         xPos,yPos = Node.getPosition()
    #         if Node.getDead():
    #             sym = 'x'
    #             color = 'k'
    #         elif Node.getBeacon():
    #             sym = '*'
    #             color = 'b'
    #         else:
    #             sym = 'o'
    #             color = 'g'
    #         plt.scatter(xPos,yPos,marker = sym,color=color) 
    #     for contam in contaminationList:
    #         xPos,yPos = contam.getPosition()
    #         plt.scatter(xPos,yPos,marker = '2',color='m') 
    #     #plt(x_nodes[find(node_status,1,"l")],y_nodes[find(node_status,1,"l")],linestyle='o') 
    #     #plt(x_radiation_points,y_radiation_points,linestyle,'o') 
    #     #plt(x_nodes[find(node_status,0,"g")],y_nodes[find(node_status,0,"g")],linestyle='x') 
    #     plt.show(block = False)
    #     plt.pause(0.001)

