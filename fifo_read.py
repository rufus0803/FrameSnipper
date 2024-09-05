import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)


READ_SIGNAL_PIN = 18

GPIO.setup(READ_SIGNAL_PIN, GPIO.OUT)


FIFO_PATH = "fifo_read_orig"
if not os.path.exists(FIFO_PATH):
    os.mkfifo(FIFO_PATH)

def signal_read_pulse():
    GPIO.output(READ_SIGNAL_PIN, GPIO.HIGH)
    time.sleep(0.001) 
    GPIO.output(READ_SIGNAL_PIN, GPIO.LOW)

try:

    with open(FIFO_PATH, "r") as fifo:
        while True:

            data = fifo.readline()
            if data:
                print(f"{data.strip()}")
                signal_read_pulse() 
            else:
                time.sleep(0.01) 

except KeyboardInterrupt:
    print("Break")

finally:
    GPIO.cleanup()
