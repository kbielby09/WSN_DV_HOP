
#include <iostream>
#include <utility>
#include <fstream>
#include <sstream>
#include <math.h> 
#include <vector>
#include <cmath>

std::pair<double, double> nodes [3];
double avgHopSize = 10.5;

struct point 
{
    float x,y;
};

float norm (point p) // get the norm of a vector
{
    return pow(pow(p.x,2)+pow(p.y,2),.5);
}

point trilateration(point point1, point point2, point point3, double r1, double r2, double r3) {
    point resultPose;

    //unit vector in a direction from point1 to point from the average hop size
    double p2p1Distance = avgHopSize;
    point ex = {(point2.x-point1.x)/p2p1Distance, (point2.y-point1.y)/p2p1Distance};
    point aux = {point3.x-point1.x,point3.y-point1.y};

    //signed magnitude of the x component
    double i = ex.x * aux.x + ex.y * aux.y;

    //the unit vector in the y direction. 
    point aux2 = { point3.x-point1.x-i*ex.x, point3.y-point1.y-i*ex.y};
    point ey = { aux2.x / norm (aux2), aux2.y / norm (aux2) };

    //the signed magnitude of the y component
    double j = ey.x * aux.x + ey.y * aux.y;

    //coordinates
    double x = (pow(r1,2) - pow(r2,2) + pow(p2p1Distance,2))/ (2 * p2p1Distance);
    double y = (pow(r1,2) - pow(r3,2) + pow(i,2) + pow(j,2))/(2*j) - i*x/j;

    //result coordinates
    double finalX = point1.x+ x*ex.x + y*ey.x;
    double finalY = point1.y+ x*ex.y + y*ey.y;
    resultPose.x = finalX;
    resultPose.y = finalY;

    return resultPose;
}

int main(int argc, char *argv[]) {
    std::cout << "EE 407 Computer Networks" << std::endl;
    std::cout << "Professor: Yu Liu\n";
    std::cout << "Kyle Bielby, Joseph Morrison, Tarak Patel, and Josh Schiling\n";
    std::cout << "\n";
    std::cout << "DV HOP EXAMPLE" << std::endl;
    std::cout << "\n";

    point finalPose;  // final position calculated by trilateration

    // create node coordinates
    point p1 = {4.0,4.0};
    point p2 = {9.0,7.0};
    point p3 = {9.0,1.0};

    // display node coordinates
    std::cout << "node 1 corrdinates: x: " << p1.x << " y: " << p1.y << std::endl;
    std::cout << "node 2 corrdinates: x: " << p2.x << " y: " << p2.y << std::endl;
    std::cout << "node 3 corrdinates: x: " << p3.x << " y: " << p3.y << std::endl;
    std::cout << std::endl;

    // set radius from individual points
    double r1,r2,r3;
    r1 = avgHopSize;
    r2 = avgHopSize;
    r3 = avgHopSize;

    // Perform trilateration to find 
    finalPose = trilateration(p1,p2,p3,r1,r2,r3);
    std::cout <<"unknown node coordinates: X:::  " << finalPose.x << std::endl;
    std::cout << "unknown node coordinates: Y:::  " << finalPose.y << std::endl; 
    
}

void setCoordinates(double x, double y) {
    std::cout << "Creating pair" << std::endl;
    std::pair<double, double> node = std::make_pair(x, y);
}

