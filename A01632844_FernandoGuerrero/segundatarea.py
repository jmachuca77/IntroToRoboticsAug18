#this instruction is to download Tkinter from the terminal: sudo apt-get install python-tk
#here is the code for dronekit to appear at the tec: dronekit-sitl copter --home=20.735454,-103.457520,149,253
#To connect the drone to mavproxy from the terminal the instruction used is: mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551
#This programme contains an extra credit.(Line 67 and 68)
#here is to begin the importing of connect, VehicleMode, LocationGlobalRelative, time, Command and LocationGlobal from dronekit.
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import time
#here we are importing from pymavlink the mavutil and Tkinter function.
from pymavlink import mavutil
import Tkinter as tk 


#now we are defining the variable arm_and_takeoff and this variable is getting the altitude to be printed as running.
def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    #here is to print a message that the vehicle is not armed yet. Then it waits for a second.
    while not vehicle.is_armable:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    
    #here is to print that the mode has been changed and to comunicate the program that the mode of the vehicle will change into guided.
    print ("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    #here is to comunicate to the program to show a warning, when the vehicle is already armed.
    print ("WARNING MOTORS ARMING")
    vehicle.armed = True

    #in this step is to show a waiting while the vehicle is not completely armed. Then it waits for a second.
    while not vehicle.armed:
        print ("Waiting for arming...")
        time.sleep(1)
    #here is to indicate that the drone is starting the journey and to show and warning in the screen.
    print ("WARNING, Taking off")
    vehicle.simple_takeoff(TargetAltitude)
    #here is to know what the altitude of the drone is and print it in the screen.
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print ("Altitude: %f" % currentAltitude)
        #now here is to recognize that the dron can't get the exactly altitude, but close to it yes. It prints a message that the dron got the correct altitude too. Finally the break ends a loop and wait for a second.
        if currentAltitude >= (TargetAltitude*0.95):
            print ("Altitude Reached, Takeoff finished")
            break 
        time.sleep(1)

#At this part of the programme, we are saying to the programme to define the variable set_velocity_body and we declared the axes (x,y,z but this last one not will be used) that will be used by the drone for future movement.
def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, 
            0, 0, 0, #position
            vx, vy, vz, #velocity
            0, 0, 0, #acceleration
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#In this command what we are doing is declaring the key variable as an event, within which it is defined that when using the letter r it will change to RTL mode and when pressing the letter z change to LAND mode. In addition, we declared the speed with which we want the drone to travel on the axes of x and y, which is 5 m|s.
#Extra credit part
def key(event):
    if event.char == event.keysym: 
        if event.keysym == 'r':
            print("after r pressed change the vehicle mode to RTL")
            vehicle.mode = VehicleMode("RTL")
        elif event.keysym == 'z':
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

#Finally, we are connecting mavproxy to the drone. Also, we are calling the main function and Tkinter. Finally, if the name of the function is equal to main the main function will be executed.
def main():
    
    global vehicle
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    arm_and_takeoff(vehicle, 10)
    
    root = tk.Tk()
    print(" Control the drone with the arrow keys. Press r for RTL mode")
    root.bind_all('<Key>', key)
    root.mainloop()
    

if __name__=="__main__":
    main()

 



    