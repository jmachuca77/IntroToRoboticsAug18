from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
def arm_and_takeoff(vehicle, TargetAltitude):
    print("Arming an Taking off...")

    While not vehicle.is_armable:
    print("Not armable, waiting...")
    time.sleep(1)
print("WARMING TURNING ON MOTORS!")

vehicle.mode = VehicleMode ("GUIDE")
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
    def main():
        vehicle = connect("udp:localhost:14551", wait_ready=True=)
        arm_and_takeoff(vehicle, 10)
        if__name__=="__main__":
        main()