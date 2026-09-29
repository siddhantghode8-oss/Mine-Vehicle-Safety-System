"""
Mine Vehicle Safety System
SIH 2026 Prototype

This prototype uses simulated sensor values to demonstrate
the basic safety-risk decision logic.

No real hardware or AI model is connected yet.
"""


def calculate_risk(distance, visibility, object_detected):
    """
    Determine the current safety level.

    distance: estimated distance to detected object (meters)
    visibility: visibility condition from 0 to 100
                100 = clear, 0 = extremely poor
    object_detected: True if a relevant object is detected
    """

    if not object_detected:
        return "NORMAL"

    # Critical condition
    if distance <= 10 or visibility <= 20:
        return "CRITICAL"

    # Warning condition
    if distance <= 25 or visibility <= 40:
        return "WARNING"

    # Caution condition
    if distance <= 50 or visibility <= 60:
        return "CAUTION"

    return "NORMAL"


def main():
    print("=" * 50)
    print("   MINE VEHICLE SAFETY SYSTEM")
    print("   SIH 2026 Prototype")
    print("=" * 50)

    # Simulated sensor values
    distance = 30          # meters
    visibility = 45        # percentage
    object_detected = True

    print(f"\nObject detected : {object_detected}")
    print(f"Distance        : {distance} m")
    print(f"Visibility      : {visibility}%")

    risk_level = calculate_risk(
        distance,
        visibility,
        object_detected
    )

    print(f"\nSafety Level    : {risk_level}")

    if risk_level == "NORMAL":
        print("Status          : Safe operation")

    elif risk_level == "CAUTION":
        print("Status          : Maintain attention")

    elif risk_level == "WARNING":
        print("Status          : Reduce speed and stay alert")

    elif risk_level == "CRITICAL":
        print("Status          : Immediate hazard detected!")
        print("Action          : Apply configured emergency response")


if __name__ == "__main__":
    main()
