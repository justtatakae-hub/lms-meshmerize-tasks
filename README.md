# LMS / Meshmerize Selection Tasks

## Contents
- BOM/  : Task 4 (BOM, power block diagram), Task 5 (power budget, battery)
- docs/ : PDFs for Tasks 2, 3, 6, 7, 8, 9
- src/  : task1.py

## How to run
- Task 1: python3 src/task1.py
- Task 9 logic test: cd src/tests && g++ -std=c++11 -I.. test_core.cpp -o test_core && ./test_core
- Firmware: open src/line_follower.ino in Arduino IDE (ESP32 board package), upload.

## Assumptions
- Prices in BOM are estimates; verify before ordering.
- Motor and ESP32 current figures in Task 5 are estimates.
- Appendix A corrections: IN4 moved GPIO 11 -> GPIO 4 (GPIO 6-11 are flash pins);
  GPIO 25 is ADC2 (not ADC1), so BLE is used for diagnostics, not Wi-Fi.

## Limitations
- Core logic tested on a PC only. Firmware not yet tested on hardware.
- PID gains are starting values, not tuned.
