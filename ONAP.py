import random
import time

print('One Night At Phython')
input('press enter to start')
input('You can close door (front, right, left)')
input('You can watch CCTV but sometimes it broken')
input('Keep our battery while 6am')

battery = 100
Time = 0
time2 = 12
Commandy = 1
CommandyList = [3, 6, 8, 11, 13]
CommandyNum = 0
Hardy = 1
HardyList = [3, 4, 5, 7, 12]
HardyNum = 0
Softy = 2
SoftyList = [3, 5, 6, 7, 8, 9, 10]
SoftyNum = 0
Eletricy = 1
EletrictyList = [3, 5, 7, 9, 11, 12]
EletricyNum = 0
game1 = True
left = False
right = False
front = False
game2 = False
wirebreak = False
timewire = True
batterywire = True
Camwire = True
Doorwire = True
batterynum = 2
RESULT = 'Game Over'
while game1:
  if timewire == False:
    ran1 = random.randint(1,20)
    if ran1 == 1:
      timewire = True
  if batterywire == False:
    ran1 = random.randint(1,15)
    if ran1 == 1:
      batterywire = True
  if Camwire == False:
    ran1 = random.randint(1,5)
    if ran1 == 1:
      Camwire = True
  if Doorwire == False:
    ran1 = random.randint(1,5)
    if ran1 == 1:
      Doorwire = True
  if wirebreak == True:
    timewire = False
    batterywire = False
    Camwire = False
    Doorwire = False
    wirebreak = False
  if time2 == 6:
    RESULT = 'You Survived!!'
    game1 = False
  if battery <= 0:
    timewire = False
    batterywire = False
    Camwire = False
    Doorwire = False
    left = False
    right = False
    front = False
  if Time >= 60:
    Time = Time - 60
    time2 = time2 + 1
    if time2 == 13:
      time2 = 1
  if timewire == True:
    print(str(time2) + ':' + str(Time))
  if timewire == False:
    print('@!$*&:&^%$&')
  if batterywire == True:
    print(str(battery) + '%')
  if batterywire == False:
    print('&%*$@%')
  choice = input('Do you wanna see a CCTV or close Door?')
  if Camwire == False:
    print('Cam wire broken...')
    time.sleep(3)
  if choice == 'CCTV' and Camwire == True:
    if Softy == Commandy:
      print("Can't Find Commandy(Cam Error)")
    if Softy == Hardy:
      print("Can't Find Hardy(Cam Error)")
    if Softy != Commandy:
      print('Commandy is in ' + 'room ' + str(Commandy))
    if Softy != Hardy:
      print('Hardy is in ' + 'room ' + str(Hardy))
    if Softy >= 8 and Softy != Commandy and Softy != Hardy and Softy != Hardy:
      print('Softy is in room '+str(Softy))
    if Softy == Eletricy:
      print("Can't Find Eletricy(Cam Error)")
    if Softy != Eletricy:
      print('Eletricy is in ' + 'room ' + str(Eletricy))
    time.sleep(3)
    Time = Time + random.randint(5, 15)
    if battery >= 0:
      battery = battery - random.randint(0, batterynum)
  CommandyRan = random.randint(0, 4)
  HardyRan = random.randint(0, 3)
  SoftyRan = random.randint(0, 5)
  EletricyRan = random.randint(0, 6)
  if CommandyRan == 0:
    Commandy = CommandyList[CommandyNum]
    CommandyNum = CommandyNum + 1
  if Commandy == 13 and left == False:
    print('----------------')
    print('|   ---  ---   |')
    print('|     0  0     |')
    print('|      O       |')
    print('----------------')
    print('if intruder come: Kill cruelly and drive out...')
    time.sleep(5)
    print('iusjdfhialwj;juaehlawehulaegfiahdfjkahskfagkudshfgaksd')
    game1 = False
  if Commandy == 13 and left == True:
    print('Knock Knock')
    num2 = random.randint(1, 3)
    Commandy = CommandyList[num2]
    CommandyNum = num2
    time.sleep(5)
  if HardyRan == 0:
    Hardy = HardyList[HardyNum]
    HardyNum = HardyNum + 1
  if Hardy == 12 and right == False:
    print('----------------')
    print('----------------')
    print('|  0        0  |')
    print('|    ______    |')
    print('|______________|')
    print("I'll make you hard to live. Actually life is hard")
    time.sleep(5)
    print('ajdfhlahfeiufdhbsagfvgcvhxjcgydafgkeyt37823yehuidjahkea')
    game1 = False
  if Hardy == 12 and right == True:
    print('Knock...')
    num2 = random.randint(1, 3)
    Hardy = HardyList[num2]
    HardyNum = num2
    time.sleep(5)
  if SoftyRan == 0:
    Softy = SoftyList[SoftyNum]
    SoftyNum = SoftyNum + 1
  if Softy == 10 and front == False:
    print('|~~~~~~~~~~~~~~|')
    print('|  (0)    (0)  |')
    print('| \          / |')
    print('|  \________/  |')
    print('|______________|')
    print("It's okay. I'll kill you as softly as.HAHAHAHAHAHAHAHA")
    time.sleep(5)
    print('daijfklhjbxhfbksydigwavdngfahdfhag,bfagjsdgfaujfhtdfhymkuhkutdjur')
    game1 = False
  if Softy == 10 and front == True:
    print('Bang')
    num2 = random.randint(1, 3)
    Softy = SoftyList[num2]
    SoftyNum = num2
    time.sleep(5)
  if EletricyRan == 0:
    Eletricy = EletrictyList[EletricyNum]
    EletricyNum = EletricyNum + 1
  if Eletricy == 12 and right == False:
    print('HaHaHa')
    wirebreak = True
    Eletricy = EletrictyList[1]
    EletricyNum = 1
    time.sleep(5)
    left = False
    right = False
    front = False
  if Eletricy == 12 and right == True:
    print('BamBam')
    num2 = random.randint(1, 3)
    Eletricy = EletrictyList[num2]
    EletricyNum = num2
    time.sleep(5)
  if choice == 'Door' and Doorwire == False:
    print("Door's wire problem...")
    time.sleep(3)
  if choice == 'Door' and Doorwire == True:
    DoorChoice = input('Which door you close?(front, right, left)')
    if DoorChoice == 'front' and front == True and wirebreak == False:
      front = False
      print('You open front door')
      batterynum = batterynum -10
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    elif DoorChoice == 'front' and front == False and wirebreak == False:
      front = True
      print('You close front door')
      batterynum = batterynum + 10
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    if DoorChoice == 'left' and left == True and wirebreak == False:
      left = False
      print('You open left door')
      batterynum = batterynum - 5
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    elif DoorChoice == 'left' and left == False and wirebreak == False:
      left = True
      print('You close left door')
      batterynum = batterynum + 5
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    if DoorChoice == 'right' and right == True and wirebreak == False:
      right = False
      print('You open right door')
      batterynum = batterynum - 5
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    elif DoorChoice == 'right' and right == False and wirebreak == False:
      right = True
      print('You close right door')
      batterynum = batterynum + 5
      Time = Time + random.randint(5, 15)
      time.sleep(5)
    if wirebreak == True:
      print("Can't close door...")
print(RESULT)