#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound

import robot

robot = robot.Robot(host="192.168.43.124", port=2526)
robot.connect()

