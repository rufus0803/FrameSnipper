import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BCM)


WRITE_SIGNAL_PIN = 17


GPIO.setup(WRITE_SIGNAL_PIN, GPIO.OUT)

FIFO_PATH = "fifo_write_orig"
if not os.path.exists(FIFO_PATH):
    os.mkfifo(FIFO_PATH)

def signal_write_pulse():
    GPIO.output(WRITE_SIGNAL_PIN, GPIO.HIGH)
    time.sleep(0.001) 
    GPIO.output(WRITE_SIGNAL_PIN, GPIO.LOW)

try:

    with open(FIFO_PATH, "w") as fifo:
        counter = 0
        while True:
          
            fifo.write(f"Data {counter}\n")
            fifo.flush()
            signal_write_pulse()  
            counter += 1
            time.sleep(0.1)  

except KeyboardInterrupt:
    print("Break")

finally:
    GPIO.cleanup()
