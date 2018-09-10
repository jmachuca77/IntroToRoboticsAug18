
# Imported functions, classes and methods
#To start the code in the Tec please put the next comand in the terminal #dronekit sitl copter --home=20.735517,-103.457499,30,0 
#One extra point, press 'l' for land mode 
# ****************************************************************************
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

# Set velocity 
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

        if currentAltitude >= TargetAltitude*0.95: # check the altitude to be 95% of 10 meters
            print("Altitude reached, Takeoff_finished")
            break 

        time.sleep(1) #wait one second 


def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
            vehicle.mode = VehicleMode ("RTL") ### Change the drone to return mode then print
            print "Returning..."
        elif event.keysym == 'l':
            vehicle.mode = VehicleMode ("LAND") # change the mode to land then print
            print "Landing..."
            
    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body (vehicle, 5, 0, 0 ) ### move drone 5 meters per seconds up then print
            print "Moving forward"
        elif event.keysym == 'Down':
            set_velocity_body (vehicle, -5, 0, 0)### move drone 5 meters per seconds down then print
            print "Moving backward"
        elif event.keysym == 'Left':
            set_velocity_body (vehicle, 0, -5, 0) ### move drone 5 meters per seconds left then print 
            print "Moving left"
        elif event.keysym == 'Right':
            set_velocity_body (vehicle, 0, 5, 0) ### move drone 5 meters per seconds rigth then print
            print "Moving rigth"

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

 
