import time
from djitellopy import Tello
def main():
    tello = Tello()
    tello.connect()
    print("Connected")

    tello.takeoff()
    tello.move_up(20)
    tello.move_down(40)
    tello.land()

if __name__=="__main__":
    main()