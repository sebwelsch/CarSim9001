import random

class Gearbox(object):

    def __init__(self):
        self.wheels = {'frontLeft':Wheel(), 'frontRight':Wheel(), 'rearLeft':Wheel(), 'rearRight':Wheel()}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        if self.clutchEngaged == True:
            return
        elif self.currentGear < 5:
            self.currentGear += 1
        else:
            return

    def shiftDown(self):
        if self.clutchEngaged == True:
            return
        elif self.currentGear > 0:
            self.currentGear -= 1
        else:
            return

    def rotate(self, revolutions):
        if self.clutchEngaged == True:
            for x in self.wheels:
                self.wheels[x].rotate(revolutions * self.gears[self.currentGear])
        else:
            return

class Wheel(object):

    def __init__(self):
        self.orientation = random.randint(0, 361)

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    def updateModel(self, dt):
        if self.theTank.contents > 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            self.currentRpm = 0

class Car(object):

    def __init__(self):
        self.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def remove(self, amount):
        if self.contents > 0:
            self.contents = self.contents - amount
        else:
            return

    def refuel(self):
        self.contents = self.capacity
