#first of all, you have to start the dronekit simulator with the instruction: dronekit-sitl copter --home=20.735552,-103.456232,20,20 where the numbers oare the coordinates of the desired place of the simulation to start.
#next you declare de objects to import from the dronekit, which are the conecction, the drone simulator and the GPS ad the time counter in seconds
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#Here you define the procedure to be done by the command arm_and_takeoff
def arm_and_takeoff(vehicle, TargetAltitude): #here you declare that the procedure to be done when it arms and takeofss must be a connection with the simulatorand that the "drone" must rise to a certain height that you previously defined. 
    print('arming and taking off...') #you just notify what is happening.

    while not vehicle.is_armable: #This condition tells that while the vehicle is not fully connected it should show a message telling that until it works.
        print("not armable, waiting...")
        time.sleep(1)
    print("warning turning on motors!") #This message shows up when the connection is completed and the engines are ready to go.

    vehicle.mode = VehicleMode("GUIDED") #This sets the drone to the mode where it follows the precharged instructions.
    vehicle.armed = True #this stablishes the condition that something will happen just if the vehicle is ready to go.

    while not vehicle.armed: #Acts as the notifier that tells you if the vehicle is not ready.
        print ("Vehicle not armable, waiting...")
        time.sleep(1)

    vehicle.simple_takeoff(TargetAltitude) #This command tells the drone to reach a certain altitude preprogrammed.
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude:", currentAltitude) #The anterior loop tells the drone to get tehir specific altitude and show it.

        if currentAltitude >= TargetAltitude*0.95:
            print ("Altitude Reached, takeoff finished")
            break
        time.sleep(1) #It shows the message whenever the desired altitude is reached

def executeMission(vehicle): #In this instruction you define another instruction to be done by the drone.
    waypoint = LocationGlobalRelative(20.735631,-103.456892,20)#This ones are coordinates that the drone must reach and you give this values to the wayppoints#
    waypoint2 = LocationGlobalRelative(20.736136,-103.456748,20)
    waypoint3 = LocationGlobalRelative(20.736068,-103.456136,20)
    
    vehicle.simple_goto(waypoint) #This instruction tells the drone to go to an specific place designated by the the waypoint#
    print("traveling to waypoint1") #Thiss prints whenever the drone is traveling
    time.sleep(20) #This gives some time for the instruction to happen.
    #The rest set of instructions are the same as the previous one, but just tell the drone to go to another place.

    vehicle.simple_goto(waypoint2)
    print("traveling to waypoint2")
    time.sleep(20)

    vehicle.simple_goto(waypoint3)
    print("traveling to waypoint3")
    time.sleep(20)

def main(): #This part defines the main process and compiles the previous defined process and arranges them in a certain order to be done.
    vehicle = connect("udp:localhost:14551",wait_ready=True) #This instruction is to connect with the vehicle
    
    arm_and_takeoff(vehicle,10) #It tells to make the process of the takeoff previously defined to a certain altitude. Here you program the altitude to be reached.
    vehicle.airspeed = 10 #Sets the fly speed of the drone to the desired meters per second.
    executeMission(vehicle) #It tells the drone to carry on the previously defined process of the dislpacement of the drone. 
    vehicle.mode=VehicleMode("RTL") #sets the vehicle mode from GUIDED to RTL which means that the drone should return to the starting point and land.
    time.sleep(20)
    print "Battery: %s" % vehicle.battery.voltage #It shows the vehicle voltage after the mission finished.


if __name__=='__main__':
    main() #This stablishes that yoou can call this process in another programming session.