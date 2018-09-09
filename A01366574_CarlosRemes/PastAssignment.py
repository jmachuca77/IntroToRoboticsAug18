
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    while not vehicle.is_armable: 
        print ("vehicle is not armable, waiting...")
        time.sleep(1)

    print ("changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    print ("WARNING MOTORS ARMING")
    vehicle.armed = True

    while not vehicle.armed:
        print ("waiting for arming...")
        time.sleep(1)

    print("WARNING: taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print ("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude reached, Takeoff finished")
            break
            
        time.sleep(1)

def executeMission(vehicle):
    print ("executing mission")
    waypoint1 = LocationGlobalRelative(20.735371,-103.456121,20)
    vehicle.simple_goto(waypoint1)
    time.sleep(30)

    waypoint2 = LocationGlobalRelative(20.735517,-103.457538,20)
    vehicle.simple_goto(waypoint2)
    time.sleep(30)

    waypoint3 = LocationGlobalRelative(20.736438,-103.457430,20)
    vehicle.simple_goto(waypoint3)
    time.sleep(30)

    waypoint4 = LocationGlobalRelative(20.736303,-103.456085,20)
    vehicle.simple_goto(waypoint4)
    time.sleep(30)

    vehicle.simple_goto(waypoint1)
    time.sleep(30)

    home = LocationGlobalRelative(20.735917,-103.456639,20)
    vehicle.simple_goto(home)
    time.sleep(30)

     


def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True)
    arm_and_takeoff(vehicle,20)
    vehicle.airspeed = 10
    executeMission(vehicle)
    vehicle.mode = VehicleMode("LAND")
    battery = vehicle.battery
    print (battery)


if __name__ =="__main__":
    main()