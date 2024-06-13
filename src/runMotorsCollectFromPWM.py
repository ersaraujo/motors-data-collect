from utils import *

m10 = [0.0, -18.0, 18.0,  18.0,  -18.0, -22.0, 22.0, 22.0,  -22.0, 0.0]
m20 = [0.0, -18.0, 18.0,  -18.0, 18.0,  -22.0, 22.0, -22.0, 22.0, 0.0]
m30 = [0.0, 18.0,  -18.0, -18.0, 18.0,  22.0, -22.0, -22.0, 22.0, 0.0]
m40 = [0.0, 18.0,  -18.0, 18.0,  -18.0, 22.0, -22.0, 22.0,  -22.0, 0.0]

# Grupo0.0,  M11, M21, M31, M41
m11 = [0.0, -16.0, 16.0, 16.0, -16.0, -20.0, 20.0, 20.0, -20.0, 0.0]
m21 = [0.0, -16.0, 16.0, -16.0, 16.0, -20.0, 20.0, -20.0, 20.0, 0.0]
m31 = [0.0, 16.0, -16.0, -16.0, 16.0, 20.0, -20.0, -20.0, 20.0, 0.0]
m41 = [0.0, 16.0, -16.0, 16.0, -16.0, 20.0, -20.0, 20.0, -20.0, 0.0]

# Grupo0.0,  M12, M22, M32, M42
m12 = [0.0, -17.8, 17.8, 17.8, -17.8, -21.8, 21.8, 21.8, -21.8, 0.0]
m22 = [0.0, -17.8, 17.8, -17.8, 17.8, -21.8, 21.8, -21.8, 21.8, 0.0]
m32 = [0.0, 17.8, -17.8, -17.8, 17.8, 21.8, -21.8, -21.8, 21.8, 0.0]
m42 = [0.0, 17.8, -17.8, 17.8, -17.8, 21.8, -21.8, 21.8, -21.8, 0.0]

# Grupo0.0,  M13, M23, M33, M43
m13 = [0.0, -19.6, 19.6, 19.6, -19.6, -23.6, 23.6, 23.6, -23.6, 0.0]
m23 = [0.0, -19.6, 19.6, -19.6, 19.6, -23.6, 23.6, -23.6, 23.6, 0.0]
m33 = [0.0, 19.6, -19.6, -19.6, 19.6, 23.6, -23.6, -23.6, 23.6, 0.0]
m43 = [0.0, 19.6, -19.6, 19.6, -19.6, 23.6, -23.6, 23.6, -23.6, 0.0]

# Grupo0.0,  M14, M24, M34, M44
m14 = [0.0, -21.4, 21.4, 21.4, -21.4, -25.4, 25.4, 25.4, -25.4, 0.0]
m24 = [0.0, -21.4, 21.4, -21.4, 21.4, -25.4, 25.4, -25.4, 25.4, 0.0]
m34 = [0.0, 21.4, -21.4, -21.4, 21.4, 25.4, -25.4, -25.4, 25.4, 0.0]
m44 = [0.0, 21.4, -21.4, 21.4, -21.4, 25.4, -25.4, 25.4, -25.4, 0.0]

# Grupo0.0,  M15, M25, M35, M45
m15 = [0.0, -23.2, 23.2, 23.2, -23.2, -17.2, 17.2, 17.2, -17.2, 0.0]
m25 = [0.0, -23.2, 23.2, -23.2, 23.2, -17.2, 17.2, -17.2, 17.2, 0.0]
m35 = [0.0, 23.2, -23.2, -23.2, 23.2, 17.2, -17.2, -17.2, 17.2, 0.0]
m45 = [0.0, 23.2, -23.2, 23.2, -23.2, 17.2, -17.2, 17.2, -17.2, 0.0]

def main():
    conn = Comm("199.0.1.1", 9600, 9601)

    # pwms = Utils.getPWMValues(0)
    # print(f"Loaded PWM values: {pwms}")

    conn.sendPWM(2, 2, m10, m20, m30, m40)
    time.sleep(10)

    conn.sendPWM(2, 2, m11, m21, m31, m41)
    time.sleep(10)

    conn.sendPWM(2, 2, m12, m22, m32, m42)
    time.sleep(10)

    conn.sendPWM(2, 2, m13, m23, m33, m43)
    time.sleep(10)

    conn.sendPWM(2, 2, m14, m24, m34, m44)
    time.sleep(10)

    conn.sendPWM(2, 2, m15, m25, m35, m45)
    time.sleep(10)


if __name__ ==  "__main__":
    main()
