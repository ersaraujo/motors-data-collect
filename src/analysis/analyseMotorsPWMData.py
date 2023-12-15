import numpy as np
import utils.motorplotlib as mp

if __name__ == "__main__":
    path, formatted_datetime = mp.getMostRecentFile()
    log = np.loadtxt(path, delimiter=',', skiprows=1)

    # Indicates which motor we want to analyze.
    which_motor = 0

    # Data to plot.
    motors = []
    inputs = []
    timestamps = []

    # Save the last input (PWM) we sent to robot.
    last_input = -100

    # Save the last timestamp of all sequence. 
    # Used to update the initial offset for each PWM round. 
    last_timestamp = 0

    # Initial time offset of a PWM round.
    initial_time_offset = 0

    # Tolerance between two rounds of PWM's input.
    EPS_PWM = 0.01

    # Select data on log.
    for line in log:
        motor_data, input_data, _, timestamp_data = mp.deserializeLogLineToData(line)
        motors.append(motor_data[which_motor])
        inputs.append(input_data[which_motor])

        if (abs(input_data[which_motor] - last_input) > EPS_PWM) and (len(timestamps) > 0):
            initial_time_offset += last_timestamp
        timestamps.append(timestamp_data + initial_time_offset)
        
        last_timestamp = timestamp_data
        last_input = input_data[which_motor]

    mp.plotMultipleGraphs(timestamps, [motors, inputs], ["motors", "inputs"], formatted_datetime)



