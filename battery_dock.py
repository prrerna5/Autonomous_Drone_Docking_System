from dronekit import connect, VehicleMode
import time

BATTERY_THRESHOLD = 20

vehicle = connect(
    "/dev/ttyACM0",
    baud=57600,
    wait_ready=True
)

print("[INFO] Battery monitoring started...")

while True:

    battery = vehicle.battery.level

    print(f"Battery Level : {battery}%")

    if battery <= BATTERY_THRESHOLD:

        print("[WARNING] Low Battery")

        print("[INFO] Returning Home...")

        vehicle.mode = VehicleMode("RTL")

        while vehicle.armed:
            print("[INFO] Landing...")
            time.sleep(2)

        print("[SUCCESS] Drone docked successfully.")

        break

    time.sleep(5)

vehicle.close()
