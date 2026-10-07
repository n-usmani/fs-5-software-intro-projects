import matplotlib.pyplot as plt
import numpy as np
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 3.98
K_I = 0.1
K_D = 0.1

STEPS = 550

car = make_car(desired_v=20.0, dt=0.1)

# create lists
velocities = []
errors = []
time = []




# the STEPS loop
for this_step in range(STEPS): # [0, 550)
    velocities.append(car["v"]) # append velocity
    time.append(car["t"])

    # get error & desired accel
    err_desired_accel = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle_perc = err_desired_accel[1]

    errors.append(err_desired_accel[0]) # append error

    # addition for part 5: add error to net_error
    car["net integral"] += (err_desired_accel[0] * car["dt"])

    update(car, throttle_perc)
# end of STEPS loop

velocities = [round(x, 3) for x in velocities]
errors = [round(x, 4) for x in errors]

print(velocities[-1])
print(errors[-1])

plt.figure()
plt.plot(time, velocities)

plt.figure()
plt.plot(time, errors)

plt.show()