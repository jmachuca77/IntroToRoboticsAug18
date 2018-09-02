from dronekit import, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    while not vehicle.is_armable
        print ("Vehicle is not armable, waiting...")
        time.sleep(1)

        vehicle.armed = True 

        vehicle.simple_takeoff(TargetAltitude)

def main():
    vehicle connect ("udp.localhost:14551"wait_ready=True)

    arm_and_takeoff(vehicle, 10)

if __name__ == "__main__":
    main()
