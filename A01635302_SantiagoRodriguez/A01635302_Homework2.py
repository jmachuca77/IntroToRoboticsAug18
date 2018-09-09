from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal    #This command imports some information regarding the drone.

from pymavlink import mavutil   #This imports some functions from Mavlink.

import time     #This imports a function to enable delays in the code.

import Tkinter as tk    #This imports the functions from Tkinter.

def Takeoff_procedure(vehicle, Hoveraltitude):  #This will define the takeoff before begining the mission.
    
    print("Begining take off")  #Just a warning
    vehicle.mode = VehicleMode("GUIDED")    #This tells the drone to enter GUIDED mode, this will allow the takeoff.
    
    print("Turning on motors")  #Also a warning
    vehicle.armed = True    #This tells the drone to turn on the motors.
    
    while not vehicle.armed:    #This code will make a delay so that the code isn't processed too fast & the drone has time to properly turn on.
        print("Please wait")
        time.sleep(4)
    
    vehicle.simple_takeoff(Hoveraltitude)   #This function will begin the lift off now that the motors are running & the drone is in GUIDED mode.
    
    while True:     #This will form an infinite loop to tell the altitude.

        currentAltitude = vehicle.location.global_relative_frame.alt    #A variable we call curentAltitude will be equal to the height of the drone.
        print("Altitude: %f" % currentAltitude)     #This will print the altitude of the drone.
        time.sleep(1)   #This delay will avoid annoying spamming of altitude updates.
        
        if currentAltitude >= (Hoveraltitude*0.97):     #This will compare the altitude with the wished altitude, the desiered altitude is reduced a tiny bit since the drone almost never reaches exactly the right altitude.
            
            print("Stable altitude reached")    #This message indicates we have reached the proper altitude.
            break   #This will break the loop.

def land(vehicle):  #This will land the drone.

    print("Beginning landing")
    vehicle.mode = VehicleMode("LAND")  #This begins the LAND mode which lands the drone.
    time.sleep(30)
    print("The drone has landed")

def set_velocity_body(vehicle, vx, vy, vz): #This will define the function that will tell the drone how to move.
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

def key(event):     #This function will tell the drone when to move where.
    
    vehicle = connect("udp:localhost:14551",wait_ready=True)       #Vehicle must be defined once more

    while True:

        if event.char == event.keysym:  #This will tell if the value of keysym is a character or not.

            if event.keysym == "r":     #This will make the drone return.
                root = tk.Tk()
                root.bind_all('<Key>', key)     #This will ask again for value of the key for further instructions.
                print("The drone will return to the takeoff point.")
                vehicle.mode = VehicleMode("RTL")
                time.sleep(1)   

        else:

            if event.keysym == 'Up':    #This will tell the drone to move forwrard.

                set_velocity_body(vehicle, 5, 0, 0)
                
            elif event.keysym == 'Down':    #This will tell the drone to move backwards.

                set_velocity_body(vehicle, -5, 0, 0)
                
            elif event.keysym == 'Left':    #This will tell the drone to move to the left.

                set_velocity_body(vehicle, 0, -5, 0)
                
            elif event.keysym == 'Right':   #This will tell the drone to move to the right.

                set_velocity_body(vehicle, 0, 5, 0)
                
def main():     #This will define the main function, in here we'll execute most of the code.

    vehicle = connect("udp:localhost:14551",wait_ready=True)    #This will connect the drone & wait until it's ready
    
    Takeoff_procedure(vehicle, 10)   #This calls the Takeoff_procedure, in this case, it'll hover up to 10 m.
    
    root = tk.Tk()      #Line 93-96 will make Tkinter read the keyboard inputs.
    print("Control the drone with the arrow keys. Press r for RTL mode")
    root.bind_all('<Key>', key)
    root.mainloop() 

    key(event)  #This function will make the drone move given specific inputs.
    

if __name__ == "__main__":    #This condition will execute our main function if the other programs are running.
    
    main()

    #Pending issues, the event variable isn't defined & it remains unclear how to define it.
    #The keysym variable holding the input is permanent & to register another input, a new window must open, doesn't always work.
    #Intermitent flight paths.