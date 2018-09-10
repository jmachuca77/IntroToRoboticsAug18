from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

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

def excecuteMission(vehicle):
    print("Executing Mission") #mensaje de aviso
   
    waypointbase = LocationGlobalRelative(20.735886,-103.455731,20)
    waypoint1 = LocationGlobalRelative(20.735527,-103.456387,20) #puntos donde pasa
    waypoint2 = LocationGlobalRelative(20.735632,-103.457188,20)
    waypoint3 = LocationGlobalRelative(20.736210,-103.457104,20)
    waypoint4 = LocationGlobalRelative(20.736065,-103.456331,20)
    waypoint5 = LocationGlobalRelative(20.735527,-103.456387,20)
    
    vehicle.simple_goto(waypoint1,10) # Aqui va al primer punto para comenzar a hacer el cuadrado
    time.sleep(35)                    # tiempo para el viaje
    vehicle.simple_goto(waypoint2,10)
    time.sleep(35)
    vehicle.simple_goto(waypoint3,10)
    time.sleep(35)
    vehicle.simple_goto(waypoint4,10)
    time.sleep(35)
    vehicle.simple_goto(waypoint5,10)
    time.sleep(35)
    vehicle.simple_goto(waypointbase,10) # Aqui ya termino el viaje y va de regreso al punto incial, arriba del gym
    time.sleep(35)    
    
# Function used to test the functions in this file
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    arm_and_takeoff(vehicle, 10) #altura
    excecuteMission(vehicle)
    print("Battery:", vehicle.battery.voltage, "v") #voltaje de la bateria
    vehicle.mode = VehicleMode("LAND") #aterrizaje automatico

# if we included this file in another file then this code does not run by default,
# functions in this file in other files
if __name__ == "__main__":
    main()




# Lo logre <3