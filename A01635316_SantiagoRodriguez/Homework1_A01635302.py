from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal   #This command imports some information regarding the drone.

import time    #This imports a function to enable delays in the code.

def Takeoff_procedure(vehicle, Hoveraltitude):  #This will define the takeoff before begining the mission.
    
    print("Begining take off")  #Just a warning
    vehicle.mode = VehicleMode("GUIDED")    #This tells the drone to enter GUIDED mode, this will allow the takeoff.
    
    print("Turning on motors")  #Also a warning
    vehicle.armed = True    #This tells the drone to turn on the motors.
    
    while not vehicle.armed:    #This code will make a delay so that the code isn't processed too fast & the drone has time to properly turn on.
        print("Please wait")
        time.sleep(4)
    
    vehicle.simple_takeoff(Hoveraltitude)   #This function will begin the lift off now that the motors are running & the drone is in GUIDED mode.
    
    while True:     #This will form an infinite loop to tell the altitude.

        currentAltitude = vehicle.location.global_relative_frame.alt    #A variable we call curentAltitude will be equal to the height of the drone.
        print("Altitude: %f" % currentAltitude)     #This will print the altitude of the drone.
        time.sleep(1)   #This delay will avoid annoying spamming of altitude updates.
        
        if currentAltitude >= (Hoveraltitude*0.97):     #This will compare the altitude with the wished altitude, the desiered altitude is reduced a tiny bit since the drone almost never reaches exactly the right altitude.
            
            print("Stable altitude reached")    #This message indicates we have reached the proper altitude.
            break   #This will break the loop.

def mission(vehicle):   #This defines the activities the drone has to do.

    waypoint1 = LocationGlobalRelative(20.736696,-103.456628,15)   #Line 32,33,34 & 35 define the location of the waypoints
    waypoint2 = LocationGlobalRelative(20.737114,-103.456584,15)
    waypoint3 = LocationGlobalRelative(20.737155,-103.457071,15)
    
    vehicle.simple_goto(waypoint1, groundspeed=10)   #Line 36-41 tell the drone to go to each waypoint at a speed of 10 m/s
    time.sleep(15)
    vehicle.simple_goto(waypoint2, groundspeed=10)
    time.sleep(15)
    vehicle.simple_goto(waypoint3, groundspeed=10)
    time.sleep(15)

def mission2(vehicle):

    waypoint4 = LocationGlobalRelative(20.736734,-103.457114,15)    #Line 45-47 also tell the drone to come back, the reason why this is in a different function is an error by Python.
    vehicle.simple_goto(waypoint4, groundspeed=10)
    time.sleep(15)

def land(vehicle):  #This will be the final instruction for the drone

    vehicle.mode = VehicleMode("LAND")  #This begins the LAND mode which lands the drone.
    time.sleep(30)
    print("The drone has landed")
    print "Battery: %s" % vehicle.battery   #This will tell us how much battery is left.

def main():    #This will define the main function, in here we'll execute most of the code.
    
    vehicle = connect("udp:localhost:14551",wait_ready=True)    #This will connect the drone & wait until it's ready
    Takeoff_procedure(vehicle, 15)   #This calls the Takeoff_procedure, in this case, it'll hover up to 15m.
    mission(vehicle)    #This will call the function "mission".
    mission2(vehicle)   #This will call the function "mission2".
    land(vehicle)   #This will land the vehicle by calling the "land" fucntion.

if __name__ == "__main__":    #This condition will execute our main function if the other programs are running.
    
    main()