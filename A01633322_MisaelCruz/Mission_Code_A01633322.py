from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


def arm_and_takeoff(vehicle, TargetAltitude):   #Definimos arm_and_takeoff
    print("Running arm_and_takeoff")        #Avisamos que el dron esta encendido y preparandoce para despegar

    while not vehicle.is_armable:
        print("vehicle is not armable, waiting...")
        time.sleep(1)  #Se comprueba si que el drone esta armado

    print("Changing mode for GUIDED") #Cambiamos la configuración del drone a GUIDED
    vehicle.mode =VehicleMode("GUIDED")

    print("WARNING MOTORS ARMING") #Se avisa que los motores estan encendidos y hay que tener precaución
    vehicle.armed = True

    while not vehicle.armed: #En esta parte se verifica que el drone este armado
        print("Waiting for arming...") #Se imprime un mensaje diciendo que este se esra armando
        time.sleep(1) #Cuando por fin este armado dejara de aparecer el mensaje

    print("warning taking off") #Una vez terminado de verificar que el drone este armado con motores encendidos entonces
    vehicle.simple_takeoff(TargetAltitude) #Avisa que esta apunto de despegar

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude Reached, Takeoff finished")
            break

        time.sleep(1)

def executeMission(vehicle):
    print("Executing Mission") #Se imprime un mensaje diciendo que esta por ejecutar una mision
    waypoint1 = LocationGlobalRelative(20.736396, -103.457451,20) #Aqui se especifica los puntos por los
    waypoint2 = LocationGlobalRelative(20.735496, -103.457552,20) #Cuales se quier que el drone pase
    waypoint3 = LocationGlobalRelative(20.735376, -103.456116,20)
    waypoint4 = LocationGlobalRelative(20.736282, -103.456057,20)
    waypointinitial = LocationGlobalRelative(20.735864, -103.456779,20)
    squarep1 = LocationGlobalRelative(20.736031, -103.456601,20)
    squarep2 = LocationGlobalRelative(20.736031, -103.455644,20)
    squarep3 = LocationGlobalRelative(20.735134, -103.455644,20)
    squarep4 = LocationGlobalRelative(20.735129, -103.456603,20)
    libraryp = LocationGlobalRelative(20.735034, -103.454745,20)
    vehicle.simple_goto(waypoint1,10) #Apartir de aqui se coloca en orden los lugares por los cuales
    time.sleep(30)                    #se quiere que el drone pase, especificando su velocidad y el tiempo
    vehicle.simple_goto(waypoint2,10)
    time.sleep(30)
    vehicle.simple_goto(waypoint3,10)
    time.sleep(35)
    vehicle.simple_goto(waypoint4,10)
    time.sleep(30)
    vehicle.simple_goto(waypoint1,10)
    time.sleep(35)
    vehicle.simple_goto(waypointinitial,10) #Aqui termina de dar una vueltapor el perimetro de las canchas de futbol
    time.sleep(30)           #al terminar el recorrido regresa a su posición incial
    vehicle.simple_goto(squarep1,10)#En este mometo el drone incia su recorrido para hacer un cuadrado perfecto
    time.sleep(30)
    vehicle.simple_goto(squarep2,10)
    time.sleep(30)
    vehicle.simple_goto(squarep3,10)
    time.sleep(30)
    vehicle.simple_goto(squarep4,10)
    time.sleep(30)
    vehicle.simple_goto(squarep1,10)
    time.sleep(30)
    vehicle.simple_goto(waypointinitial,10) #Una vez concluido el cuadrado el drone regresa a la posicion incial
    time.sleep(30)
    vehicle.simple_goto(libraryp,10) #Para luego dirigirse a la biblioteca y regresar, dando por concluido el viaje
    time.sleep(40)
    vehicle.simple_goto(waypointinitial,10)
    time.sleep(40)
    print("Battery:", vehicle.battery.voltage, "V")#Nos despliega cuanto voltaje recibe el drone


def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True) #Se establece la conexion con mavproxy para poder controlar al drone

    arm_and_takeoff(vehicle, 10) #definimos la altura que tomara el drone
    executeMission(vehicle) #Aqui que executeMission llama a vehicle
    vehicle.mode = VehicleMode("LAND") #Cambiamos la configuración del drone a LAND para que aterrice sin necesidad de escribirlo en la terminal

if __name__ == "__main__":
    main() #hace que las funciones dentro de main sean ejecutadas
