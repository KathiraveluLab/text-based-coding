class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Started, let's ride!")
    def stop(self):
        self.speed = 0
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Speed is:", self.speed)
        else:
            print("You need to start me first")


class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

c1 = Car()
c1.increase_speed(10)
c2 = Car(True)
c2.increase_speed(10)
c3 = Car(True, 50)
c3.increase_speed(10)
c4 = Car(started=True, speed=40)
c4.increase_speed(10)