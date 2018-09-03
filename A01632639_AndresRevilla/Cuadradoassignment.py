from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
    def arm_and_takeoff(vehicle, TargetAltitude): #Defines the variable arm_and_takeoff
        print("Running arm_and_takeoff") #Lets us know the drone is on and ready for takeoff
            while not vehicle.is_armable:
                print("vehicle is not armable, patiently waiting...")
                time.sleep(1) #waits a second to see if the drone is armed
            print("Changing to GUIDED") #Warning that the drone will change to guided mode
        vehicle.mode =VehicleMode("GUIDED")
            print("WARNING MOTORS STARTING ONE STEP AWAY PLEASE") #Warning that the motors are starting
        vehicle.armed = True
            while not vehicle.armed: #Verifying if the drone is armed
                print("Waiting for arming...:v") #The drone is arming
                time.sleep(1) #The last message disappears when it is armed
            print("WARNING UP AND AWAY") #After verifying everything its ready 
        vehicle.simple_takeoff(TargetAltitude) #The drone will take off
            while True:
                    currentAltitude = vehicle.location.globla_relative_frame.alt
                    print("Altitude: %f" % currentAltitude)
                        if currentAltitude >= (TargetAltitude*0.95):
                            print("Altitude reached, Takeoff Done")
                            break
                        time.sleep(1)
def executeMission(vehicle):
    print("Mission Beginning") #It tells you the mission is starting
    waypoint1 = LocationGlobalRelative(20.736396, -103.477451,20) #Specifing the way the drone will go  
    waypoint2 = LocationGlobalRelative(20.735496, -103.457552,20)
    waypoint3 = LocationGlobalRelative(20.735376, -103.456116,20)
    waypoint4 = LocationGlobalRelative(20.736282, -103.456057,20)
    waypointinitial = LocationGlobalRelative(20.735864, -103.456779,20)
    square1 = LocationGlobalRelative(20.736031, -103.456601,20)
    square2 = LocationGlobalRelative(20.736031, -103.455644,20)
    square3 = LocationGlobalRelative(20.735134, -103.455644,20) 
    square4 = LocationGlobalRelative(20.735129, -103.456603,20) 
    biblio = LocationGlobalRelative(20.735034, -103.454745,20)  
    vehicle.simple_goto(waypoint1,10) #You place the waypoints in order specifying time and velocity
    time.sleep(30)
    vehicle.simple_goto(waypoint2,10) #This is for the Football courts assignment
    time.sleep(30)
    vehicle.simple_goto(waypoint3,10) 
    time.sleep(30)
    vehicle.simple_goto(waypoint4,10) 
    time.sleep(30)
    vehicle.simple_goto(waypoint1,10) 
    time.sleep(30)
    vehicle.simple_goto(square1,10) #this is for the square
    time.sleep(30)
    vehicle.simple_goto(square2,10) 
    time.sleep(30)
    vehicle.simple_goto(square3,10) 
    time.sleep(30)
    vehicle.simple_goto(square4,10) 
    time.sleep(30)
    vehicle.simple_goto(square1,10) 
    time.sleep(30)
    vehicle.simple_goto(waypointinitial,10) #it goes to the start
    time.sleep(30)
    vehicle.simple_goto(biblio,10) #then it heads to the library
    time.sleep(30)
    vehicle.simple_goto(waypointinitial,10) 
    time.sleep(30)
    print("Battery: ", vehicle.battery.voltage, " V") #it shows the battery left
def main():
    vehicle = connect("udp:localhost:14441", wait_ready:True) #connects to mavproxy
        arm_and_takeoff(vehicle, 10) #Altitude
    executeMission(vehicle) 
    vehicle.mode : VehicleMode("LAND") #This makes the drone land without a command
if _name_ == "_main_":
    main() #main executes