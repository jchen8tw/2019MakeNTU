import RPi.GPIO as GPIO
import time
import test
trigger_pin_boxopen = 2
echo_pin_boxopen = 3
trigger_pin_up = 14
echo_pin_up = 15
trigger_pin_down = 17
echo_pin_down = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_boxopen, GPIO.OUT)
GPIO.setup(echo_pin_boxopen, GPIO.IN)
GPIO.setup(trigger_pin_up, GPIO.OUT)
GPIO.setup(echo_pin_up, GPIO.IN)
GPIO.setup(trigger_pin_down, GPIO.OUT)
GPIO.setup(echo_pin_down, GPIO.IN)

def send_trigger_pulse(trigger_pin):
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout, echo_pin):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance(trigger_pin, echo_pin):
    send_trigger_pulse(trigger_pin)
    wait_for_echo(True, 5000, echo_pin)
    start = time.time()
    wait_for_echo(False, 5000, echo_pin)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len * 340 *100 /2
    distance_in = distance_cm / 2.5
    return distance_cm

while True:
    dis_boxopen = get_distance(trigger_pin_boxopen,echo_pin_boxopen)
    dis_up = get_distance(trigger_pin_up,echo_pin_up)
    dis_down = get_distance(trigger_pin_down,echo_pin_down)
    if dis_boxopen > 30:
        #print("box is open!")
        #print("up:",get_distance(trigger_pin_up,echo_pin_up))
        #print("down: ",get_distance(trigger_pin_down,echo_pin_down))
        #print("up: ",dis_up)
        #print("down ",dis_down)
        if dis_up < 35 or dis_down < 35:
            print("this is so long fewiuhfiulwehfiuehfiluweahfuilewahfliaeufhwieuafhlieu")
            print(test.reko())
            time.sleep(5)
    else:
        pass
        #print("box is closed")
    #print('box distance', dis_boxopen)
    time.sleep(0.01)
