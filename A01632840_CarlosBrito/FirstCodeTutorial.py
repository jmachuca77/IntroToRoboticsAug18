from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
#Defines the arming of the drone and take off
def arm_and_takeoff(vehicle,TargetAltitude):
    print("Running arm and takeoff")
    #In case the vehicle is nor armable, the function is told to wait until it is armable
    while not vehicle.is_armable:
        print("Vehicle is not armable, waiting...")
        time.sleep(1)
    #Changes to the control mode
    print("Changing mode to GUIDED")
    vehicle.mode = VehicleMode("GUIDED")
    #Warning that the motors are indeed arming, and 
    print("WARNING MOTORS ARMING!")
    vehicle.armed = True
    #The function is told to wait until the vehicle is armed
    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)
    #Warning that the vehicle is elevating in the air, and the vehicle starts moving upwards
    print("WARNING Taking off")
    vehicle.simple_takeoff(TargetAltitude)

    while True:
        #Prints current altitude and also tells you which is the current altitude relative to your starting point
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude )
        #If the current altitude of the drone reaches %95 of the target altitude, it stops the while function
        if currentAltitude >= TargetAltitude*0.95:
            print("Altitude Reached, Takeoff finished")
            break       
        #waits one second
        time.sleep(1) 


def executeMission(vehicle):    
    #Defines the variables of the waypoints of the mission, as well as telling you the start of the mission
    print("Executing mission 66")
    TopRight= LocationGlobalRelative(20.736276, -103.456070, 20)
    TopLeft = LocationGlobalRelative(20.736276, -103.456692, 20)
    BotLeft = LocationGlobalRelative(20.735654, -103.456692 , 20)
    BotRight = LocationGlobalRelative(20.735654, -103.456070 , 20)
    CommandMitSpeed = LocationGlobalRelative(20.735809, -103.457403, 20)
    #calls the waypoints in the order to create a square
    vehicle.simple_goto(TopRight, 10)
    time.sleep(20)
    vehicle.simple_goto(TopLeft, 10)
    time.sleep(20)
    vehicle.simple_goto(BotLeft, 10)
    time.sleep(20)
    vehicle.simple_goto(BotRight, 10)
    time.sleep(20)
    vehicle.simple_goto(TopRight, 10)
    time.sleep(20)
    #Asks the drone for the voltage
    Voltage_vehicle = vehicle._voltage
    #Prints voltage    
    print("Battery Voltage: " + '%.2f' % float(Voltage_vehicle/1000.0) + "V")
    
    
#Main function defined, which includes the arming and take off of the drone, calling for the mission, and finally landing the bot
def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    arm_and_takeoff(vehicle,10)
    executeMission(vehicle)
    vehicle.mode = VehicleMode("LAND")

#calls the main function
if __name__ == "__main__":
    main()
