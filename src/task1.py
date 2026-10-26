"""Logic:-
We are using weighted centroid to find the line's position relative to the robot. 
Weights are sensors positions left to right. Weighted centroid: sum(w*r) / sum(r).
If it is 0->line in center
        -ve->line is left
        +ve->line is right

Each motor is clamped to maximum value while keeping the sign.
This is done to avoid sending too high values to motors which can damage them.
Using abs() on the limit means a negative 'max' argument cannot invert the logic.
"""


WEIGHTS = (-2, -1, 0, 1, 2)  # sensor positions, left to right


def line_position(readings, weights=WEIGHTS):
    """Weighted centroid: sum(w*r) / sum(r). Returns None if all readings are zero."""
    if len(readings) != len(weights):
        raise ValueError("need exactly %d readings" % len(weights))
    if any(r < 0 for r in readings):
        raise ValueError("readings must be non-negative")
    total = sum(readings)
    if total == 0:
        return None  # no line seen (avoids divide-by-zero)
    return sum(w * r for w, r in zip(weights, readings)) / total


def limit_motors(left, right, max_mag):
    """Clamp both commands to [-max_mag, +max_mag], keeping the sign."""
    m = abs(max_mag)

    def clamp(v):
        return max(-m, min(m, v))

    return clamp(left), clamp(right)


if __name__ == "__main__":
    print("--- line_position ---")
    for r in ([0, 0, 100, 0, 0], [0, 50, 100, 0, 0], [0, 0, 0, 80, 100],
              [100, 0, 0, 0, 0], [0, 0, 0, 0, 0]):
        print(r, "->", line_position(r))
    print("--- limit_motors (max 255) ---")
    for l, r in ((300, -80), (-400, 400), (120, 90), (0, -255)):
        print((l, r), "->", limit_motors(l, r, 255))



##Output:-
# --- line_position ---
# [0, 0, 100, 0, 0] -> 0.0
# [0, 50, 100, 0, 0] -> -0.3333333333333333
# [0, 0, 0, 80, 100] -> 1.5555555555555556
# [100, 0, 0, 0, 0] -> -2.0
# [0, 0, 0, 0, 0] -> None
# --- limit_motors (max 255) ---
# (300, -80) -> (255, -80)
# (-400, 400) -> (-255, 255)
# (120, 90) -> (120, 90)
# (0, -255) -> (0, -255)
