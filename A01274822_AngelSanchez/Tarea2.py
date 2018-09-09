from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import time
import Tkinter as tk
from pymavlink import mavutil # para que el codigo funcione estamos importando otra funcion para que trabaje con el codigo

# Importante: agregar los siguientes apartados
# Descargar Tkinter en la terminal con el siguiente comando: sudo apt-get install python-tk
# Para cambiar la posicion del dron en la consola colocar: dronekit-sitl copter --home=20.737207,-103.456803,250,350
# Para usar mavproxy se uso mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551

#Esta parte fue tomada de la tarea 1
def arm_and_takeoff(vehicle, TargetAltitude): #define una variable
    print ("Running arm_and_takeoff") #aviso

    while not vehicle.is_armable:
        print ("Vehicle not armable, waiting...") #Este es para comprobar si esta armado el dron
        time.sleep(1) #sino envia un aviso

    print ("Changing mode to GUIDED") #cambianos la opcion a GUIDED
    vehicle.mode = VehicleMode("GUIDED")

    print ("WARNING MOTORS ARMING!") #aviso de motores armados
    vehicle.armed = True

    while not vehicle.armed: # si el dron no esta armado se espera para verificar
        print ("waiting for arming...") #aviso
        time.sleep(1)

    print ("WARNING! Taking off!") #aviso de despegue
    vehicle.simple_takeoff(TargetAltitude)
   
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print ("Altitude: %f" % currentAltitude)
        
        if currentAltitude >= (TargetAltitude*0.95): #los drones vuelan un aproximado nunca es exacto
            print("Altitude Reached, Takeoff finished")
            break

        time.sleep(1)

def set_velocity_body(vehicle, vx, vy, vz): #Este esta funcion se utilizaran las demas para que el dron se mueva en los ejes x, y, z, aunque z no se utilizara
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

def key(event): #se define la variable key
    if event.char == event.keysym: # si alguna de las letras es presionada entonces...
        if event.keysym == 'r': #Si esta tecla es precionada entonces se cambiara el modo a RTL
            vehicle.mode = VehicleMode("RTL") #Lleva al dron al punto inicial
            print("Se ha cambiado el modo a RTL, ejecutando...")
        elif event.keysym == 't': #Pero si esta tecla es presionada entonces se cambiara el modo a LAND
            vehicle.mode = VehicleMode("LAND") #el dron aterriza donde se encuentre, NOTA:esta parte es del EXTRA CREDIT
            print("Se ha cambiado el modo a LAND, ejecutando...")

    else:
        if event.keysym == 'Up': #el dron se movera a 5 metros por segundo sobre el eje 'x' hacia adelante
            set_velocity_body(vehicle, 5, 0, 0)

        elif event.keysym == 'Down': #el dron se movera a 5 metros por segundo sobre el eje 'x' hacia atras
            set_velocity_body(vehicle, -5, 0, 0)

        elif event.keysym == 'Left': #el dron se movera a 5 metros por segundo sobre el eje 'y' hacia la izquierda
            set_velocity_body(vehicle, 0, -5, 0)

        elif event.keysym == 'Right': #el dron se movera a 5 metros por segundo sobre el eje 'y' hacia la derecha
            set_velocity_body(vehicle, 0, 5, 0)
      
def main():
    global vehicle #inicializamos la variable vehicle para que pueda trabajar
    vehicle = connect('udp:127.0.0.1:14551', wait_ready=True) #Conectar la mavproxy con el servidor deseado
    arm_and_takeoff(vehicle, 10) #ejecutar la funcion con una altura de 10
    root = tk.Tk()
    print("Presiona r para RTL o t para LAND")
    root.bind_all('<Key>', key) #llama a la funcion key dependiendo de la tecla que pusiste arriba
    root.mainloop()
    
if __name__=="__main__": #
     main() 
