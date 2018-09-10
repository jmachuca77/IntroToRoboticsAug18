
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
import time 
from pymavlink import mavutil
import Tkinter as tk

 #poner en dronekit esta forma para que salga en el tec dronekit-sitl copter --home=20.736739,-103.457105,1641,5385
# 
def arm_and_takeoff(vehicle, TargetAltitude):
    print("running arm_and_takeoff")
  
  
    while not vehicle.is_armable:
          print("vehicle not armable, waiting...")
          time.sleep(1)

    print("changing mode to guided")
    vehicle.mode = VehicleMode("GUIDED") 
       
    print("WARNING MOTORS ARMING")
    vehicle.armed = True
   
    while not vehicle.armed:
        print("waiting for arming...")
        time.sleep(1)

    print("warning taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude reached, Takeoff finished")
            break
            
        time.sleep(1)
    

def set_velocity(vehicle, vx, vy, vz):
 msg = vehicle.message_factory.set_position_target_local_ned_encode(
 0,
 0, 0,
 mavutil.mavlink.MAV_FRAME_BODY_NED,
 0b0000111111000111, 
 0, 0, 0, #-- POSICION
 vx, vy, vz, #-- VELOCIDAD
 0, 0, 0, #-- ACCELERACION
 0, 0)
 vehicle.send_mavlink(msg)
 vehicle.flush() 
    
def key(event):
    if event.char == event.keysym:#events starts coming if a letter is pushed
        if event.keysym == 'r' :#if letter r is push vehicle will become rtl
         vehicle.mode = VehicleMode("RTL")
         print("mode RTL active")
         time.sleep(1)
        elif event.keysym == '1':#if 1 is presed vehicle is goitn to land
         vehicle.mode = VehicleMode("LAND")
         print("land")
         time.sleep(1)
    
    else: 
        if event.keysym == 'up':
           set_velocity(vehicle,5,0,0)
        elif event.keysym == 'down':
           set_velocity(vehicle,-5,0,0)
        elif event.keysym == 'right':
           set_velocity(vehicle,0,5,0)
        elif event.keysym == 'left':
           set_velocity(vehicle,0,-5,0)




def main():
    global vehicle #the program did not if vehicle was not defined
    vehicle = connect('udp:localhost:14551', wait_ready=True)
    arm_and_takeoff (vehicle, 10)#the vehicle goes up
    root = tk.Tk()
    print("control the drone with the arrow keys. Press r for RTL mode or land with 1")
    root.bind_all('<Key>', key)
    root.mainloop()
    
    
   
   
   
if __name__ == "__main__":
    main()
   