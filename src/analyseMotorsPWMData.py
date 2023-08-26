import numpy as np
import matplotlib.pyplot as plt

def deserializeLogLineToData(log_line):
    motors = log_line[0:3]
    inputs = log_line[4:7]
    timestamp = log_line[8+4]
    return motors, inputs, timestamp

def plot_multiple_graphs(x_data, y_data_list, labels, formatted_datetime):
    plt.figure(figsize=(20, 10))  # Set the figure size
    
    for i, y_data in enumerate(y_data_list):
        plt.plot(x_data, y_data, marker=',', label=labels[i])
    
    plt.xlabel("TIME")
    plt.ylabel("MOTOR")
    plt.title("MOTOR X TIME")
    plt.legend()
    plt.grid(True)

    plt.savefig(fname=f'./results/motor_response_{formatted_datetime}.png')

if __name__ == "__main__":
    formatted_datetime = '2023-08-26_20-42-02'
    log = np.loadtxt(f'./results/motor_log_{formatted_datetime}.csv', delimiter=',', skiprows=1)

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
        motor_data, input_data, timestamp_data = deserializeLogLineToData(line)
        motors.append(motor_data[which_motor])
        inputs.append(input_data[which_motor])

        if (abs(input_data[which_motor] - last_input) > EPS_PWM) and (len(timestamps) > 0):
            initial_time_offset += last_timestamp
        timestamps.append(timestamp_data + initial_time_offset)
        
        last_timestamp = timestamp_data
        last_input = input_data[which_motor]

    plot_multiple_graphs(timestamps, [motors, inputs], ["motors", "inputs"], formatted_datetime)



