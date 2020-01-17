from sensor import sensorData
import serial
import time
global aold
global lang
global rang
# Base station coordinates
ser1 = serial.Serial('COM6', 9600, timeout=0.1)
def router():
    global aold
    global lang
    global rang
    x = sensorData()
    aold = x[2]
    time.sleep(2)
    while True:
        x = sensorData()
        a = x[2]
        rang = 0
        lang = 0
        final_ang = 90
        if a > aold:
            turn = a - aold
            if turn > 90:
                if rang <= 90:
                    rang = 180 - turn - lang
                    turn = 180 - turn  # anti_clockwise
                    final_ang = final_ang + turn
                    lang = 0
                    ser1.write(final_ang)
            elif turn < 90:
                if a > 90 and aold > 90:
                    rang = rang - turn
                    if rang <= 90:
                        turn = turn  # clockwise
                        final_ang = final_ang - turn
                        ser1.write(final_ang)
                elif a < 90 and aold < 90:
                    lang = lang + turn
                    if lang <= 90:
                        turn = turn  # clockwise
                        final_ang = final_ang - turn
                        ser1.write(final_ang)
                    elif lang > 90:
                        rang = 180 - turn - lang
                        turn = 180 - turn  # anti_clockwise
                        final_ang = final_ang + turn
                        lang = 0
                        ser1.write(final_ang)
        elif a < aold:
            turn = aold - a
            if turn > 90:
                if rang <= 90:
                    lang = 180 - turn - rang
                    turn = 180 - turn  # clockwise
                    final_ang = final_ang - turn
                    rang = 0
                    ser1.write(final_ang)
            elif turn < 90:
                if a < 90 and aold < 90:
                    lang = lang - turn
                    if lang <= 90:
                        turn = turn  # anti_clockwise
                        final_ang = final_ang + turn
                        ser1.write(final_ang)
                elif a > 90 and aold > 90:
                    rang = rang + turn
                    if rang <= 90:
                        turn = turn  # anti_clockwise
                        final_ang = final_ang + turn
                        ser1.write(final_ang)
                    elif rang > 90:
                        lang = 180 - turn - rang
                        turn = 180 - turn  # clockwise
                        final_ang = final_ang - turn
                        rang = 0
                        ser1.write(final_ang)
        aold = a
        if final_ang == 85 or final_ang == 117 or final_ang == 73 or final_ang == 105 or final_ang == 74 or final_ang == 116 or final_ang == 75 or final_ang == 107 or final_ang == 80 or final_ang == 112 or  final_ang == 76 or final_ang == 108 or final_ang == 119 or final_ang == 100 or final_ang == 97 or final_ang == 115 or final_ang == 87 or final_ang == 68 or final_ang == 65 or final_ang == 83 or final_ang == 9:
            return final_ang+1
        else:
            return final_ang
