from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle, TargetAltitude):

    print("Running arm_and_takeoff")
    while not vehicle.is_armable:
        
        print ("Vehicle not armable, waiting...")
        time.sleep(1)

    print("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True

    while not vehicle.armed:

        print("Waiting for arming...")
        time.sleep(1)

    print("WARNING, Taking off!")
    vehicle.simple_takeoff(TargetAltitude)

    while True:

        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print("Target altitude reached, Takeoff finished")
            break

        time.sleep(1)
    
def executeMission(vehicle):

    print("Executing mission...")
    waypoint = LocationGlobalRelative(-35.362270,149.165091,20)
    vehicle.simple_goto(waypoint)
    time.sleep(30)

def main():

    vehicle = connect("udp:localhost:14551",wait_ready=True)
    arm_and_takeoff(vehicle, 10)
    executeMission(vehicle)
    vehicle.mode = VehicleMode("LAND")

if __name__ == "__main__":
    
    main()