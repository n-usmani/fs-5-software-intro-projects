import matplotlib.pyplot as plt
import numpy as np
import statistics
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

# SETUP ===============
K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)
# end SETUP ===========

# create lists ========
velocities = []
errors = []
time = []

avg_velocities = []
avg_errors = []
K_Ps = []
K_Is = []
K_Ds = []
# end create lists ===

for k_p in range(30):

    for k_i in range(30):

        for k_d in range(30):

            # we've entered a 3-way combo. making fresh vars:
            car = make_car(desired_v=20.0, dt=0.1)
            velocities = []
            errors = []
            time = []

            # now let's run 550 steps with this combo
            for this_step in range(STEPS):
                # append curr velocity and curr time
                velocities.append(car["v"])
                time.append(car["t"])

                # get error & desired accel
                err_desired_accel = calculate_desired_acceleration(car, K_P, K_I, K_D)
                throttle_perc = err_desired_accel[1]



                # END STEPS LOOP

            K_D += 0.1
            K_Ds.append(K_P)
            # END k_d LOOP

        K_I += 0.1
        K_Is.append(K_P)
        # END k_i LOOP

    K_P += 0.1
    K_Ps.append(K_P)
    # END k_p LOOP