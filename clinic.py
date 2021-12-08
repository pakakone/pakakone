from pythonds.basic import Queue

import random


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

class doctor:
    def __init__(self, ppm):
        self.rate = ppm
        self.currentpatint = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentpatint != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentpatint = None

    def busy(self):
        if self.currentpatint != None:
            return True
        else:
            return False

    def startNext(self,newpatint):
        self.currentpatint = newpatint
        self.timeRemaining = newpatint.getPatint() /self.rate *60

class Patints :
    def __init__(self,time):
        self.timestamp = time
        self.Patint = random.randrange(20,61)

    def getStamp(self):
        return self.timestamp

    def getPatint(self):
        return self.Patint

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, patintPerMinute):

    doctorcomer = doctor(patintPerMinute)
    clinecQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if nextpatint():
         patints = Patints(currentSecond)
         clinecQueue.enqueue(patints)

      if (not doctorcomer.busy()) and (not clinecQueue.isEmpty()):
        nextPatints = clinecQueue.dequeue()
        waitingtimes.append(nextPatints.waitTime(currentSecond))
        doctorcomer.startNext(nextPatints)

      doctorcomer.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)

    print("Average Wait  " +(convert(averageWait)+", %3d patints are remaining."%clinecQueue.size()))

def nextpatint():
    num = random.randrange(1,361)
    if num == 360:
        return True
    else:
        return False

for i in range(10):
    simulation(4*3600,10)
