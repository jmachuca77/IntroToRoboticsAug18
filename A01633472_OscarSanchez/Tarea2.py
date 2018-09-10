#************************************************************************************************************************************************************************************************************************#
# Commands that have to be include in the terminal:
# Importing Tkinter:                                                   sudo apt-get install python-tk
# Set the drone in campus:                                         -   sitl copter --home=20.736334,-103.456695,130,312
# Connect the drone with mavproxy through the terminal                 mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551
#The programm has the extra credit of the landing point in the line 82 a 84

#Here we are importing connect, VehicleMode, LocationGlobalRelativa, Command and LocationGlobal from dronekit
#Also we are importing time and Tkinter for reading keyboard events
#Finnally we are importing mavutil drom pymavlink
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import time
from pymavlink import mavutil
import Tkinter as tk

#************************************************************************************************************************************************************************************************************************#
#Then you have to define the variable arm_and_takeoff which its arguments are vehicle and TargetAtltitude.
#When this variable activates it will print the message "Running arm_and_takeoff".
def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    # The while not function means that if the vehicle is not armable it will print the message "Vehicle not armable, waiting...". And with the time.sleep it will wait 1 second.
    while not vehicle.is_armable:
        print("Vehicle not armable, waiting...")
        time.sleep(1)

    #If this function is false it will print the message "Changing mode to GUIDED" After this you have to comunicate to the program that the mode of the vehicle has change to "GUIDED".
    print("Changign mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    #Next it will print the message "WARNING MOTORS ARMING!". And set the property vehicle.armed to True.
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True

    #If the property vehicled.armed is false then it will print the message "Waiting for arming,..". And it will wait 1 second.
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    #If this function is false then it will print the message "WARNING! Taking off!". And with the property .simple_takeoff the program will receive the value of the target altitude.
    print("WARNING! Taking off!")
    vehicle.simple_takeoff(TargetAltitude)
    
    #If this is True then you will assigned the altitude of the location of the vehicle to the variable currentAltitude. And it will be printed the altitude. 
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        #Inside this while function is a conditional function if that say that if the currentAltitude is greater or equal to the TargetAltitude times 0.95 it will print the message: "Altitude Reached, Takeoff finished".
        #Is 0.95 because the value we want for the altitude will never get exactly to it so it get to the most aproximate value.
        #Finally if this happens without errors, with the break function is going to stop the loop.
        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude Reached, Takeoff finished")
            break
        #It will wait 1 seconf for each value printed.
        time.sleep(1)

#************************************************************************************************************************************************************************************************************************#
#Then we are defining the set_velocity_body for sending velocity reference
#Also we are declaring the axes x, y, z which will be used for the movement of the drone (the axis z will not be used)
def set_velocity_body(vehicle, vx, vy, vz):    
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,
        0, 0,
        mavutil.mavlink.MAV_FRAME_BODY_NED,
        0b0000111111000111, #-- BITMASK -> Consider only the velocities
        0, 0, 0, #-- POSITION
        vx, vy, vz, #-- VELOCITY
        0, 0, 0, #-- ACCELERATIONS
        0, 0) 
    vehicle.send_mavlink(msg)
    vehicle.flush()

#************************************************************************************************************************************************************************************************************************#
#We are setting some instructions when the the letter r and l are pressed to set the vehicle.mode to LAND OR RTL according to the letter pressed
#Also we are delcaring that the velocity to 5 m/s 
#When the key pressed is up or down or left or right we are setting the velocity in the axes x and y  
def key(event):
    if event.char == event.keysym:
        if event.keysym == 'r':
            print("After r pressed vehicle mode changes to RTL")
            vehicle.mode = VehicleMode("RTL")
        elif event.keysym == 'l':
            print("After l pressed vehicle mode changes to LAND")
            vehicle.mode = VehicleMode("LAND")
    else: 
        if event.keysym == 'Up':
            set_velocity_body(vehicle, 5, 0, 0)
        elif event.keysym == 'Down':
            set_velocity_body(vehicle, -5, 0, 0)   
        elif event.keysym == 'Left': 
            set_velocity_body(vehicle, 0, -5, 0) 
        elif event.keysym == 'Right':     
            set_velocity_body(vehicle, 0, 5, 0) 

#************************************************************************************************************************************************************************************************************************#
#Finally we are connecting to the vehicle with the udp direction. And calling the function arm_and_takeoff
#And with the commands of root it is reading the keyboard with Tkinter
def main ():

    global vehicle 
    vehicle = connect('udp:127.0.0.1:14551', wait_ready=True)
    arm_and_takeoff(vehicle, 10)

    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode and press l for LAND mode)
    root.bind_all('<Key>', key)
    root.mainloop()

#If the name of the function is equal to "main" then it will ejecute the function main
if __name__ == "__main__":
    main()