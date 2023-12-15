import os

def getLogsPath():
    return getFolderPath('results/logs')

def getPlotsPath():
    return getFolderPath('results/plots')

def getResultsPath():
    return getFolderPath('results')

def getPWMPath():
    return getFolderPath('pwm_inputs')

def getFolderPath(subfolder):
    cur_path = os.getcwd()
    proj_path = os.path.abspath(os.path.join(cur_path, os.pardir, os.pardir))
    path = os.path.join(proj_path, subfolder)
    return path