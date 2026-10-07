"""
Descr: Observes final velocity and final error for 18 different
K_P's between 0.10 and 0.95, with step of 0.05 each time.
Generates matplotlib plots of K_P vs final velocity and
K_P vs final error
"""

import matplotlib.pyplot as plt
import numpy as np
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

# create lists
velocities = []
errors = []
time = []

final_velocities = []
final_errors = []
K_Ps = []


for ii in range(18): # <-- the K_P values loop
    # the STEPS loop

    car = make_car(desired_v=20.0, dt=0.1)
    velocities = []
    errors = []

    for this_step in range(STEPS): # [0, 550)
        velocities.append(car["v"]) # append velocity
        time.append(car["t"])

        # get error & desired accel
        err_desired_accel = calculate_desired_acceleration(car, K_P, K_I, K_D)
        throttle_perc = err_desired_accel[1]

        errors.append(err_desired_accel[0]) # append error

        update(car, throttle_perc)
    # end of STEPS loop

    velocities = [round(x, 3) for x in velocities]
    errors = [round(x, 4) for x in errors]

    # updating K_P and saving the final velocity and final error
    K_Ps.append(round(K_P, 2))
    final_velocities.append(velocities[STEPS - 1])
    final_errors.append(errors[STEPS - 1])
    K_P += 0.05


print(final_velocities)
print(final_errors)

plt.figure()
plt.plot(K_Ps, final_velocities)
plt.figure()
plt.plot(K_Ps, final_errors)
plt.show()

"""
plt.figure()
plt.plot(time, velocities)

plt.figure()
plt.plot(time, errors)

plt.show()
"""

# just to see
# print(velocities)
# print(errors)



# 