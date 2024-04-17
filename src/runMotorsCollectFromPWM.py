from utils import *

def main():
    conn = Comm("199.0.1.1", 9600, 9601)

    pwms = Utils.getPWMValues(0)
    print(f"Loaded PWM values: {pwms}")

    conn.sendCommand(3, 3, 0.25, pwms)

if __name__ ==  "__main__":
    main()
