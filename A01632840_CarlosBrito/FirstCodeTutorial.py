from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle,TargetAltitude):
    print("Running arm and takeoff")

    while not vehicle.is_armable:
        print("Vehicle is not armable, waiting...")
        time.sleep(1)

    print("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("WARNING Taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude )
        
        if currentAltitude >= TargetAltitude*0.95:
            print("Altitude Reached, Takeoff finished")
            break       
        
        time.sleep(1) 


def executeMission(vehicle):
    print("Executing mission 66")
    waypoint1 = LocationGlobalRelative(20.735827, -103.455555, 20)
    waypoint2 = LocationGlobalRelative(20.735827, -103.455800, 20)
    waypoint3 = LocationGlobalRelative(20.736072, -103.455800, 20)
    waypoint4 = LocationGlobalRelative(20.736072, -103.455555, 20)
    waypoint5 = LocationGlobalRelative(20.735827, -103.455555, 20)
    vehicle.simple_goto(waypoint1)
    time.sleep(20)
    vehicle.simple_goto(waypoint2)
    time.sleep(20)
    vehicle.simple_goto(waypoint3)
    time.sleep(20)
    vehicle.simple_goto(waypoint4)
    time.sleep(20)
    vehicle.simple_goto(waypoint5)
    time.sleep(20)

def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    
    arm_and_takeoff(vehicle,10)
    executeMission(vehicle)
    vehicle.mode = VehicleMode("LAND")

if __name__ == "__main__":
    main()
