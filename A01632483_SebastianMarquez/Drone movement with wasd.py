#Import of libraries
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import tkinter
from pymavlink import mavutil
import subprocess

#This line code calls the console to execute the mavproxy and connect to dronekit
#subprocess.call("mavproxy.py --master tcp:127.0.0.1:5760 --out udp:localhost:14551", shell=True)
#time.sleep(15)

vehicle = connect("udp:localhost:14551", wait_ready=True)

#This makes the drone arm and takeoff, currently it reaches 2m at takeoff as set in main
def arm_and_takeoff(vehicle, TarjetAltitude):
    print ("Arming and taking off...")

    while not vehicle.is_armable:
        print ("Vehicle not armable. waiting...")
        time.sleep (1)
    
    print ("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    print ("WARNING MOTORS ARMING!")
    vehicle.armed = True
    
    while not vehicle.armed:
        print ("Waiting for arming...")
        time.sleep(1)

    print ("WARNING! Taking off!")
    vehicle.simple_takeoff(TarjetAltitude)
    
    while True:
        currentaltitude = vehicle.location.global_relative_frame.alt
        print("Altitutude: %f" % currentaltitude)

        if currentaltitude == TarjetAltitude:
            print ("Altitude Reached")
            break
        time.sleep(1)

#Sets the veelocity values that will later be sent to the drone
def set_velocity_body(Vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,
        0, 0,
        mavutil.mavlink.MAV_FRAME_BODY_NED, 0b0000111111000111, 
        0, 0, 0,
        vx, vy, vz,
        0, 0, 0,
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#This was made thinking that the drone starts at (using command --home=20.735520,-103.457456,000,000) 20.735520,-103.457456. This code basically makes the dorne move on a square with the use of four movements
def executeOrder66(Vehicle):
    print("Palpatine just told the drone to execute order 66")
    waypoint1 = LocationGlobalRelative(20.736120,-103.457456,20)
    waypoint2 = LocationGlobalRelative(20.736120,-103.457056,20)
    waypoint3 = LocationGlobalRelative(20.735520,-103.457056,20)
    waypoint4 = LocationGlobalRelative(20.735520,-103.457456,20)

    vehicle.simple_goto(waypoint1)
    time.sleep(20)
    print("reached first point")
    vehicle.simple_goto(waypoint2)
    time.sleep(20)
    print("reached second point")
    vehicle.simple_goto(waypoint3)
    time.sleep(20)
    print("reached third point")
    vehicle.simple_goto(waypoint4)
    time.sleep(20)
    print("reached last point")

#Movement and landing commands, the arrow keys move the dorne in X and Y axys, the l lands the drone
def movement_commands(event):
    print(event.char)
    if event.char == event.keysym:
        if event.keysym == "w":
            set_velocity_body(vehicle, 10, 0, 0)
            print("Moving forward...")
    
        if event.keysym == "s":
            set_velocity_body(vehicle, -10, 0, 0)
            print("Moving backward...")
    
        if event.keysym == "a":
            set_velocity_body(vehicle, 0, -10, 0)
            print("Moving left...")
    
        if event.keysym == "d":
            set_velocity_body(vehicle, 0, 10, 0)
            print("Moving right...")

        if event.keysym == "l":
            vehicle.mode = VehicleMode("LAND")
            print("Land sequence iniciated")
        time.sleep(0.5)

def move_mode():
    
    root =tkinter.Tk()
    print("Control the drone with the arrow keys on the keyboard. Press the L key for iniciating landing sequence, have fun!")
    root.bind_all('<Key>', movement_commands)
    root.mainloop()

    
    

#This is the main funtion, first it connects to the drone on the especified direction, runs the arm and takeoff funtion and then makes the drone land.
def main():
    arm_and_takeoff(vehicle, 2)
    move_mode()


if __name__== '__main__':
    main()
