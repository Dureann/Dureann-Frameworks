#MARROW Tile Framework 
#Init, imports, vars
import random
import time
pyc = 0
pxc = 0
zonerow1 = []
zonerow2 = []
zonerow3 = []
zonerow4 = []
zonerow5 = []
#Tiles and entities
player = "XX"
treetile = "⸙⸙"
snowtile = "❅❅"
pathtile = "░░"

def forestpath():
  zonerow1.clear(); zonerow2.clear(); zonerow3.clear(); zonerow4.clear(); zonerow5.clear();
  zonerow1.append(treetile); zonerow1.append(treetile); zonerow1.append(pathtile); zonerow1.append(treetile); zonerow1.append(treetile)
  zonerow2.append(treetile); zonerow2.append(treetile); zonerow2.append(pathtile); zonerow2.append(treetile); zonerow2.append(treetile)
  zonerow3.append(treetile); zonerow3.append(treetile); zonerow3.append(pathtile); zonerow3.append(treetile); zonerow3.append(treetile)
  zonerow4.append(treetile); zonerow4.append(treetile); zonerow4.append(pathtile); zonerow4.append(treetile); zonerow4.append(treetile)
  zonerow5.append(treetile); zonerow5.append(treetile); zonerow5.append(pathtile); zonerow5.append(treetile); zonerow5.append(treetile)

forestpath()

while 1==1:
  
  print(zonerow1[0] + zonerow1[1] + zonerow1[2] + zonerow1[3] + zonerow1[4])
  print(zonerow2[0] + zonerow2[1] + zonerow2[2] + zonerow2[3] + zonerow2[4])
  print(zonerow3[0] + zonerow3[1] + zonerow3[2] + zonerow3[3] + zonerow3[4])
  print(zonerow4[0] + zonerow4[1] + zonerow4[2] + zonerow4[3] + zonerow4[4])
  print(zonerow5[0] + zonerow5[1] + zonerow5[2] + zonerow5[3] + zonerow5[4])
  
  action = input("Move/Act: ")
  if (action == "w"):
    pyc = pyc - 1
  elif (action == "a"):
    pxc = pxc - 1
  elif (action == "s"):
    pyc = pyc + 1
  elif (action == "d"):
    pxc = pxc + 1
  else:
    print("action or movement not recognized")
    time.sleep(1.5)
    continue
  
  if pyc == 0:
    forestpath()
    zonerow1.pop(pxc)
    zonerow1.insert((int(pxc)), player)
  if pyc == 1:
    forestpath()
    zonerow2.pop(pxc)
    zonerow2.insert((int(pxc)), player)
  if pyc == 2:
    forestpath()
    zonerow3.pop(pxc)
    zonerow3.insert((int(pxc)), player)
  if pyc == 3:
    forestpath()
    zonerow4.pop(pxc)
    zonerow4.insert((int(pxc)), player)
  if pyc == 4:
    forestpath()
    zonerow5.pop(pxc)
    zonerow5.insert((int(pxc)), player)
  # if pyc == 5:
  #   forestpath()
  #   zonerow5.pop(pxc)
  #   zonerow5.insert((int(pxc - 1)), player)
  #   pyc = pyc - 1
