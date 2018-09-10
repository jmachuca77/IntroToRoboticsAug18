import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk
#Para descargar Tkinter sudo apt-get install python-tk
#dronekit-sitl copter --home=20.735864,-103.456779,350,450
#mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551
#Realice el punto extra de LAND
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

def arm_and_takeoff(vehicle, TargetAltitude): #Definimos arm_and_takeoff
    print("Arming and teaking off...") #Avisamos que el drone esta encendido y preparandose para despegar

    while not vehicle.is_armable: #Hasta que el drone este armado no va a pasar al siguiente paso
        print ("Not armable,waiting...") #Imprime este mensaje cada segundo hasta que este armado
        time.sleep(1)
        
    print("WARNING TURNING ON MOTORS") #Advierte que los motores estan encendidos

    vehicle.mode = VehicleMode("GUIDED") #Cambia el drone a modo GUIDED
    vehicle.armed=True

    while not vehicle.armed:
        print("Vehicle not armable,waiting...") #Se hace un chequeo del drone praa comprobar que ahora este armado
        time.sleep(1)

    vehicle.simple_takeoff(TargetAltitude)#Le decimos al drone que despegue a una altura de 10 metros

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: ", currentAltitude)

        if currentAltitude >= TargetAltitude*0.95:
            print ("Altitude Reached")
            break
        
        time.sleep(1)
#En la linea 54 se realizo el punto extra
def key(event):#Definimos la variable key que toma el valor de event
    if event.char == event.keysym: #Si alguna de las teclas presionadas es una letra entonces
        if event.keysym == 'r':#Si preciona r va a 
            vehicle.mode =VehicleMode("RTL")#Cambir el modo del drone a RTL
        elif event.keysym == 'l':#Si presiona l cambia a 
            vehicle.mode = VehicleMode("LAND")#modo LAND

    else: #Si presiona alguna tecla que no sea una letra entonces hace esto
        if event.keysym == 'Up':#Si presiona la flecha hacia arriba
            set_velocity_body(vehicle, 5, 0, 0)#El drone se mueve 5 m/s hacia en frente, dependiendo de donde apunte el drone
            #La flecha del drone es el eje de las x
        elif event.keysym == 'Down':#si presiona la flecha de abajo se movera a 5m/s en direccion hacia abajo del eje de las x
            set_velocity_body(vehicle, -5, 0, 0)
        elif event.keysym == 'Left':#Si presiona la flecha de la izquierda se movera a 5 m/s hacia el eje de las y negatvas
            set_velocity_body(vehicle, 0, -5, 0)
        elif event.keysym == 'Right':#Si presiona la flecha de la derecha se movera a 5 m/s hacia el eje de las y positivas
            set_velocity_body(vehicle, 0, 5, 0)
    
        
#Definimos vhicle como una variable global
#porque en def key decia que vehicle no estaba defino , cuando lo colocabamos dentro de key decia que event no estaba definio
#para evitar esto mejor colocar vehicle como global
#En vehicle connect se establece la coneccion con la terminal
def main():
    global vehicle
    vehicle = connect("udp:localhost:14551",wait_ready=True) 
    arm_and_takeoff(vehicle,10)#Definimos la altura a la que queremos que llegue
    
    root = tk.Tk()
    print("Presiona r para RTL o l para LAND")
    root.bind_all('<Key>', key)
    root.mainloop()


if __name__ == "__main__":#hace que las funciones dentro de main sean ejecutadas
    main()
 
