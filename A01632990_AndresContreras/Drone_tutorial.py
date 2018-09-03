from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

def arm_and_takeoff(vehicle, TargetAltitude):
    print("Arming and taking off...")

    while not vehicle.is_armable:
        print("Not armable, waiting...")
        time.sleep(1)
    print("WARNING TURNING ON MOTORS")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print ("Vehicle not armable, waiting...")
        time.sleep(1)
    print ("Warning taking off... ")
    vehicle.simple_takeoff(TargetAltitude)
    
    while True:
        currentAltitude = vehicle.location.global_relative_frame.alt
        print("Altitude: %f" % currentAltitude)

        if currentAltitude >= (TargetAltitude*0.95):
            print ("Altitude Reached, Take off f")
            break
        time.sleep(1) 

def executeMission(vehicle):
    print("Executing Mission...")
    waypoint = LocationGlobalRelative(20.737247,-103.457025, 10)
    waypoint2 = LocationGlobalRelative(20.737730,-103.457012, 10)
    waypoint3 = LocationGlobalRelative(20.737710,-103.456595, 10)
    waypoint4 = LocationGlobalRelative(20.737241,-103.456604, 10)
    #Lo anterior sirve para poner las localizaciones a donde se dirigira el dron a 10 ms para hacer el cuadrado
    vehicle.simple_goto(waypoint2,10)
    time.sleep(15)
    vehicle.simple_goto(waypoint3,10)
    time.sleep(15)
    vehicle.simple_goto(waypoint4,10)
    time.sleep(15)
    vehicle.simple_goto(waypoint,10)
    time.sleep(15)
    #Esto ayuda a poner la velocidad y el tiempo para que llegue el dron
    print("Battery:", vehicle.battery.voltage, "v")
    #Y con esto checas la bateria del dron 


def main():
    vehicle = connect("udp:localhost:14551", wait_ready=True)
    arm_and_takeoff(vehicle,10)
    executeMission(vehicle)
    vehicle.mode = VehicleMode("LAND")

if __name__=="__main__":
    main()