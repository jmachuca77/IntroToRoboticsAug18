from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
def arm_and_takeoff(vehicle, TargetAltitude):
    print ("Runnung arm_and_take off")
 
    while not vehicle.is_armable: 
        print ("vehicle is not armable, waiting...")
        time.sleep(1)
        
        print ("changing to guided")
        vehicle.mode = VehicleMode("GUIDED")
        print("warning, motors arming")
        vehicle.armed = True

    while not vehicle.armed:
        print ("waiting for arming")
        time.sleep(1)
    print("warning, taking of")
     vehicle.simple_takeoff(TargetAltitude)
    while True: 
        currentAltitide = vehicle.location.global_relative_frame.alt
        print("altitude: %f" %currentAltitide)
        if currentAltitide >= (TargetAltitude*0.95):
            print("altitude reached")
            break




def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True)
    arm_and_takeoff(vehicle, 10)
if __name__=="__main__":
    main()



