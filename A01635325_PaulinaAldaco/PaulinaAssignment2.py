from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal 
#imports functions from dronekit
import time
#imposts time function so that you can create delays
from pymavlink import mavutil
#will allow to send commands to mavproxy
import Tkinter as tk
#will allow to use Tkinter to read the keybord
from Paulina import arm_and_takeoff
#imports the function arm_and_takeoff from the file Paulina

vehicle = connect('udp:localhost:14551',wait_ready=True)
    #creates an object to store the vehicle, connects it to the drone, and waits for it to be ready

def main():
    #defines function main
    
    arm_and_takeoff(vehicle, 10)
    #calls function

    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode and l to land.")
    root.bind_all('<Key>', key)
    root.mainloop()
    #reads the keyboard with tkinter

    key(event)
    #calls the function key
    
def set_velocity_body(vehicle, vx, vy, vz):
#defines the function which will take the parameter vehicle and vx,vy,vz (velocities in x, y, and z axis)
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111,
            0, 0, 0,      #position
            vx, vy, vz,   #velocity
            0, 0, 0,      #acceleration
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
#this function sends a mavlink velocity command
#it is in body frame reference which means the x, y, and z axis are in relation to the drone

def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
            vehicle.mode = VehicleMode('RTL')
            print('rtl mode')
        elif event.keysym == 'l':
            vehicle.mode = VehicleMode('LAND')
            print('land mode')
        #extra credit
    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body(vehicle,5,0,0)
            print('forward')
        elif event.keysym == 'Down':
            set_velocity_body(vehicle,-5,0,0)
            print('back')
        elif event.keysym == 'Left':
            set_velocity_body(vehicle,0,-5,0)
            print('left')
        elif event.keysym == 'Right':
            set_velocity_body(vehicle,0,5,0)
            print('right')
#this function checks what key is being pressed
#depending on the key calls the set_velocity_body function with a certain value 


if __name__ == '__main__':
    main()
#it will only run the main function when the program is executed stand alone