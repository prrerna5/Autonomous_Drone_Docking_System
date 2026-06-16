Connects Raspberry Pi to Pixhawk using DroneKit.


  

from dronekit import connect

CONNECTION_STRING = "/dev/ttyACM0"
BAUD_RATE = 57600

print("[INFO] Connecting to Pixhawk...")

vehicle = connect(
    CONNECTION_STRING,
    baud=BAUD_RATE,
    wait_ready=True
)

print("[SUCCESS] Connected Successfully")

print(vehicle.version)
print(vehicle.battery)

vehicle.close()
