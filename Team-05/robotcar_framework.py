import random
import time

# Robot settings
SAFE_DISTANCE = 30
LOW_BATTERY = 20

battery = 100


def read_distance_sensor():
    """Simulate an ultrasonic sensor."""
    return random.randint(10, 100)


def move_forward():
    print("🤖 Moving forward")


def turn_left():
    print("↩️ Turning left")


def turn_right():
    print("↪️ Turning right")


def stop():
    print("🛑 Robot stopped")


def check_battery():
    global battery
    battery -= 5
    return battery


# Main robot loop
while battery > LOW_BATTERY:

    distance = read_distance_sensor()
    battery = check_battery()

    print(f"\nDistance: {distance} cm")
    print(f"Battery: {battery}%")

    if distance < 20:
        stop()
        print("Obstacle very close!")

        # Choose a direction randomly
        if random.choice([True, False]):
            turn_left()
        else:
            turn_right()

    elif distance < SAFE_DISTANCE:
        print("Obstacle nearby")
        turn_right()

    else:
        move_forward()

    time.sleep(1)

stop()
print("Battery low. Returning to charging station...")
    
    