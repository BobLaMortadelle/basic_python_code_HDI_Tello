from djitellopy import Tello
def main():
    tello = Tello()
    tello.connect()
    print("Connected")
    tello.query_battery()
    tello.query_sdk_version()
    tello.end()


if __name__=="__main__":
    main()

