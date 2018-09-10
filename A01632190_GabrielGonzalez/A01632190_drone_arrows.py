#first of all, you have to start the dronekit simulator with the instruction: dronekit-sitl copter --home=20.735552,-103.456232,20,20 where the numbers oare the coordinates of the desired place of the simulation to start.
#next you declare de objects to import from the dronekit, which are the conecction, the drone simulator and the GPS ad the time counter in seconds
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk #Here you import the interpreter function to read your keyboard from Tkinter
from gabodrone import arm_and_takeoff #Here you import the arm and take off from a previous programming session thanks to the 'main'.

vehicle = connect("udp:localhost:14551",wait_ready=True) #This instruction is to connect with the vehicle
#The previous one lets you connect with the "drone" to start the arm and take off function.
def set_velocity_body(vehicle, vx, vy, vz): #Here you define that there will be some values assigned to the variables vx, vy and vz that sate in which three-dimensional way the drone will move.
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
def key(event): #This will define the process to be done whe a key from the keyboard is pressed.
    if event.char == event.keysym: #-- standard keys
                if event.keysym == 'r': #This says that if the key 'r' is pressed, the drone with return to the launch point and land.
                 vehicle.mode=VehicleMode("RTL")
                 print("Returning to launch point.")    
                else: #-- non standard keys
                        if event.keysym == 'w': #This tells that each key will assign a different value to the vx and vy variables, making the drone to move in a direction.
                                set_velocity_body(vehicle, 20, 0, 0)
                                print("Moving forwward")
                        elif event.keysym == 's':
                                set_velocity_body(vehicle, -20, 0, 0)
                                print("Moving backwards")
                        elif event.keysym == 'a':
                                set_velocity_body(vehicle, 0, -20, 0)
                                print("Moving to the left")
                        elif event.keysym == 'd':
                                set_velocity_body(vehicle, 0, 20, 0)
                                print("Moving to the right")

def main(): #This part defines the main process and compiles the previous defined process and arranges them in a certain order to be done.
    vehicle = connect("udp:localhost:14551",wait_ready=True) #This instruction is to connect with the vehicle
    
    global vehicle

    arm_and_takeoff(vehicle,10) #It tells to make the process of the takeoff previously defined to a certain altitude. Here you program the altitude to be reached.
    root = tk.Tk()
    print("Control the drone with the arrow keys. Press r for RTL mode")
    root.bind_all('<Key>', key)
    root.mainloop()   #The four last code lines allow the process of the reading of your keyboard and the connection and interpretation for the drone of this.



if __name__=='__main__':
    main() #This stablishes that you can call this process in another programming session.