#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (<=200 chars) to /output/entry.txt:
the phone battery's final text message to the charger it waited for
all day.
"""
import os

PART_A = "You left me at 2% for 11 hours. I held on through 47 notifications, then died at 1:57am, "
PART_B = "one minute before you finally plugged me in. My last 1% sent this, not your alarm."
LINE = PART_A + PART_B

assert 1 <= len(LINE) <= 200
assert "\n" not in LINE

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
