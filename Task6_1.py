import time


class TrafficLight:
    color = 0

    def running(self):
        for i in range(3):
            if i == 0:
                TrafficLight.color = "red"
                print(TrafficLight.color)
                time.sleep(7)
            elif i == 1:
                TrafficLight.color = "yellow"
                print(TrafficLight.color)
                time.sleep(2)
            else:
                TrafficLight.color = "green"
                print(TrafficLight.color)
                time.sleep(1)


a = TrafficLight()
a.running()

