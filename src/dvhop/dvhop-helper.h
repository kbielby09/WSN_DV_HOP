#include "ns3/core-module.h"
#include "ns3/csma-module.h"
#include "ns3/applications-module.h"
#include "ns3/internet-module.h"
#include <tuple>

namespace ns3{
        class DVHopHelper : public UdpEchoClientHelper
        {
        public:
            // Constructor for dv hop algorithm
            DVHopHelper(Address addr, uint16_t port);

            // sets position of node
            void SetPosition(double x, double y);

            // Gets position of node 
            double GetXPosition();
            double GetYPosition();

            // Gets location status of node
            bool GetLocationStatus();

            // trilaterates node in topology


            // provide
        private: 
            
            bool positionKnown = false;        // boolean variable used to set if anchor node
            double mPositionX = 0;             // x value of grid poisition of node
            double mPositionY = 0;             // y value of grid position of node
            double mAverageHopDistance = 5.7;  // The average hop size of the given node. 
        };
    
}