from dronekit import connect, VehicleMode, LocationGlobalRelative
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


    while not vehicle.armed:# se Confirma que el vehículo está armado antes de despegar 
        print("waiting for arming...")
        time.sleep(1) 

    print("WARNING Taking off")
    vehicle.simple_takeoff(TargetAltitude)#este comando es para despegar a la altitud objetivo

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt #esperan a que la altura sea segura antes de procesar la mision
        print("Altitude %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95): #si la altura es mayor o igual a el 95% de la altura desada imprime altura alcanzada y rompe el loop
            print("Altitude Reached, finished")
            break
        
        time.sleep(1)
    
def excecuteMission(vehicle):#Esta es la parte de la mision para hacer un cuadrado
    print("Ejecutando mision")
    waypointinicio = LocationGlobalRelative (20.736297, -103.455971, 10)#poner latitud, longitud de la cordenada y la altitud respectivamente en los parentesis 
    vehicle.simple_goto(waypointinicio,10)#el vehiculo va a la cordenada waypoint a una velocidad de 10 m/s pero casi nunca se va a esta velocidad el drone regula la velocidad a una adecuada
    time.sleep(10) #puse duermete o espera 10 segundo por si antes no estaba en el punto de inicio tenga tiempo de llegar y comenzar desde este punto
    waypoint5 = LocationGlobalRelative (20.735185, -103.455178,10)# en estas siguientes tres cordenadas viaja a 2 puntos del tec
    vehicle.simple_goto(waypoint5,10)
    time.sleep(35)
    waypoint6= LocationGlobalRelative (20.734938, -103.455887,10)
    vehicle.simple_goto(waypoint6,10)
    time.sleep(25)
    waypointinicio = LocationGlobalRelative (20.736297, -103.455971, 10)
    vehicle.simple_goto(waypointinicio,10)
    time.sleep(30)# es el tiempo que se desplaza para llegar al punto de inicio y empezar la mision semi cuadrado
    waypoint = LocationGlobalRelative(20.735432,-103.456115, 10 )#Empieza hacer la mision del cuadrado
    vehicle.simple_goto(waypoint,10)
    time.sleep(25)#los 25 es que se espere este tiempo (25 segundos) para hacer la otra accion
    waypoint2 = LocationGlobalRelative (20.735533, -103.457436, 10)#los waypoint los nombre de una manera diferente y cada uno esotra cordenada
    vehicle.simple_goto(waypoint2, 10)
    time.sleep(25)
    waypoint3 = LocationGlobalRelative (20.736364, -103.457304,10)
    vehicle.simple_goto(waypoint3, 10)
    time.sleep(25)
    waypointinicio = LocationGlobalRelative (20.736297, -103.455971, 10)
    vehicle.simple_goto(waypointinicio,10)
    time.sleep(25)# despues de dar la vuelta a todo el campo de futbol regresa al punto "home" establecido en dronekit y aterriza
# lo siguiente es una funcion que llama a todas las funciones que estan adentro de esta
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)#  el dron lo conectas a el udp que es un protocolo sin internet funciona con redes
    arm_and_takeoff(vehicle, 10)#arma el vehiculo y lo pone a Targetaltitude que es la altura en este caso 10m
    excecuteMission(vehicle)#declaramos la mision adentro de main para que se pueda realizar
    vehicle.mode = VehicleMode("LAND")#cambia el modo del drone a land y hace que aterrise bajando la altura poco a poco
    print("Mision cumplida el dron aterrizo con exito, Battery voltage:", vehicle.battery.voltage, "V") #aqui pido que me muestre el voltage de la bateria despes de realizar la mision

if __name__=="__main__": #Llama a la funcion main
    main()


