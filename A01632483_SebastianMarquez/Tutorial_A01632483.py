from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle, TarjetAltitude):
    print ("Arming and taking off...")

    while not vehicle.is_armable:
        print ("vehicle not armable. waiting...")
        time.sleep (1)
    
    print ("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    print ("WARNING MOTORS ARMING!")
    vehicle.armed = True
    
    while not vehicle.armed:
        print ("waiting for arming...")
        time.sleep(1)

    print ("WARNING! Taking off!")
    vehicle.simple_takeoff(TarjetAltitude)
    
    while True:
        currentaltitude = vehicle.location.global_relative_frame.alt
        print("Altitutude: %f" % currentaltitude)

        if currentaltitude == TarjetAltitude:
            print ("altitude Reached")
            break
        time.sleep(1)

#This was made thinking that the drone starts at 20.735320,-103.457706. This code basically makes the dorne move on a square with the use of four movements
def executeOrder66(vehicle):
    print("Palpatine just told the drone to execute order 66")
    waypoint1 = LocationGlobalRelative(20.735310,-103.457706,20)
    waypoint2 = LocationGlobalRelative(20.735310,-103.457716,20)
    waypoint3 = LocationGlobalRelative(20.735320,-103.457716,20)
    waypoint4 = LocationGlobalRelative(20.735320,-103.457706,20)

    vehicle.simple_goto(waypoint1)
    time.sleep(30)
    print("reached first point")
    vehicle.simple_goto(waypoint2)
    time.sleep(30)
    print("reached second point")
    vehicle.simple_goto(waypoint3)
    time.sleep(30)
    print("reached third point")
    vehicle.simple_goto(waypoint4)
    time.sleep(30)
    print("reached last point")

    

#This is the main funtion, first it connects to the drone on the especified direction, runs the arm and takeoff funtion and then makes the drone land.
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    
    arm_and_takeoff(vehicle, 10)
    executeOrder66(vehicle)

    vehicle.mode = VehicleMode("LAND")

if __name__== '__main__':
    main()
