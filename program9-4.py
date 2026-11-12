class Appliance:
    def turn_on(self):
        pass
    def turn_off(self):
        pass
class TV(Appliance):
    def turn_on(self):
        print("The TV turns on.")
    def turn_off(self):
        print("The TV turns off.")
class WashingMachine(Appliance):
    def turn_on(self):
        print("The washingmachine turns on.")
    def turn_off(self):
        print("The washingmachine turns off.")
class AirConditioner(Appliance):
    def turn_on(self):
        print("The airconditioner turns on.")
    def turn_off(self):
        print("The airconditioner turns off.")

appliance = [TV(), WashingMachine(), AirConditioner()]
for box in appliance:
    box.turn_on()
for box in appliance:
    box.turn_off()