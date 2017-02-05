from sensor.sensor import Sensor


def main():
    sensor = Sensor()
    print("Distance received: " + sensor.get_distance_in_cm())

if __name__ == "__main__":
    main()
