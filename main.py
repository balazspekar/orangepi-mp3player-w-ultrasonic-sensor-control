from modules.sensor import Sensor
from modules.player import Player
import time

def main():
    sensor = Sensor()
    #while True:
    #    print("Distance received: " + str(sensor.get_distance()))

    player = Player()
    player.load_file()    
    player.play()
    print("wait")
    for i in reversed(range(10)):
        print(i)
        time.sleep(1)
    print("tryna stop")
    player.stop()
    print("exiting")

if __name__ == "__main__":
    main()
