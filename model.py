class Gearbox(object)

    def __init__(self):
        currentGear = 0
        clutchEngaged = False
        gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        if clutchEngaged = True:
            return
        elif currentGear < 5:
            currentGear = + 1
        else:
            return

    def shiftDown(self):
        if clutchEngaged = True:
            return
        elif currentGear > 0:
            currentGear = - 1
        else:
            return

    def rotate(self, revolutions):
        print()

class Wheel(object)


class Engine(object)

    def __init__(self):
        throttlePosition = 0
        theGearbox = Gearbox()
        currentRpm = 0
        consumptionConstant = 0.0025
        maxRpm = 100
        theTank = Tank()

    def updateModel(self, dt):
        if theTank > 0:
            currentRpm = throttlePosition * maxRpm
            theTank.remove(currentRpm * consumptionConstant)
            theGearbox.rotate(currentRpm * (dt / 60))
        else:
            currentRpm = 0

class Car(object)

    def __init__(self):
        theEngine = Engine()

    def updateModel(self, dt):
        theEngine.updateModel(dt)

class Tank(object)

    def __init__(self):
        capacity = 100
        contents = 100

    def remove(self, amount):
        if contents > 0:
            contents = contents - amount
        else:
            return

    def refuel(self):
        contents = capacity
