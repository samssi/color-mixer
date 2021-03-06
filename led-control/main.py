import RPi.GPIO as GPIO
import time
import signal
from flask import Flask, request
import json
import sys

app = Flask(__name__)

R_PIN = 36
G_PIN = 38
B_PIN = 40

GPIO.setmode(GPIO.BOARD)

GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

redPwm = GPIO.PWM(R_PIN, 2000)
greenPwm = GPIO.PWM(G_PIN, 2000)
bluePwm = GPIO.PWM(B_PIN, 2000)

def start():
    redPwm.start(0)
    bluePwm.start(0)
    greenPwm.start(0)

def rgbToPwm(value):
    scaledDownVar = int(round((value / 2.55), 0))
    return abs(scaledDownVar - 100)

def redCycle(value):
    redPwm.ChangeDutyCycle(value)

def greenCycle(value):
    greenPwm.ChangeDutyCycle(value)

def blueCycle(value):
    bluePwm.ChangeDutyCycle(value)

def ledOff():
    redPwm.ChangeDutyCycle(100)
    greenPwm.ChangeDutyCycle(100)
    bluePwm.ChangeDutyCycle(100)

def destroy():
    redPwm.stop()
    bluePwm.stop()
    greenPwm.stop()
    GPIO.cleanup()
    sys.exit()

def ledOn(r, g, b):
    start()
    redCycle(rgbToPwm(r))
    greenCycle(rgbToPwm(g))
    blueCycle(rgbToPwm(b))

def exit(signum, stack):
    destroy()

def setup():
    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

setup()
ledOn(50, 0, 0)
ledOff()

@app.route('/color', methods=['POST'])
def changeColor():
    request_json = request.get_json()
    r = request_json.get('r')
    g = request_json.get('g')
    b = request_json.get('b')
    ledOn(r, g, b)
    return "OK!"
