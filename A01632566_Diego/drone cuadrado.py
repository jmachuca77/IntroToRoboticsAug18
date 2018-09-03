from dronekit import connect, VehicleMode, LocationGlobalRelative
import time#archivos importados dronekit 
#al conectar dronekit se usaron las coordenadas de 20.736051, -103.456728,123,234
def arm_and_takeoff(vehicle, TargetAltitude):#se preparan despegue y altura determinada
    print ("Arming and taking off...")
    while not vehicle.is_armable:#en caso de que el despegue falle, le dice al vehiculo que espere 
        print("Not armable, waiting...")
        time.sleep(1)
    print("Warning, turning on motors!")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed= True
    while not vehicle.armed:
        print("vehicle not armable, waiting...")
        time.sleep(1)#indica que el vehiculo no estalisto
    vehicle.simple_takeoff(TargetAltitude)
    while True:
      currentAltitude = vehicle.location.global_relative_frame.alt
      print("Altitude ", currentAltitude)#despliega altura del dron
      if currentAltitude >= TargetAltitude*0.95:
         print("Altitude Reached, Takeoff finished")
         break#hace que el vehiculo llegu casi a la altura indicada y deja de asender
      time.sleep(1)
def executemision(vehicle):
    print("Excecuting mission")
    print("sobrevolando el campus")
    waypoint0 = LocationGlobalRelative(20.7330609,-103.4541425,10) #cafeteria
    waypoint5 = LocationGlobalRelative(20.736680,-103.454615,10)#punto en un jardin del tec
    waypoint1 = LocationGlobalRelative(20.735366,-103.456128,10)#primer punto cancha de fut
    waypoint2 = LocationGlobalRelative(20.735456,-103.457592,10)#segundo punto c.f
    waypoint3 = LocationGlobalRelative(20.736455,-103.457472,10)#tercer punto c.f
    
    waypoint4 = LocationGlobalRelative(20.736332,-103.456091,10)#cuarto punto de c.f
    waypoint6 = LocationGlobalRelative(20.736051,-103.456728,10)#aterrizar en cancha de fut
#coordenadas para mover el dron
    vehicle.simple_goto(waypoint0,10)#vuelo a 10 metros por segundo
    time.sleep(50)
    print("cafeterya")
    vehicle.simple_goto(waypoint5,10)
    time.sleep(30)
    print('plants are ok')
    print("Going to field")
    print("covering perimeter")
    vehicle.simple_goto(waypoint1,10)
    time.sleep(40)
    print("fotball field reached, mission staring")
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
    print("mission succeed")
    print("preparing to land")
    vehicle.simple_goto(waypoint6,10)
    time.sleep(40)
    print("landing ongoing")
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)#conectar al servidor
    arm_and_takeoff(vehicle, 10)#ejecutar la funcion de arm adn takeoff
    executemision(vehicle)
    print("Battery:", vehicle.battery.voltage, "v")
    vehicle.mode= VehicleMode("LAND")#el dron aterriza.
    print("drone landed, mission succeed")
    
if __name__== "__main__":
    main()#ejecutar todo el contenido de main
