from dronekit import connect, VehicleMode, LocationGlobalRelative 
import time 
 #poner en dronekit esta forma para que salga en el tec dronekit-sitl copter --home=20.736739,-103.457105,1641,5385

def arm_and_takeoff(vehicle, TargetAltitude):
    print("running arm_and_takeoff")
  
  
    while not vehicle.is_armable:
          print("vehicle not armable, waiting...")
          time.sleep(1)

    print("changing mode to guided")
    vehicle.mode = VehicleMode("GUIDED") 
       
    print("WARNING MOTORS ARMING")
    vehicle.armed = True
   
    while not vehicle.armed:
        print("waiting for arming...")
        time.sleep(1)

    print("warning taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude reached, Takeoff finished")
            break
            
        time.sleep(1)
    
def makemission(vehicle):
    print("making mission")
    waypoint =  LocationGlobalRelative(20.736739,-103.457105,19)
    vehicle.simple_goto(waypoint,13,13)
    print("point1")
    time.sleep(5)
    waypoint =  LocationGlobalRelative(20.736962,-103.457084,19)
    vehicle.simple_goto(waypoint,13,13)
    print("point2")
    time.sleep(10)
    waypoint =  LocationGlobalRelative(20.736930,-103.456847,19)
    vehicle.simple_goto(waypoint,13,13)
    print("point3")
    time.sleep(10)
    waypoint =  LocationGlobalRelative(20.736721,-103.456861,19)
    vehicle.simple_goto(waypoint,13,13)
    print("point4")
    time.sleep(10)
    waypoint =  LocationGlobalRelative(20.736739,-103.457105,19)
    vehicle.simple_goto(waypoint,13,13)
    print("point1")
    print("mission finished")
    time.sleep(10)

    

def batterystatus(vehicle):
    print ("battery: %f v" % vehicle.battery.voltage)
    
    

def main():
    
    vehicle = connect("udp:localhost:14551",wait_ready=True)
    
    arm_and_takeoff(vehicle, 10)
    makemission(vehicle)
    vehicle.mode = VehicleMode("LAND")
    print("Landing")
    time.sleep(23)
    print("Landed")
    time.sleep(2)
    batterystatus(vehicle)


if __name__ == "__main__":
    main()

