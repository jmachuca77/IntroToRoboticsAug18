from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
import time 
from pymavlink import mavutil
import Tkinter as tk 

#se descarga Tkinter de la terminal con el comando sudo apt-get install python-tk
#para correr dronekit se uso el comando  dronekit-sitl copter --home=20.736051,-103.456728,123,234
#para correr mavproxy seusa el comando en la terminal de mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551
#el programa tiene el punto extra de pasar a modo land con otra tecla. (a)
def arm_and_takeoff(vehicle, TargetAltitude):#se define que se armara el vehiculo y llegara a cierta altura
    print ("Arming and taking off...")

    while not vehicle.is_armable:#el vehiculo se prepara para armarse 
        print("Not armable, waiting...")
        time.sleep(1)
    print("Warning, turning on motors!")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed= True

    while not vehicle.armed:
        print("vehicle not armable, waiting...")
        time.sleep(1)#se escribe eso mientras el vehiculo no este armado

    vehicle.simple_takeoff(TargetAltitude)

    while True:
      currentAltitude = vehicle.location.global_relative_frame.alt
      print("Altitude ", currentAltitude)#se imprime la altitud del dron en tiempo real

      if currentAltitude >= TargetAltitude*0.95:
         print("Altitude Reached, Takeoff finished")
         break#una vez la alitud sea mayor al 95% se dejara de imprimir y se escribira eso
      time.sleep(1)



def set_velocity_body(vehicle, vx, vy, vz):#con esta funcion se haran las funciones para mover el dron en el eje de las x, y y z pero la z siempre sera 0 porque no queremos cambiar la altitud
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111,
            0, 0, 0,#posicion
            vx, vy, vz,#velocidad
            0, 0, 0,#aceleracion
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

def key(event):#nota: el eje positivo de las x es donde este apuntando la flecha el dron
    if event.char == event.keysym:# se declara el evento para cambiar las acciones al presionar ciertas letras
        if event.keysym == 'r':

            vehicle.mode = VehicleMode("RTL")# se declara que al precionar la letra r se cambia el dron al modo RTL lo cual hace que regrese al punto de inicio y aterrice
            print("Mode RTL slected returning to starting point and preparing to land")
        elif event.keysym == 'a':
            vehicle.mode = VehicleMode("LAND")# se declara que al precionar la tecla a el dron cambia a modo LAND y aterriza
            print("Mode land selected, landing")#esto es un punto extra
        
            

    else:
        if event.keysym == 'Up':#con esto se indica que al precionar la flecha up el dron se movera a 5 metros sobre segundo en el eje positivo de las x
            set_velocity_body(vehicle, 5, 0, 0)

        elif event.keysym == 'Down':#lo mismo pero en el eje negativo de las x
            set_velocity_body(vehicle, -5, 0, 0)

        elif event.keysym == 'Left':
            set_velocity_body(vehicle, 0, -5, 0)#lo mismo pero en el eje negativo de las y
        
        elif event.keysym == 'Right':
            set_velocity_body(vehicle, 0, 5, 0)# lo mismo pero en el eje positivo de las y
        
       

def main():

    global vehicle   #puse la variable vehicle como global debido a que cuando corria el programa la funcion key decia que no estaba definida la variable vehiculo.
    
    vehicle = connect("udp:localhost:14551", wait_ready=True)#conectar mavproxy al servidor escogido
    arm_and_takeoff(vehicle, 10)#ejecutar la funcion de arm adn takeoff
    
    

    root = tk.Tk()#se conecta nuestro programa con lo que descargamos al inicio al Tkinter
    print (">> Control the drone with the arrow keys. Press r for RTL mode or a to LAND mode")
    root.bind_all('<Key>', key)#con esto se manda a llamar a la funcion key dependiendo de la tecla que uses
    root.mainloop()

    
    
    


if __name__== "__main__":#Con esto se ejecuta la funcion main la cual hace que todas las funciones se ejecuten y en el orden que las pusite
    main()