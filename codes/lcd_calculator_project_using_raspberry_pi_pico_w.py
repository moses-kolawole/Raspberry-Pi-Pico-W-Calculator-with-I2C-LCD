from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import time

def result_displayer(a, b, c, op):
    lcd.clear()

    lcd.move_to(2, 0)
    lcd.putstr("Final Result")

    lcd.move_to(0, 1)
    lcd.putstr(f"{a}{op}{b}={c}")


I2C_ADDR = 0x27
ROWS = 2
COLS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)

while True:

    lcd.clear()
    lcd.putstr("Hello Moses")

    lcd.move_to(0, 1)
    lcd.putstr("Good Evening")

    time.sleep(3)

    lcd.clear()
    lcd.putstr("Enter Oper")
    lcd.move_to(2, 1)
    lcd.putstr("+,-,*,/")

    operation_type = input("Enter operation (+,-,*,/): ").strip()

    lcd.clear()
    lcd.putstr(operation_type)

    time.sleep(2)

    lcd.clear()
    lcd.putstr("Enter No1")

    no1_input = float(input("Enter number 1: ").strip())

    lcd.move_to(0, 1)
    lcd.putstr(str(no1_input))

    time.sleep(2)

    lcd.clear()
    lcd.putstr("Enter No2")

    no2_input = float(input("Enter number 2: ").strip())

    lcd.move_to(0, 1)
    lcd.putstr(str(no2_input))

    time.sleep(2)

    if operation_type == "+":
        result = no1_input + no2_input
        result_displayer(no1_input, no2_input, result, operation_type)

    elif operation_type == "-":
        result = no1_input - no2_input
        result_displayer(no1_input, no2_input, result, operation_type)

    elif operation_type == "*":
        result = no1_input * no2_input
        result_displayer(no1_input, no2_input, result, operation_type)

    elif operation_type == "/":

        if no2_input != 0:
            result = no1_input / no2_input
            result_displayer(no1_input, no2_input, result, operation_type)

        else:
            lcd.clear()
            lcd.putstr("Divide by 0")
            lcd.move_to(0, 1)
            lcd.putstr("Not Allowed")

    else:
        lcd.clear()
        lcd.putstr("Wrong Oper")

    time.sleep(5)