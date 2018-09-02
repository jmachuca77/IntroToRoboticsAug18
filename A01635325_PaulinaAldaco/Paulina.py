from dronekit import connect, VehicleMode, LocationGlobalRelative 
#imports functions connect(to connect to the drone),
#VehicleMode(sets mode for drone),
#and LocationGlobalRelative(gives altitude for drone)
import time
#imposts time function so that you can create delays

def arm_and_takeoff(vehicle, TargetAltitude):
#defines the function arm_and_takeoff which recieves the target altitude and includes the object vehicle
    print('Running arm and takeoff')
    #prints the message
    
    while not vehicle.is_armable:
    #while the vehicle is not ready to arm
        print('Vehicle is not armable, waiting...')
        
        time.sleep(1)
        #waits one second
    #waits for the vehicle to be armable before continuing
    
    print('Changing mode to GUIDED')
    vehicle.mode = VehicleMode('GUIDED')
    #changes the mode to guided
    
    print('WARNING: motors arming')
    vehicle.armed = True
    #arms the vehicle
    
    while not vehicle.armed:
    #while the vehicle isn't armed
        print ('Waiting for arming...')
        
        time.sleep(1)
        #waits one second
    #waits for the vehicle to be armed
    
    print('WARNING: taking off')
    vehicle.simple_takeoff(TargetAltitude)
    #takes off to the target altitude
    
    while True:
    #endlessly runs loop
        currentAltitude = vehicle.location.global_relative_frame.alt
        #assigns the variable currentAltitude the value of the altitude reltive to the starting point
        print('Altitude: %f' % currentAltitude)
        #prints the message and the value of the variable

        if currentAltitude >= (TargetAltitude*0.95):
        #checks if currentAltitude is greater than or equal to 95% of TargetAltitude
            print('Altitude reached, takeoff finished')
            
            break
            #stops the loop
        
        time.sleep(1)
        #waits one second

def executeMission(vehicle):
#defines the function executeMission which includes the object vehicle
    print('Executing mission')
    
    vehicle.airspeed = 10
    #changes the airspeed to 10 m/s

    waypoint = LocationGlobalRelative(20.736177,-103.456495,10)
    waypoint2 = LocationGlobalRelative(20.735818,-103.456495,10)
    waypoint3 = LocationGlobalRelative(20.735818,-103.456136,10)
    waypoint4 = LocationGlobalRelative(20.736177,-103.456136,10)
    #assigns a location to waypoint, waypoint2, waypoint3, and waypoint4
    
    vehicle.simple_goto(waypoint)
    #moves the drone to waypoint
    time.sleep(14)
    #waits 18 seconds

    vehicle.simple_goto(waypoint2)
    time.sleep(14)

    vehicle.simple_goto(waypoint3)
    time.sleep(14)

    vehicle.simple_goto(waypoint4)
    time.sleep(14)

    print('Mission executed')

def main():
#defines the main function
    
    vehicle = connect('udp:localhost:14551',wait_ready=True)
    #creates an object to store the vehicle
    #connects it to a drone via udp, localhost is the ip address and 14551 is the port
    #wait_ready tells the function connect that it is ready only when it has downloaded only when it has all the information it needs from the drone
    
    arm_and_takeoff(vehicle, 10)
    #calls the function and takes off to 10 meters

    executeMission(vehicle)
    #calls the function

    vehicle.mode = VehicleMode('LAND')
    #assigns the mode LAND and lands the vehicle
    print('Vehicle has landed')

    print('Battery voltage: %s' % vehicle.battery.voltage)
    #prints the battery voltage

if __name__ == '__main__':
    main()
#it will only run the main function when the program is executed stand alone
#this allows other functions to be reused in other files
