from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import time
from pymavlink import mavutil
import Tkinter as tk

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


def arm_and_takeoff(vehicle, TargetAltitude):
    print("Arming and taking off...")

    while not vehicle.is_armable:
        print("Not armable, waiting...")
        time.sleep(1)
    print("WARNING TURNING ON MOTORS")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    print ("Warning taking off... ")
    vehicle.simple_takeoff(TargetAltitude)
    
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print ("Altitude Reached, Take off f")
            break
        time.sleep(1) 

def key(event): #Este evento es para definir lo que pasara si aprietas ciertas teclas
    if event.char == event.keysym:
        if event.keysym == 'r':
            print ("RTL Mode.. The vehicle is going to the inicial position to land")
            vehicle.mode = VehicleMode("RTL")
        #Si se preiona la tecla 'r' el dron se dirigira al punto incial y se estacionara ahi
        #>>>>Esto es el punto extra<<<<
        elif event.keysym == 'l':
            print ("Landing the vehicle..")
            vehicle.mode = VehicleMode("LAND")
        #En este caso si oprimes 'l' el dron aterrizara en el punto donde se encuentre en el momento    
    else:
        if event.keysym == 'Up': #Si se presiona la tecla de up el dron ira hacia delante 
            set_velocity_body(vehicle, 5, 0, 0)
        elif event.keysym == 'Down': #Aqui es down para ir abajo
            set_velocity_body(vehicle,-5, 0, 0)
        elif event.keysym == 'Right': #Aqui right para la derecha
            set_velocity_body(vehicle, 0, 5, 0)
        elif event.keysym == 'Left': # Y left para izquierda
            set_velocity_body(vehicle, 0, -5, 0)
     #Lo anterior va a una velocidad de 5m por segundo   

def main(): 
    global vehicle #Con esto llamamos a la variable global de vehicle
    vehicle = connect("udp:localhost:14551", wait_ready=True)  #Aqui se conecta con el dron primeramente
    arm_and_takeoff(vehicle,10) #Luego depega 10 metros       
    root = tk.Tk() #Con esto se abre el tk para el teclado
    print(">> Control the drone with the arrow keys") 
    print("Press 'r' for RTL mode")
    print("Press 'l' for land the vehicle wherever it is") #En los anteriores imprimimos las instrucciones para que el usuario pueda aterrizarlo a su gusto
    root.bind_all('<Key>', key)
    root.mainloop() 

if __name__=="__main__":
    main()   
            
    


