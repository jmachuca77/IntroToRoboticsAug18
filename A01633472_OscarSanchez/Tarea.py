#First you have to import connect, VehicleMode, LocationGlobalRelative and time from dronekit that will be used for the code.
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#Then you have to define the variable arm_and_takeoff which its arguments are vehicle and TargetAtltitude.
#When this variable activates it will print the message "Running arm_and_takeoff".
def arm_and_takeoff(vehicle, TargetAltitude):
    print("Running arm_and_takeoff")

    # The while not function means that if the vehicle is not armable it will print the message "Vehicle not armable, waiting...". And with the time.sleep it will wait 1 second.
    while not vehicle.is_armable:
        print("Vehicle not armable, waiting...")
        time.sleep(1)

    #If this function is false it will print the message "Changing mode to GUIDED" After this you have to comunicate to the program that the mode of the vehicle has change to "GUIDED".
    print("Changign mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")

    #Next it will print the message "WARNING MOTORS ARMING!". And set the property .armed to True.
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True

    #If the property vehicled.armed is False then it will print the message "Waiting for arming,..". And it will wait 1 second.
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    #If this function is false then it will print the message "WARNING! Taking off!". And with the property .simple_takeoff the program will receive the value of the target altitude.
    print("WARNING! Taking off!")
    vehicle.simple_takeoff(TargetAltitude)
    
    #If this is True then you will assigned the altitude of the location of the vehicle to the variable currentAltitude. And it will be printed the altitude. 
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        #Inside this while function is a conditional function if that say that if the currentAltitude is greater or equal to the TargetAltitude times 0.95 it will print the message: "Altitude Reached, Takeoff finished".
        #Is 0.95 because the value we want for the altitude will never get exactly to it so it get to the most aproximate value.
        #Finally it this happens without errors with the break function is going to stop the loop.
        if currentAltitude >= (TargetAltitude*0.95):
            print("Altitude Reached, Takeoff finished")
            break
        #It will wait 1 seconf for each value printed.
        time.sleep(1)


#Then you defined a second variable excecuteSquare which contain the moves of the drone will make in order to get to the initial point, inside of the arguments is vehicle.
def excecuteSquare(vehicle):
#First it will be print the message "Excecuting and the move"
#Then waypoint gets the global relative location in the map
#Then with the property .simple_gotto the drone will go to the point marked before with and altitude of 10 m/s.
#Finally wthe time.sleep it will wait 35 seconds until the drone has reached that point.

#This process repeasts itself 4 times because we want 4 moves in order to get an square.

    print("Excecuting First Move")
    (waypoint1) = LocationGlobalRelative(20.736292,-103.455978,25)
    vehicle.simple_goto(waypoint1,10)
    time.sleep(35)

    print("Excecuting Second Move")
    (waypoint2) = LocationGlobalRelative(20.735281,-103.456082,25)
    vehicle.simple_goto(waypoint2,10)
    time.sleep(35)

    print("Excecuting Thrid Move")
    (waypoint3) = LocationGlobalRelative(20.735391,-103.456831,25)
    vehicle.simple_goto(waypoint3,10)
    time.sleep(35)

    print("Excecuting Last Move")
    (waypoint4) = LocationGlobalRelative(20.736334,-103.456695,25)
    vehicle.simple_goto(waypoint4,10)
    time.sleep(35)

    #After the drone passes the 4 points it will be printed the battery voltage.
    print("Battery Voltage:", vehicle.battery.voltage)

#Finally you have to define the main variable which ejecute the declared variables.
#The ip direction of the silt to the drone and wait for be True
def main():
    vehicle = connect("udp:localhost:14551",wait_ready=True)

#Here are the variables declared before (arm_and_takeoff and excecuteSquare) that will ejecuted its functions. Then you have to set the mode LAND for the vehicle mode.
    arm_and_takeoff(vehicle, 25)
    excecuteSquare(vehicle)
    vehicle.mode = VehicleMode("LAND")
    
#If the name of the function is equal to "main" then it will ejecute the function main
if __name__ == "__main__":
    main()
