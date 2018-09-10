#you have to include these comands in your terminal: import Tkinter as tk, from pymavlink import mavutil
# To make the drone begin at Tec you have to write this code: dronekit--sitl copter --home=20.736420, -103457415,238, 208 
#this is the part of the code where you can get different functions that are inside of dronekit. One is to conect to the drone, the other is give the drone a mode to operate, the last is to have the altitude
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
#this is to have time in our code
import time
from pymavlink import mavutil
import Tkinter as tk

#This is to determine that we are working with new varaibles that have speed an direction
def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,            #-- POSITION
            vx, vy, vz,         #-- VELOCITY
            0, 0, 0,            #-- ACCELERATIONS
            0, 0)

    vehicle.send_mavlink(msg)
    vehicle.flush()

def arm_and_takeoff(vehicle, TargetAltitude):
    print ("Arming a Take off...")
#here we are saying that
    while not vehicle.is_armable:
        print("Not armable, waiting...")
        time.sleep(1)
  
      
    print ("changing mode to GUIDED")
    #so here we are comunicating directly with the module console, and we are telling it to print it is guided when we execute the function
    vehicle.mode = VehicleMode("GUIDED")

    print ("WARNING TURNING ON MOTORS!")
    vehicle.armed = True 
#This loop is going to print the text as long as the vehicle isn't armed
    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    #since this print is outside of the while, it will print whit no condition telling it otherwise
    print ("WARNING! Taking off!")
    # We are telling it to take off at the altitude we already assigned
    vehicle.simple_takeoff(TargetAltitude)
    while True:
        #this is just give the altitude the drone is a name, and it will be constantly printing that value
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)
#This condition if, is saying that as long as the current altitude is less than or equal to our alreday established altitude*0.95, then print the message and stop printing the altitude thank to the break
        if currentAltitude >= TargetAltitude*0.95:
            print ("Altitude Reached, takeoff finished")
            break

        time.sleep(1)
#This is to tell it to change mode when "r" is typed and to land where it started 
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r': 
            vehicle.mode = VehicleMode("RTL")
        #this block of code is for the extra credit wher if you click on "m" for the drone to automatically land where it is and change its mode to LAND
        elif event.keysym == 'm':
            vehicle.mode = VehicleMode("LAND")
    else: #-- non standard keys that will make the drone move in the direction we want
        #vehicle.mode = VehicleMode("RTL")
        if event.keysym == 'Up':#Move the drone forward
           set_velocity_body(vehicle, 5, 0, 0) ### add your code for what should happen when pressing the up arrow ###
        elif event.keysym == 'Down':#Moves the drone backward
             set_velocity_body(vehicle,-5, 0, 0)### add your code for what should happen when pressing the down arrow ###
        elif event.keysym == 'Left':#Move the drone left
             set_velocity_body(vehicle, 0, -5, 0)### add your code for what should happen when pressing the Left arrow ###
        elif event.keysym == 'Right':#Moves the drone right
             set_velocity_body(vehicle, 0, 5, 0)### add your code for what should happen when pressing the Right arrow ###

#****************************************************************************
#   MAIN CODE
#
#****************************************************************************

### add your code to connect to the drone here ###
def main():
    # it was necesary to make vehicle global so the event function would also apply to it
    global vehicle
    #here we are connecting to our sitl with it's IDP, and through the mavproxy port. the wait ready is going to let us know it is conected only when everything downloaded and ready to go
    vehicle = connect("udp:localhost:14551",wait_ready=True)
# here we going to tell it to begin with the mission, and then land it making the altitude go from the 10 we assigned to 0
    arm_and_takeoff(vehicle, 10)
    
    

 
# Read the keyboard with tkinter
    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode. Press m for automatic LAND")
    root.bind_all('<Key>', key)
    root.mainloop()

# Here we are simply stating that if the fucntions name is "main", the execute the function
if __name__=="__main__":
    main()