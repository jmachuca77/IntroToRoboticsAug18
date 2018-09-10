import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk





def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    while not vehicle.is_armable: 
        print ("vehicle is not armable, waiting...")
        time.sleep(1)

    print ("changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    print ("WARNING MOTORS ARMING")
    vehicle.armed = True

    while not vehicle.armed:
        print ("waiting for arming...")
        time.sleep(1)

    print("WARNING: taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print ("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude reached, Takeoff finished")
            break
            
        time.sleep(1)




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




def key(vehicle,event):
    if event.char == event.keysym: 
        if event.keysym == 'r':
            vehicle.mode = VehicleMode("RTL") #RTL is return to llanding which is really convenient
                
            
    else: 
        if event.keysym == 'w':
            set_velocity_body(vehicle,5,0,0)
        elif event.keysym == 's':
            set_velocity_body(vehicle,-5,0,0)
        elif event.keysym == 'a':
            set_velocity_body(vehicle,0,-5,0)
        elif event.keysym == 'd':
            set_velocity_body(vehicle,0,5,0)


def control(vehicle):
    root = tk.Tk()
    print(">> Control the drone with the wasd. Press r for RTL")
    root.bind_all('<Key>', key)
    root.mainloop()


def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True)
    arm_and_takeoff(vehicle,10)
    control(vehicle)


    


if __name__ =="__main__":
    main()            