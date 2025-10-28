import time
import cv2
from djitellopy import Tello
def main():
    tello = Tello()
    tello.connect()
    print("Connected")

    # tello.query_sdk_version()

    tello.set_video_direction(tello.CAMERA_FORWARD)
    tello.streamon()


    while True:
        frame = tello.get_frame_read().frame
        crop_img = frame[0:240, 0:320]
        cv2.imshow("Frame", crop_img)
        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

    time.sleep(5)
    tello.send_control_command('EXT tof?')
    tello.end
    # tello.send_expansion_command("tof?")
    

if __name__=="__main__":
    main()