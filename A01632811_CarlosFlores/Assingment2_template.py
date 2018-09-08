
#***************************************************************************
# Title        : Assignment2_template.py
#
# Description  : This file is a starting point for assignment 2 it contains
#                the main parts and pseudo code for you to complete with your 
#                own code.
#
# Environment  : Python 2.7 Code. 
#
# License      : GNU GPL version 3
#
# Editor Used  : Sublime Text
#
#****************************************************************************

#****************************************************************************
# Imported functions, classes and methods
#****************************************************************************
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

#****************************************************************************
#   Method Name     : set_velocity_body
#
#   Description     : Sends a MAVLINK velocity command in body frame reference
#                     This means that the X, Y, Z axis will be in relation to the 
#                     vehicle. 
#                     Positive X values will move the drone forward
#                     Positive Y values will move the drone Right
#                     Positive Z values will move the drone down
#                     The values for vx, vy and vz are in m/s, so sending a value
#                     of say 5 in vx will move the drone forward at 5 m/s
#
#                     More information can be found here:
#                     http://ardupilot.org/dev/docs/copter-commands-in-guided-mode.html
#
#   Parameters      : vehicle:  vehicle instance to send the command to
#                     vx:       Velocity in the X axis 
#                     vy
#                     vz
#
#   Return Value    : None
#
#   Author           : tiziano fiorenzani
#
#****************************************************************************

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

#****************************************************************************
#   Method Name     : arm_and_takeoff
#
#   Description     : Add your takeoff function from your last assignment here
#
#   Parameters      : targetAltitude
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
def arm_and_takeoff (vehicle, TargetAltitude): #arm the drone and then take off to the altitude choosen
    print ("Arming and Taking off...")

    while not vehicle.is_armable:
           print ("Not armable yet, waiting...")  
           time.sleep(1)

    print ("Warning turning on motors, stay away") 

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed= True

    while not vehicle.armed:
        print ("Waiting...")
        time.sleep(1)   

    vehicle.simple_takeoff(TargetAltitude)  

    
    while True: 
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude:", currentAltitude)

        if currentAltitude >= TargetAltitude*0.95:
            print("Altitude reached, Takeoff_finished")
            break 

        time.sleep(1)

#****************************************************************************
#   Method Name     : key
#
#   Description     : Callback for TkInter Key events
#
#   Parameters      : Event: tkinter event containing the key that was pressed
#
#   Return Value    : None
#
#   Author           : You
#
#****************************************************************************
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
            vehicle.mode = VehicleMode ("RTL") ### Change the drone to return mode
        elif event.keysym == 'l':
            vehicle.mode = VehicleMode ("LAND") # change the mode to land
            
    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body (vehicle, 5, 0, 0 ) ### move drone 5 meters per seconds up
        elif event.keysym == 'Down':
            set_velocity_body (vehicle, -5, 0, 0)### move drone 5 meters per seconds down
        elif event.keysym == 'Left':
            set_velocity_body (vehicle, 0, -5, 0) ### move drone 5 meters per seconds left 
        elif event.keysym == 'Right':
            set_velocity_body (vehicle, 0, 5, 0) ### move drone 5 meters per seconds rigth

#   MAIN CODE

# connect to the drone here 
def main ():
    global vehicle
    vehicle = connect ("udp:localhost:14551", wait_ready=True)
    
    arm_and_takeoff(vehicle,10) #take off 
    # Read the keyboard with tkinter
    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode. Press l for LAND mode")
    root.bind_all('<Key>', key)
    root.mainloop()

if __name__== "__main__":
    main()

 
