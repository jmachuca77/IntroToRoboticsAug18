from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import time



def arm_and_takeoff (vehicle, TargetAltitude):
    print ("Arming and Taking off...")

    while not vehicle.is_armable:
           print ("Not armable, waiting...")  
           time.sleep(1)

    print ("Warning turning on motors") 

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed= True

    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
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
    print("Excecuting Mission")
    #waypoint = LocationGlobalRelative(-35.362270,149.165091,20)
    waypoint = LocationGlobalRelative(20.735517,-103.457499,30)
    vehicle.simple_goto(waypoint)
    time.sleep(30)


#Function used to test the function in thsi file
def main ():
    vehicle = connect ("udp:localhost:14551", wait_ready=True)
    init_point = LocationGlobal(20.735517,-103.457499,30)
    vehicle.home_location = init_point
    #vehicle.home_location=vehicle.location.global_frame
    
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()
    print " Home Location: %s" % vehicle.home_location

    arm_and_takeoff(vehicle,10)
    excecuteMission(vehicle)
    vehicle.mode = VehicleMode("LAND")

#Codigo agregado
if __name__== "__main__":
    main()

