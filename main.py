from sensor.sensor import Sensor


def main():
    sensor = Sensor()
    while True:
        print("Distance received: " + str(sensor.get_distance()))

if __name__ == "__main__":
    main()
