import time
import RPi.GPIO as GPIO


def main():
    GPIO.setmode(GPIO.BCM)
    print("Starting detection, press key !")
    for pin in range(1, 28):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        for pin in range(1, 28):
            if GPIO.input(pin) == 0:
                print('['+str(pin)+'] Pressed')
    time.sleep(0.1)

if __name__ == "__main__":
    main()
