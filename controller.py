#!/usr/bin/env python

from simple_pid import PID
import time
import numpy as np
import matplotlib.pyplot as plt

class Vehicle:
    def __init__(self):
        self.speed = 0

    # Ideally this is some sort of actual measurement
    def update(self, acceleration, dt):
        self.speed += acceleration*dt
        return self.speed

if __name__ == "__main__":
    vehicle= Vehicle()
    speed = vehicle.speed

    pid = PID(5, 0.01, 0.1, setpoint=speed)
    pid.output_limits = (0, 100)

    start_time = time.time()
    last_time = start_time

    # keep track of values for plotting
    acceleration, setpoint, y, x = [], [], [], []

    while time.time() - start_time < 10:
        current_time = time.time()
        dt = current_time - last_time

        accel = pid(speed)
        speed = vehicle.update(accel, dt)

        x += [current_time-start_time]
        y += [speed]
        setpoint += [pid.setpoint]
        acceleration += [accel]

        if current_time - start_time > 1:
            pid.setpoint = 75

        last_time = current_time

    plt.plot(x, y, label='measured')
    plt.plot(x, setpoint, label='target')
    plt.plot(x, acceleration, label='acceleration')
    plt.axis([0, 10, 0, 125])
    plt.xlabel('time')
    plt.ylabel('speed')
    plt.legend
    plt.show()
