# Para llamar a dronekit en la terminal se usa el comando dronekit-sitl copter --home=20.736297,03.455971,546,698 , presionas r para el modo RTL y h para que cambie a LAND
#importas de dronekit connect, VehicleMode, LocationGlobal para despues utilizarlos en el codigo
#Mavproxy se llama en la terminal como mavproxy.py --master tcp:localhost:5760 --out udp:localhost:14551
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk
import time

def arm_and_takeoff(vehicle, TargetAltitude): #defines si el piloto ya esta listo y la altitud
    print("Running arm_and_takeoff")# imprime lo que le pusiste entre las comillas running arm_and_takeoff, print sirve para que imprima el mensaje o la variable

    while not vehicle.is_armable: #es un loop que dice si el piloto automatico no esta listo imprime el veiculo no esta listo espera y esto se imprime cada segundo hasta que este listo
       print("Vehicle is not armable, waiting...")
       time.sleep(1)#si no le pones tiempo de espera el mensaje se imprimira continuamente, este sirve para uqe cada que pase un segundo lo imprima y no se repita tant
    print("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")#cambia el modo del veiculo de stabilized a GUIDED

    print("WARNING motors arming...")
    vehicle.armed = True 

    while not vehicle.armed:
        print("waiting for arming...")
        time.sleep(1) # se epera 1 segundo para volver imprimir el mensaje

    print("WARNING Taking off")
    vehicle.simple_takeoff(TargetAltitude)#este comando es para despegar a la altitud objetivo

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt #esperan a que la altura sea segura antes de procesar la mision
        print("Altitude %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95): #si la altura es mayor o igual a el 95% de la altura desada imprime altura alcanzada y rompe el loop
            print("Altitude Reached, finished")
            break# Cuando llega a la atura requerida se rompe el loop y ya no imprime el mensaje
        
        time.sleep(1)

def set_velocity_body(vehicle, vx, vy, vz): #defines la variable de velocidad del drone, se mueve en el eje "x" y "y" y z no lo vamos a utilizar,  el eje "y" es hacia donde apunta la flecha del drone
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, 
            0, 0, 0,        #-- POSICION
            vx, vy, vz,     #-- VELOCIDAD
            0, 0, 0,        #-- ACCELERACION
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def key(event):#se define teclas para los eventos que se utilizan
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':#si presionas r entra al modo RTL y regresa al punto de despegue
            vehicle.mode = VehicleMode("RTL")#cambia de modo a RTL
            print("Modo RTL ejecutando")
        elif event.keysym == 'h':#si presionas h el drone se cambia a modo land y aterriza donde este el drone en ese momento, este es un punto extra
            vehicle.mode = VehicleMode("LAND")#el drone cambia a land
            print("Modo Land ejecutando")
    else: #-- non standard keys la y positiva es hacia donde apunta la flecha de inicio del drone
        if event.keysym == 'Up':#cuando presionas la tecla up (flecha para arriba) pone la velocidad del drone a 5m/s para arriba (eje y positiva)
            set_velocity_body(vehicle, 5, 0, 0)
        elif event.keysym == 'Down':#cuando presionas la tecla down (flecha para abajo) pone la velocidad del drone a -5m/s para abajo (eje y negativa)
            set_velocity_body(vehicle, -5, 0, 0)
        elif event.keysym == 'Left':#cuando presionas la tecla left (flecha para la izquierda) pone la velocidad del drone a -5m/s para la izquierda (eje x negativa)
            set_velocity_body(vehicle, 0, -5, 0)
        elif event.keysym == 'Right':#cuando presionas la tecla right (flecha para derecha) pone la velocidad del drone a 5m/s para derecha (eje x positiva)
            set_velocity_body(vehicle, 0, 5, 0)

def main():# se define la funcion main
    global vehicle #se define vehicle como global
    vehicle = connect('udp:127.0.0.1:14551', wait_ready=True)#  el dron lo conectas a el udp que es un protocolo sin internet, esta funciona con redes
    arm_and_takeoff(vehicle, 10)#arma el vehiculo y lo pone a Targetaltitude que es la altura en este caso 10m
    #vehicle.mode = VehicleMode("LAND")#cambia el modo del drone a land y hace que aterrise bajando la altura poco a poco
    root = tk.Tk()
    print(">> Control the drone with the arrow keys. Press r for RTL mode")
    root.bind_all('<Key>', key)
    root.mainloop() #entra a un loop de root
if __name__=="__main__": #Llama a la funcion main, si aparece esto si se guardo
     main()