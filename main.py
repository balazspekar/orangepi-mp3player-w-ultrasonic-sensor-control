from modules.sensor import Sensor
from modules.player import Player


def main():
    sensor = Sensor()
    #while True:
    #    print("Distance received: " + str(sensor.get_distance()))

    player = Player()
    player.load_file()    
    player.play()
    #print("visszatert")

if __name__ == "__main__":
    main()
