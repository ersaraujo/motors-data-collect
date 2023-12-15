import os
import matplotlib.pyplot as plt

def deserializeLogLineToData(log_line):
    motors = log_line[0:3]
    inputs = log_line[4:7]
    desired = log_line[8:11]
    timestamp = log_line[12]
    
    return motors, inputs, desired, timestamp

def plotMultipleGraphs(x_data, y_data_list, labels, formatted_datetime):
    plt.figure(figsize=(20, 10))

    for i, y_data in enumerate(y_data_list):
        plt.plot(x_data, y_data, marker=',', label=labels[i])

    plt.xlabel("TIME")
    plt.ylabel("MOTOR")
    plt.title("MOTOR X TIME")
    plt.legend()
    plt.grid(True)

    path = getResultsPath() + '/plots/motor_response_' + formatted_datetime

    plt.savefig(fname=path + '.png')

def getMostRecentFile(file_prefix = 'motor_log_', file_extension=".csv"):
    # Get the path to the folder
    path = getResultsPath() + '/logs'

    # List all files in the folder
    files = os.listdir(path)

    # Filter out only the files with the desired format and extension
    formatted_files = [file for file in files if file.startswith(file_prefix) and file.endswith(file_extension)]

    # Sort the files based on their modified timestamps (most recent first)
    sorted_files = sorted(formatted_files, key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=True)

    # Get the most recent file
    if sorted_files:
        most_recent_file = sorted_files[0]
        filepath = os.path.join(path, most_recent_file)
        datetime_str = most_recent_file[len(file_prefix):len(file_prefix) + len("YYYY-MM-DD_HH-MM-SS")]
        print(f"Loading data from file: moto_log_{datetime_str}.csv")
        return filepath, datetime_str
    else:
        return None, None
    
def getResultsPath(dir = '/results'):
    _path = os.getcwd()
    _path = _path.split('/')
    _path = '/'.join(_path[:-2])
    path = _path + dir
    return path