from dronekit import connect, VehicleMode, LocationGlobalRelative
import time#todo esto es lo que se importa de dronekit aqui
#al conectar dronekit se usaron las coordenadas de 20.736051, -103.456728,123,234


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
def executemision(vehicle):
    print("Excecuting mission")
    print("Exploring  the TEC")
    waypoint0 = LocationGlobalRelative(20.734917,-103.454843,10) #punto de la biblioteca
    waypoint5 = LocationGlobalRelative(20.736680,-103.454615,10)#punto en un jardin del tec
    waypoint1 = LocationGlobalRelative(20.735366,-103.456128,10)#primer punto del campo de fut
    waypoint2 = LocationGlobalRelative(20.735456,-103.457592,10)#segundo punto c.f
    waypoint3 = LocationGlobalRelative(20.736455,-103.457472,10)#tercer punto c.f
    waypoint4 = LocationGlobalRelative(20.736332,-103.456091,10)#cuarto punto de c.f
    waypoint6 = LocationGlobalRelative(20.736051,-103.456728,10)#punto de aterrizaje en campo de fut
#indicaciones para mover los drones a los puntos indicados anteriormente
    vehicle.simple_goto(waypoint0,10)#ejemplo: moviendose a punto 0 a 10 metros sobre segundo
    time.sleep(50)
    print("Library explored")

    vehicle.simple_goto(waypoint5,10)
    time.sleep(30)
    print("Fields explored")
    print("Going to the footbal camp")
    print("Iniziating square mision")

    vehicle.simple_goto(waypoint1,10)
    time.sleep(40)
    print("Reached point 1, square mision has started")

    vehicle.simple_goto(waypoint2,10)
    time.sleep(30)
    print("Reached point 2")

    vehicle.simple_goto(waypoint3,10)
    time.sleep(30)
    print("Reached point 3")

    vehicle.simple_goto(waypoint4,10)
    time.sleep(30)
    print("Reached point 4")

    vehicle.simple_goto(waypoint1,10)
    time.sleep(30)
    print("Reached point 1 and mission succeed, the square was made")
    print("velocity of the flight: 10m per second, going to landind point")

    vehicle.simple_goto(waypoint6,10)
    time.sleep(40)
    print("Drone on landing point preparing to land on the footbal camp")




def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)#conectar mavproxy al servidor escogido
    arm_and_takeoff(vehicle, 10)#ejecutar la funcion de arm adn takeoff
    executemision(vehicle)
    print("Battery:", vehicle.battery.voltage, "v")
    vehicle.mode= VehicleMode("LAND")#aterrizar de modo automatico el dron sin usar el pad de control.
    print("The dron has landed, mission completed")
    
if __name__== "__main__":
    main()#ejecutar todas las funciones dentro de la funcion main

