# Multitasker App

A menu-driven Python command-line app that brings together a collection of everyday calculators, basic math helpers, quick checks, and small games in one place. Choose an option from the numbered menu, enter the requested values, and the app prints the result in the terminal.

## Features

The app currently includes 15 tools:

1. **Rectangle area** — calculates area from the rectangle's length and breadth.
2. **Triangle hypotenuse** — calculates the hypotenuse from the base and perpendicular using the Pythagorean theorem.
3. **Multiplication table** — prints the table for a number from 1 to 10.
4. **Circle area or perimeter** — calculates either value from the radius.
5. **Even or odd** — checks whether an integer is even or odd.
6. **Simple calculator** — performs addition, subtraction, multiplication, or division on two numbers.
7. **Largest of three numbers** — compares three values and reports the largest.
8. **Character checker** — identifies an entered character as uppercase, lowercase, a digit, or a special character.
9. **Speed calculator** — calculates speed from distance and time.
10. **Velocity calculator** — calculates velocity from displacement, time, and a direction entered by the user.
11. **Dice roller** — rolls a six-sided die up to five times.
12. **Date and time** — displays the current date and time.
13. **BMI calculator** — calculates BMI from the entered weight and height.
14. **Number guessing game** — try to guess a randomly selected number from 10 to 50 in up to five attempts.
15. **Voting-age check** — checks whether the entered age is at least 18.

## Requirements

- Python 3
- `colorama` for colored terminal text

Install the dependency with:

```bash
python -m pip install colorama
```

## Run the app

From the directory containing `Multitasker.py`, run:

```bash
python Multitasker.py
```

Follow the on-screen prompts and enter the number for the tool you want to use. Enter `q` at the main menu to leave the current menu. The current program also attempts to import `Task_management_app` when leaving, so that module needs to be available in the Python import path for that handoff to work.

## Notes

- Enter numeric values when prompted for measurements or calculations.
- Speed and velocity use the distance units entered per second; for example, entering distance in metres gives a result in metres per second.
- BMI is normally calculated using weight in kilograms and height in metres. The current script reads both values as integers.
- This is a learning project and a simple terminal app. Some inputs, such as division by zero or invalid numeric text, are not yet handled with friendly validation.

## Built with

- Python standard library: `math`, `random`, `datetime`, `time`, and `os`
- [`colorama`](https://pypi.org/project/colorama/) for terminal colors

## Project

This project is a collection of small interactive utilities in a single menu-based program. It is intended for practice with Python functions, user input, conditionals, loops, arithmetic, and standard-library modules.
