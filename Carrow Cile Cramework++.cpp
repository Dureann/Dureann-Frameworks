//Carrow Cile Cramework++
//include statements
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

std::vector<std::string> zonerow1;
std::vector<std::string> zonerow2;
std::vector<std::string> zonerow3;
std::vector<std::string> zonerow4;
std::vector<std::string> zonerow5;

int pyc = 0;
int pxc = 0;

std::string player = "XX";
std::string treetile = "⸙⸙";
std::string pathtile = "░░";

//function definitions
void forestpath () {
  zonerow1.clear(); zonerow2.clear(); zonerow3.clear(); zonerow4.clear(); zonerow5.clear(); 
  zonerow2.push_back(treetile); zonerow2.push_back(treetile); zonerow2.push_back(pathtile); zonerow2.push_back(treetile); zonerow2.push_back(treetile);
  zonerow2.push_back(treetile); zonerow2.push_back(treetile); zonerow2.push_back(pathtile); zonerow2.push_back(treetile); zonerow2.push_back(treetile);
  zonerow3.push_back(treetile); zonerow3.push_back(treetile); zonerow3.push_back(pathtile); zonerow3.push_back(treetile); zonerow3.push_back(treetile);
  zonerow4.push_back(treetile); zonerow4.push_back(treetile); zonerow4.push_back(pathtile); zonerow4.push_back(treetile); zonerow4.push_back(treetile);
  zonerow5.push_back(treetile); zonerow5.push_back(treetile); zonerow5.push_back(pathtile); zonerow5.push_back(treetile); zonerow5.push_back(treetile);
}
//main function
int main() { 
  forestpath();
  for (int i = 0; i < 5; i++) {
    std::cout << zonerow1[i];
  }
}
