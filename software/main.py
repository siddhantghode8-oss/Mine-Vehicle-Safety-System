"""
Mine Vehicle Safety System
SIH 2026 Prototype

Prototype version using simulated sensor/perception inputs.
"""

from risk_engine import RiskEngine


def main():

    print("=" * 50)
    print("      MINE VEHICLE SAFETY SYSTEM")
    print("             SIH 2026")
    print("=" * 50)

    # Simulated inputs
    distance = 30          # Distance to object in meters
    visibility = 45        # Visibility percentage
    object_detected = True

    print("\n--- SENSOR / PERCEPTION DATA ---")
    print(f"Object detected : {object_detected}")
    print(f"Distance        : {distance} m")
    print(f"Visibility      : {visibility}%")

    # Create risk engine
    engine = RiskEngine()

    # Analyse risk
    risk_level = engine.evaluate(
        distance,
        visibility,
        object_detected
    )

    # Get recommended action
    action = engine.get_action(risk_level)

    print("\n--- SAFETY ANALYSIS ---")
    print(f"Risk level      : {risk_level}")
    print(f"Recommended     : {action}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
