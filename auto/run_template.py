import matplotlib.pyplot as plt
import numpy as np
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 2.0
K_I = 0.2
K_D = 0.0

STEPS = 550

car = make_car(desired_v=20.0, dt=0.1)
car["error_prev"] = 0

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

    # for part 6: update error_prev term
    if this_step > 0: car["error_prev"] = errors[-1]

    errors.append(err_desired_accel[0]) # append error

    # addition for part 5: add error to net_error
    car["net_integral"] += (err_desired_accel[0] * car["dt"])
    

    update(car, throttle_perc)
# end of STEPS loop

velocities = [round(x, 3) for x in velocities]
errors = [round(x, 4) for x in errors]

print("Final Velocity: " + str(velocities[-1]))
print("Final Error: " + str(errors[-1]))

plt.figure()
plt.plot(time, velocities)

plt.figure()
plt.plot(time, errors)

plt.show()