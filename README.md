# Tom's Python Calculator

This is a simple calculator written in Python that runs in the terminal.

## What it does

It takes two numbers and an operator and gives a result. Then it asks again, looping until you quit. And it won't fall over if you typo a number.

## How it's built

- **Engine** — built first, using `def calc(a, op, b)` with if / elif / else inside to handle each operator.
- **Driver** — collects two numbers (floated) and an operator from the user, and hands back a result.
- **Loop** — keeps the calculator running so you can do more than one calculation, until you select the option to quit.
- **Guard** — a try/except that catches typos so a bad input doesn't crash the program.

## How to run it

From the folder where the file lives, run:

```
python calculator.py
```