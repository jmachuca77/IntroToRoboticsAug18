#here is to begin the importing of connect, VehicleMode, LocationGlobalRelative and time from dronekit.
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#now we are defining the variable arm_and_takeoff and this variable is getting the altitude to be printed as running.
def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    #here is to print a message that the vehicle is not armed yet. Then it waits for a second.
    while not vehicle.is_armable:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    
    #here is to print that the mode has been changed and to comunicate the program that the mode of the vehicle will change into guided.
    print ("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    #here is to comunicate to the program to show a warning, when the vehicle is already armed.
    print ("WARNING MOTORS ARMING")
    vehicle.armed = True

    #in this step is to show a waiting while the vehicle is not completely armed. Then it waits for a second.
    while not vehicle.armed:
        print ("Waiting for arming...")
        time.sleep(1)
    #here is to indicate that the drone is starting the journey and to show and warning in the screen.
    print ("WARNING, Taking off")
    vehicle.simple_takeoff(TargetAltitude)
    #here is to know what the altitude of the drone is and print it in the screen.
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print ("Altitude: %f" % currentAltitude)
        #now here is to recognize that the dron can't get the exactly altitude, but close to it yes. It prints a message that the dron got the correct altitude too. Finally the break ends a loop and wait for a second.
        if currentAltitude >= (TargetAltitude*0.95):
            print ("Altitude Reached, Takeoff finished")
            break 
        time.sleep(1)
#now this is to define the variable excecuteMission and print a message. This is also to order to the dron to make a square with four different points at a velocity of 10 meters per second and wait for 30 seconds for each movement between two points.
def excecuteMission(vehicle):
    print("Excecuting Mission")
    firstwaypoint = LocationGlobalRelative(20.735347,-103.456842,32)
    vehicle.simple_goto(firstwaypoint,10)
    time.sleep(30)

    secondwaypoint = LocationGlobalRelative(20.736330,-103.456744,32)
    vehicle.simple_goto(secondwaypoint,10)
    time.sleep(30)

    thirdwaypoint = LocationGlobalRelative(20.736402,-103.457417,32)
    vehicle.simple_goto(thirdwaypoint,10)
    time.sleep(30)

    fourthwaypoint = LocationGlobalRelative(20.735483,-103.457533,32)
    vehicle.simple_goto(fourthwaypoint,10)
    time.sleep(30)
    #now here is to print the state of voltage of the battery of the drone.
    print("Battery Voltage:", vehicle.battery.voltage)


#here we are defining the variable main, also here we are connecting the IP of the sitl to the drone.
def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True)

    arm_and_takeoff(vehicle, 32)
    excecuteMission(vehicle)
    vehicle.mode = VehicleMode("LAND")
#finally, here is to indicate that if the name of the function is equal to main, realize the main code.
if __name__=="__main__":
    main()
