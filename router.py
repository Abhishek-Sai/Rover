from sensor import sensorData
import serial
import time
global aold
# Base station coordinates
#ser1 = serial.Serial('/dev/ttyACM1', 115200, timeout=0.1)
def router():
    global aold
    x = sensorData()
    aold = x[2]
    time.sleep(2)
    while True:
        x = sensorData()
        a = x[2]
        rang = 0
        lang = 0
        final_ang = 120
        if a > aold:
            turn = a - aold
            if turn > 120:
                if rang <= 120:
                    rang = 240 - turn - lang
                    turn = 240 - turn  # anti_clockwise
                    final_ang = final_ang + turn
                    lang = 0
                    ser1.write(final_ang)
            elif turn < 120:
                if a > 120 and aold > 120:
                    rang = rang - turn
                    if rang <= 120:
                        turn = turn  # clockwise
                        final_ang = final_ang - turn
                        ser1.write(final_ang)
                elif a < 120 and aold < 120:
                    lang = lang + turn
                    if lang <= 120:
                        turn = turn  # clockwise
                        final_ang = final_ang - turn
                        ser1.write(final_ang)
                    elif lang > 120:
                        rang = 240 - turn - lang
                        turn = 240 - turn  # anti_clockwise
                        final_ang = final_ang + turn
                        lang = 0
                        ser1.write(final_ang)
        elif a < aold:
            turn = aold - a
            if turn > 120:
                if rang <= 120:
                    lang = 240 - turn - rang
                    turn = 240 - turn  # clockwise
                    final_ang = final_ang - turn
                    rang = 0
                    ser1.write(final_ang)
            elif turn < 120:
                if a < 120 and aold < 120:
                    lang = lang - turn
                    if lang <= 120:
                        turn = turn  # anti_clockwise
                        final_ang = final_ang + turn
                        ser1.write(final_ang)
                elif a > 120 and aold > 120:
                    rang = rang + turn
                    if rang <= 120:
                        turn = turn  # anti_clockwise
                        final_ang = final_ang + turn
                        ser1.write(final_ang)
                    elif rang > 120:
                        lang = 240 - turn - rang
                        turn = 240 - turn  # clockwise
                        final_ang = final_ang - turn
                        rang = 0
                        ser1.write(final_ang)
        aold = a
        if final_ang == 119 or final_ang == 100 or final_ang == 97 or final_ang == 115 or final_ang == 87 or final_ang == 68 or final_ang == 65 or final_ang == 83 or final_ang == 9:
            return final_ang+1
        else:
            return final_ang