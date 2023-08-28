import os
import numpy as np
import matplotlib.pyplot as plt

def deserialize_log_line_to_data(log_line):
    motors = log_line[0:3]
    inputs = log_line[4:7]
    desired = log_line[8:11]
    timestamp = log_line[12]
    return motors, inputs, desired, timestamp

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

def get_most_recent_datetime(folder_path, file_prefix = 'motor_log_', file_extension=".csv"):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out only the files with the desired format and extension
    formatted_files = [file for file in files if file.startswith(file_prefix) and file.endswith(file_extension)]

    # Sort the files based on their modified timestamps (most recent first)
    sorted_files = sorted(formatted_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)

    # Get the most recent file
    if sorted_files:
        most_recent_file = sorted_files[0]
        datetime_str = most_recent_file[len(file_prefix):len(file_prefix) + len("YYYY-MM-DD_HH-MM-SS")]
        print(f"Loading data from file: motor_log_{datetime_str}.csv")
        return datetime_str
    else:
        return None
    
if __name__ == "__main__":
    #formatted_datetime = '2023-08-28_13-43-46'
    cwd = os.getcwd()
    folder_path = cwd + '/results'  # Access file folder
    formatted_datetime = get_most_recent_datetime(folder_path)
    file = f'results/motor_log_{formatted_datetime}.csv'
    log = np.loadtxt(file, delimiter=',', skiprows=1)

    # Indicates which motor we want to analyze.
    which_motor = 1

    # Data to plot.
    motors = []
    inputs = []
    desired = []
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
        motor_data, input_data, desired_data, timestamp_data = deserialize_log_line_to_data(line)
        motors.append(motor_data[which_motor])
        inputs.append(input_data[which_motor])
        desired.append(desired_data[which_motor])
        timestamps.append(timestamp_data)
        
    plot_multiple_graphs(timestamps, [motors, desired, inputs], ["current rad/s", "desired rad/s", "PWM"], formatted_datetime)



