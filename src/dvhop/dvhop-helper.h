#include "ns3/core-module.h"
#include "ns3/csma-module.h"
#include "ns3/applications-module.h"
#include "ns3/internet-module.h"
#include <tuple>

namespace ns3{
    namespace dvhop{
        class DVHopHelper : public UdpEchoClientHelper
        {
        public:
            // Constructor for dv hop algorithm
            DVHopHelper(int port);

            // sets position of node
            void SetPosition(double x, double y);

            // Gets position of node 
            double GetXPosition();
            double GetYPosition();

            // Gets location status of node
            bool GetLocationStatus();

            // provide
        private: 
            //
            bool positionKnown = false; 
            double mPositionX = 0;
            double mPositionY = 0;
        };
    }
    
}