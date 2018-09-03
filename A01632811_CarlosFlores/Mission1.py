#Bajar funciones necesarias
#import dronekit_sitl

#sitl = dronekit_sitl.start_default(20.735517, -103.457499)

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time




def arm_and_takeoff (vehicle, TargetAltitude): #arm the drone and then take off to the altitude choosen
    print ("Arming and Taking off...")

    while not vehicle.is_armable:
           print ("Not armable yet, waiting...")  
           time.sleep(1)

    print ("Warning turning on motors, stay away") 

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed= True

    while not vehicle.armed:
        print ("Waiting...")
        time.sleep(1)   

    vehicle.simple_takeoff(TargetAltitude)  

    
    while True: 
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude:", currentAltitude)

        if currentAltitude >= TargetAltitude*0.95:
            print("Altitude reached, Takeoff_finished")
            break 

        time.sleep(1)

def excecuteMission(vehicle):
    print("Starting mission")
    waypoint = LocationGlobalRelative(20.735517,-103.456775,30) #first point to reach
    waypoint2 = LocationGlobalRelative(20.735943,-103.456775,30) #second poitn to reach
    waypoint3 = LocationGlobalRelative (20.735943,-103.457499,30) #third point to reach
    waypoint4 = LocationGlobalRelative (20.735517, -103.457499,30) #final point to reach and also the starting point

    vehicle.simple_goto(waypoint)
    time.sleep(30)

   # print "Local Location: %s" % vehicle.location.local_frame

    vehicle.simple_goto(waypoint2)
    time.sleep(30)

    #print "Local Location: %s" % vehicle.location.local_frame (in case that you want to know the actual position)


    vehicle.simple_goto(waypoint3)
    time.sleep(30)

    #print "Local Location: %s" % vehicle.location.local_frame (in case that you want to know the actual position)

    vehicle.simple_goto(waypoint4)
    time.sleep(30)

    print "Local Location: %s" % vehicle.location.local_frame #this permit you to know tha actual position of the drone
    print "You are in the starting point, the drone will procede to land"  #When you finish it show this message 
   



#Function used to test the function in thsi file
def main ():
    vehicle = connect ("udp:localhost:14551", wait_ready=True)
    
    arm_and_takeoff(vehicle,10) #take off 
    excecuteMission(vehicle) #Do miision with the parameter establish before
    vehicle.airspeed = 10 #speed in meters/seconds, in this part the drone do not reach ten because of the longitud that it flies.
    time.sleep(30)    
    vehicle.mode = VehicleMode("LAND")
    time.sleep(30)
    print("Mission 1 completed...")
    print("Baterry Voltage:", vehicle.battery.voltage, "v") #print the voltage

if __name__== "__main__":
    main()