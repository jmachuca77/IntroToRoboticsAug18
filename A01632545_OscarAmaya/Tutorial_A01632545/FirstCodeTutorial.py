from dronekit import, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    while not vehicle.is_armable
        print ("Vehicle is not armable, waiting...")
        time.sleep(1)

        print ("Changing mode to GUIDED")
        vehicle.mode = VehicleMode("GUIDED")

        print ("WARNING MOTORS ARMING")
        vehicle.armed = True 
        
        while not vehicle.armed
        print ("Waiting for arming...")
        time.sleep (1)

        print("WARNING! Taking off")
        vehicle.simple_takeoff(TargetAltitude)

    while True:
       
         currentAltitude = vehicle.location.global_relative_frame.atl
         print ("Altitude: %f",currentAltitude)

         if currentAltitude >= TargetAltitude*0.95
         print ("Altitude Reached")
            break

        time.sleep(1)

def fly (vehicle):
    print ("Flying")
    waypoint = LocationGlobalRelative (20.8,-103.5,19)
    vehicle.simple_goto (waypoint,13,13)
    print ("reached point 1")
    time.sleep(3)
    waypoint = LocationGlobalRelative (20.8,-103.5,19)
    print ("reached point 2")
    time.sleep(3)
    waypoint = LocationGlobalRelative (20.8,-103.5,19)
    print ("reached point 3")
    time.sleep(3)
    waypoint = LocationGlobalRelative (20.8,-103.5,19)
    print ("reached point 4")
    time.sleep(15)
    print ("You succesfully made a square")

def batterystatus(vehicle)
    vehicle.battery 
    print ("The voltage of the battery is: 13.5v")

def main ():
    vehicle = connect("udp:localhost:14551",wait_ready = True)
    arm_and_takeoff (vehicle,10)
    makemission(vehicle)
    vehicle.mode = VehicleMode("LAND")
    print batterystatus

    







def main():
    vehicle connect ("udp.localhost:14551"wait_ready=True)

    arm_and_takeoff(vehicle, 10)
    vehicle.mode = VehicleMode("LAND")

if __name__ == "__main__":
    main()
