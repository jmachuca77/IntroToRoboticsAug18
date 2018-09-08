import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk
import os

#Adds and Activates the terminal with dronekit
os.system("gnome-terminal -e 'bash -c \"dronekit-sitl copter --home=20.735798,-103.456359,1644.000,353; sleep 1000000\" '")
time.sleep(9)
#Adds and activates a terminal with mavproxy
os.system("gnome-terminal -e 'bash -c \"mavproxy.py --master tcp:127.0.0.1:5760 --out udp:localhost:14551; sleep 1000000\" '")
time.sleep(10)
def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

def arm_and_takeoff(vehicle,TargetAltitude):
    print("Running arm and takeoff")
    #In case the vehicle is nor armable, the function is told to wait until it is armable
    while not vehicle.is_armable:
        print("Vehicle is not armable, waiting...")
        time.sleep(1)
    #Changes to the control mode
    print("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    #Warning that the motors are indeed arming, and 
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True
    #The function is told to wait until the vehicle is armed
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    #Warning that the vehicle is elevating in the air, and the vehicle starts moving upwards
    print("WARNING Taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        #Prints current altitude and also tells you which is the current altitude relative to your starting point
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude )
        #If the current altitude of the drone reaches %95 of the target altitude, it stops the while function
        if currentAltitude >= TargetAltitude*0.95:
            print("Altitude Reached, Takeoff finished")
            break       
        #waits one second
        time.sleep(1) 

def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
            vehicle.mode = VehicleMode("RTL") #Return to land
        elif event.keysym == 'l':
            vehicle.mode = VehicleMode("LAND") #Land in the point you are at
            
    else: #-- non standard keys     
        if event.keysym == 'Up':
            set_velocity_body(vehicle, 5, 0, 0) #makes the drone move forward
    
        elif event.keysym == 'Down':
            set_velocity_body(vehicle, -5, 0, 0)#Makes the drone move backwards

        elif event.keysym == 'Left':
            set_velocity_body(vehicle, 0, -5, 0) #Makes the drone move Left
        elif event.keysym == 'Right':
            set_velocity_body(vehicle, 0, 5, 0)#Makes the drone move right
        
def main():
    
    ### add your code to connect to the drone here ###
    global vehicle 
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    # Take off to 10 m altitude
    arm_and_takeoff(vehicle, 10)
 
    # Read the keyboard with tkinter
    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode. Press L for LAND mode")
    root.bind_all('<Key>', key) 
    root.mainloop() 

#calls function
if __name__ == "__main__":
    main()
