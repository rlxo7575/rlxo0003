import random as r

Seats = []
for i in range(1,32):
    Seats.append(i)

students = ['강민호','강예령','김가희','김기태','김승후','김시은','김지민','김진욱','김태빈','남지영','류은준','박연수','박예림','서  율','송예원','우제은','유정민','이  결','이다인','이석호','이  얀','이종윤','이진선','이태하','임연우','장안나','정지유','조민준','최희원','허채율','황지민']

def SeatChange(Seat,Students):
    Changed = []
    for i in Seat:
        ChangeStudents = r.choice(Students)
        for x,i in enumerate(Students):
            if i == ChangeStudents:
                Students.pop(x)
                Changed.append(i)
    return Changed

def SeatDraw(list):
    printval1 = 0
    printval1 = '['+str(list[0])+']'
    for i in range(1,6):
        printval1 = printval1+'['+str(list[i])+']'

    printval2 = 0
    printval2 = '['+str(list[6])+']'
    for i in range(7,12):
        printval2 = printval2+'['+str(list[i])+']'
        
    printval3 = 0
    printval3 = '['+str(list[12])+']'
    for i in range(13,18):
        printval3 = printval3+'['+str(list[i])+']' 

    printval4 = 0
    printval4 = '['+str(list[18])+']'
    for i in range(19,24):
        printval4 = printval4+'['+str(list[i])+']'

    printval5 = 0
    printval5 = '['+str(list[24])+']'
    for i in range(25,29):
        printval5 = printval5+'['+str(list[i])+']'
    printval5 = printval5+'['+'      '+']'

    printval6 = 0
    printval6 = '['+'      '+']'
    printval6 = printval6+'['+'      '+']'
    printval6 = printval6+'['+str(list[29])+']'
    printval6 = printval6+'['+str(list[30])+']'
    printval6 = printval6+'['+'      '+']'
    printval6 = printval6+'['+'      '+']'

    print(printval1)
    print(printval2)
    print(printval3)
    print(printval4)
    print(printval5)
    print(printval6)

SeatDraw(SeatChange(Seats,students))