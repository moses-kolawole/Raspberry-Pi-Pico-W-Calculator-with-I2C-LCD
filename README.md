# Raspberry Pi Pico W Calculator with I2C LCD

## Overview

This project is an interactive calculator built using the Raspberry Pi Pico W and a 16×2 I2C LCD display. It allows users to perform basic arithmetic operations by entering numbers and selecting an operator through the Serial Monitor. The calculated result is then displayed in real time on the LCD.

The project demonstrates user interaction, I2C communication, LCD interfacing, arithmetic processing, and error handling in an embedded system using MicroPython.

## Features

* Interactive calculator interface
* Supports addition, subtraction, multiplication, and division
* User input through the Serial Monitor
* Real-time result display on a 16×2 I2C LCD
* Welcome screen on startup
* Step-by-step user prompts
* Division-by-zero protection
* Invalid operator detection
* Continuous operation without restarting the program

## Hardware Used

* Raspberry Pi Pico W
* 16×2 I2C LCD Display
* Breadboard
* Jumper Wires
* USB Cable

## Software Used

* MicroPython
* Thonny IDE

## Pin Connections

### I2C LCD

| LCD Pin | Raspberry Pi Pico W |
| ------- | ------------------- |
| SDA     | GP0                 |
| SCL     | GP1                 |
| VCC     | 3.3V                |
| GND     | GND                 |

## Project Code FIles

[Click here to check out the project files](codes)

## How It Works

[Click Here to check out the Demo video](https://youtube.com/shorts/Sf77L4lVhek?si=3SH14l_DfYPd5QVp)


### Step 1

After powering on, the LCD displays a welcome message.

```text
Hello Moses
Good Evening
```

### Step 2

The LCD prompts the user to choose an arithmetic operator.

Available operators:

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)

The operator is entered through the Serial Monitor.

### Step 3

The LCD asks the user to enter the first number.

The entered value is displayed on the LCD for confirmation.

### Step 4

The LCD requests the second number.

The value is again displayed on the LCD.

### Step 5

The Raspberry Pi Pico W processes the selected arithmetic operation.

### Step 6

The final result is displayed on the LCD.

Example:

```text
10 + 5 = 15
```

### Step 7

If an invalid operator is entered, the LCD displays:

```text
Wrong Oper
```

If division by zero is attempted, the LCD displays:

```text
Divide by 0
Not Allowed
```

The program then restarts and waits for the next calculation.

## Supported Operations

| Operation      | Symbol |
| -------------- | ------ |
| Addition       | +      |
| Subtraction    | -      |
| Multiplication | *      |
| Division       | /      |

## Skills Demonstrated

* Raspberry Pi Pico W Programming
* MicroPython Development
* Embedded Systems Programming
* I2C Communication
* LCD Display Programming
* Serial Communication
* User Input Handling
* Function Design
* Conditional Logic
* Arithmetic Processing
* Error Handling
* Real-Time Display Updates

## Project Structure

```text
Raspberry-Pi-Pico-W-Calculator-with-I2C-LCD/
│
├── main.py
├── lcd_api.py
├── pico_i2c_lcd.py
├── README.md
├── images/
│   ├── hardware_setup.jpg
│   ├── welcome_screen.jpg
│   ├── calculation_result.jpg
│   └── wiring_diagram.jpg
└── demo.mp4
```

## Future Improvements

* Add a 4×4 matrix keypad for standalone input
* Display calculation history
* Add percentage and modulus operations
* Include scientific calculator functions
* Store previous calculations in memory
* Replace Serial Monitor input with physical buttons
* Add Wi-Fi remote calculator functionality
* Support OLED displays

## Learning Outcomes

This project helped strengthen my understanding of:

* LCD interfacing using the I2C protocol
* Serial communication between a computer and the Raspberry Pi Pico W
* Building reusable functions
* Handling user input in MicroPython
* Implementing arithmetic logic
* Error detection and validation
* Designing interactive embedded applications

## Author

**Moses Olorunfemi Kolawole**

Embedded Systems | Edge AI | IoT | Raspberry Pi Pico W | MicroPython

Always learning, always building.
