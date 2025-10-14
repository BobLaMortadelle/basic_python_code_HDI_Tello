import time
from djitellopy import Tello
def main():
    tello = Tello()
    tello.connect()
    print("Connected")

    # # Ambulance flashing light
    # for  i in range (4):
    #     tello.send_expansion_command("led 255 0 0")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("led 0 0 255")
    #     time.sleep(0.1)

    # # Mapping
    # for i in range (4):
    #     tello.send_expansion_command("mled g "  + "000rr00000000000000000000000000000000000000000000000000000000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "rbbbbbbr00000000000000000000000000000000000000000000000000000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000br000000r00000000000000000000000000000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000bb000000bb000000bb000000br000000r00000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000bb000000bb000000bb000000bb000000bbr0000rb")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbbr000p0bb000000bb00000rbbp00000bb000000bb0r00p0bbbbbbbbb")
    #     time.sleep(0.5)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000bb000000bb000000bb000000bb000000bbr0000rb")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000bb000000bb000000bb000000br000000r00000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "bbbbbbbbb000000bb000000br000000r00000000000000000000000000000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "rbbbbbbr00000000000000000000000000000000000000000000000000000000")
    #     time.sleep(0.1)
    #     tello.send_expansion_command("mled g "  + "000rr00000000000000000000000000000000000000000000000000000000000")
    #     time.sleep(0.1)

    # # heart
    # for i in range(4):
    #     tello.send_expansion_command("mled g " + "000000000rr0rr00rrrrrrr0rrrrrrp00rrrrp0000rrp000000p000000000000")
    #     time.sleep(0.75)
    #     tello.send_expansion_command("mled g " + "0000000000rr0rr00rrrrrrr0rrrrrrp0rrrrrrp00rrrrp0000rrp000000p000")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "000000000rr0rr00rrrrrrr0rrrrrrp00rrrrp0000rrp000000p000000000000")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "0000000000rr0rr00rrrrrrr0rrrrrrp0rrrrrrp00rrrrp0000rrp000000p000")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "000000000rr0rr00rrrrrrr0rrrrrrp00rrrrp0000rrp000000p000000000000")
    #     time.sleep(0.75)

    # fire
    for i in range(4):
        tello.send_expansion_command("mled g " + "00000000000rr000000rpr0000rrppr000rpppr00rpppprr0rpprppr00rrrrr0")
        time.sleep(0.2)
        tello.send_expansion_command("mled g " + "0000r000000rrr0000rrpr0000rrprr000rpprr00rpppprr0rpprprr00rrrrr0")
        time.sleep(0.2)
        tello.send_expansion_command("mled g " + "000rr000000rpr0000rrpr0000rppr000rppppr00rpppprr0rpprppr00rrrrr0")
        time.sleep(0.2)
        tello.send_expansion_command("mled g " + "000r000000rrr00000rprr000rrpprr00rppprr0rpppppr0rrprppr00rrrrr00")
        time.sleep(0.2)

    # # chemicals
    # for i in range(4):
    #     tello.send_expansion_command("mled g " + "00bbbb00000bb000000bb000000bb00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000bb000000bb000000pb00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000bb000000bb000000pp00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000bb000000bp000000pr00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000bb000000pp000000rr00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000pb000000rp000000rr00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000pp000000rr000000rr00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00bbbb00000rr000000rr000000rr00000bprb000bprrrb0bprrrrrb0bbbbbb0")
    #     time.sleep(0.2)

    # # open hand pink 
    # for i in range(4):
    #     tello.send_expansion_command("mled g " + "00000000000000000000000000pppp0000ppppp00pppppp00pppppp000pppp00:")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "00000000000p00000p0p0p000p0p0p0000pppp0p00ppppp00pppppp000pppp00:")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g " + "000p00000p0p0p000p0p0p000p0p0p0p00pppp0pp0ppppp00pppppp000pppp00:")
    #     time.sleep(0.5)

    # # thumb-up pink
    # for i in range(4):
    #     tello.send_expansion_command("mled g "  + "000000000000000000pppp00bbppppp0bbppppp0bbppppp0bbppppp000000000")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g "  + "000000000000pp0000ppp000bbppppp0bbppppp0bbppppp0bbppppp000000000")
    #     time.sleep(0.2)
    #     tello.send_expansion_command("mled g "  + "0000p000000pp00000pp0000bbppppp0bbppppp0bbppppp0bbppppp000000000")
    #     time.sleep(1)



if __name__=="__main__":
    main()