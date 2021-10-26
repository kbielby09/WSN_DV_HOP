#include "dvhop-helper.h"


// Constructor for dv hop algorithm
DVHopHelper::DVHopHelper(int port) {
    // Initialize node parameters
    positionKnown = false; 
    mPositionX = 0;
    mPositionY = 0; 
}

// sets position of node
void DVHopHelper::SetPosition(double x, double y) {
    positionKnown = true; 
    mPositionX = x;
    mPositionY = y; 
}

// get x value of the position
double DVHopHelper::GetXPosition() {
    return mPositionX;
}

// get y value of the node's position  
double DVHopHelper::GetYPosition() {
    return mPositionY;
}

// Gets location status of node
bool DVHopHelper::GetLocationStatus() {
    return positionKnown; 
}