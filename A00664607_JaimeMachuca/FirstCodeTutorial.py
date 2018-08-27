from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# This function is used to make the copter takeoff to a certain altitude
# It takes a vehicle object as an argument, and the target altitude to reach 
def arm_and_takeoff(vehicle, TargetAltitude):
    print ("Arming and Taking off...")

    while not vehicle.is_armable:
        print ("Not armable, waiting...")
        time.sleep(1)

    print ("WARNING TURNING ON MOTORS!")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)

    vehicle.simple_takeoff(TargetAltitude)

    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: ", currentAltitude)

        if currentAltitude >= TargetAltitude*0.95:
            print ("Altitude Reached")
            break

        time.sleep(1)

# Function used to test the functions in this file
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    arm_and_takeoff(vehicle, 10)
    vehicle.mode = VehicleMode("LAND")

# This code is added so that if we run this file stand alone in python then the Main function is called
# if we include this file in another file then this code does not run by default, and we can then use the
# functions in this file in other files.
if __name__ == "__main__":
    main()
