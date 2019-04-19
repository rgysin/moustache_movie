#!/usr/bin/env python

from simple_pid import PID
import time
import numpy as np
import matplotlib.pyplot as plt

class Motor:
    def __init__(self):
        self.length = 76
        self.speed = 0

    # Ideally this is some sort of actual measurement
    def update(self, power, dt):
        self.speed = power
        self.length += self.speed * dt
        return self.length

if __name__ == "__main__":
    motor = Motor()
    length = motor.length

    pid = PID(5, 0.01, 0.1, setpoint=length)
    pid.output_limits = (-100, 100)

    start_time = time.time()
    last_time = start_time

    # keep track of values for plotting
    power, setpoint, y, x = [], [], [], []

    while time.time() - start_time < 10:
        current_time = time.time()
        dt = current_time - last_time

        accel = pid(length)
        length = motor.update(accel, dt)

        x += [current_time-start_time]
        y += [length]
        setpoint += [pid.setpoint]
        power += [accel]

        if current_time - start_time > 1:
            pid.setpoint = 75

        last_time = current_time

    plt.plot(x, y, label='measured')
    plt.plot(x, setpoint, label='target')
    plt.plot(x, power, label='power')
    plt.axis([0, 10, -125, 125])
    plt.xlabel('time')
    plt.ylabel('length')
    plt.legend()
    plt.show()
