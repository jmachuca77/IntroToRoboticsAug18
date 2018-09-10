#this is the part of the code where you can get different functions that are inside of dronekit. One is to conect to the drone, the other is give the drone a mode to operate, the last is to have the altitude
from dronekit import connect, VehicleMode, LocationGlobalRelative
#this is to have time in our code
import time

#so in this function we are telling it to verify if the drone is armable every second, and if that answer is no the it will contunue to print our message
#Also TargetAltitude is the altitude we want our drone to take off to
def arm_and_takeoff(vehicle, TargetAltitude):
    print ("Arming a Take off...")

    while not vehicle.is_armable:
        print("Not armable, waiting...")
        time.sleep(1)
  
      
    print ("changing mode to GUIDED")
    #so here we are comunicating directly with the module console, and we are telling it to print it is guided when we execute the function
    vehicle.mode = VehicleMode("GUIDED")

    print ("WARNING TURNING ON MOTORS!")
    vehicle.armed = True 
#This loop is going to print the text as long as the vehicle isn't armed
    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    #since this print is outside of the while, it will print whit no condition telling it otherwise
    print ("WARNING! Taking off!")
    # We are telling it to take off at the altitude we already assigned
    vehicle.simple_takeoff(TargetAltitude)
    while True:
        #this is just give the altitude the drone is a name, and it will be constantly printing that value
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)
#This condition if, is saying that as long as the current altitude is less than or equal to our alreday established altitude*0.95, then print the message and stop printing the altitude thank to the break
        if currentAltitude >= TargetAltitude*0.95:
            print ("Altitude Reached, takeoff finished")
            break

        time.sleep(1)
#This chunk of code is saying that our function is going to move into a coordinate,with a delay, and a established speed. Of cousre since we are moving into difernt points the coordinates are the only values that will change
def executeMission(vehicle):
    print ("Executing Mission ")
    waypoint = LocationGlobalRelative(20.736341,-103.456778,20)
    vehicle.simple_goto(waypoint,10)
    time.sleep(30)

    waypoint2 = LocationGlobalRelative(20.735365,-103.456843,20)
    vehicle.simple_goto(waypoint2,10)
    time.sleep(30)

    waypoint3 = LocationGlobalRelative(20.735410,-103.457537,20)
    vehicle.simple_goto(waypoint3,10)
    time.sleep(30)

    waypoint4 = LocationGlobalRelative(20.736420,-103.457415,20)
    vehicle.simple_goto(waypoint4,10)
    time.sleep(30)
    #Ok, at this point I'am only printing the value of the battery voltage that my console gives me
    print ("Battery Voltage:", vehicle.battery.voltage,"v")
    

#Function to test he functions in this flie
def main():
    #here we are connecting to our sitl with it's IDP, and through the mavproxy port. the wait ready is going to let us know it is conected only when everything downloaded and ready to go
    vehicle = connect("udp:localhost:14551",wait_ready=True)
# here we going to tell it to begin with the mission, and then land it making the altitude go from the 20 we assigned to 0
    arm_and_takeoff(vehicle, 20)
    executeMission(vehicle)
    #This the same as in the other example where we told the console to print the mode it was it
    vehicle.mode = VehicleMode("LAND")
# Here we are simply stating that if the fucntions name is "main", the execute the function
if __name__=="__main__":
    main()