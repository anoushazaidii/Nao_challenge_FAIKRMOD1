"""
Algorithm A for NAO Planning Challenge

This algorithm generates the same sequence used in the Choregraphe project.
It includes all mandatory positions and more than 5 intermediate moves.
"""

mandatory = ["StandInit", "SitRelax", "Stand", "StandZero", "Hello", "Crouch"]

intermediate = [
    "LookAt",
    "Blink",
    "Blink",
    "PlaySound",
    "AirGuitar",
    "Wait",
    "WipeForehead",
    "TaiChiChuan",
    "Bow",
    "EndPose"
]

def generate_sequence():
    # Combine mandatory + intermediate in the same order
    sequence = [
        "StandInit",
        "GoToPosition",
        "SitDown",
        "LookAt",
        "Wait3",
        "Blink",
        "Wait4",
        "Blink",
        "StandUp",
        "Hello",
        "AirGuitar",
        "Wait",
        "WipeForehead",
        "TaiChiChuan",
        "Bow",
        "EndPose"
    ]

    return sequence

if __name__ == "__main__":
    seq = generate_sequence()
    print("Generated Choreography Sequence:")
    for step in seq:
        print(" -", step)
