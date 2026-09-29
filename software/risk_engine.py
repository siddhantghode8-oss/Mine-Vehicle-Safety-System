"""
Mine Vehicle Safety System
Risk Analysis Engine

This module converts sensor/perception inputs
into a safety level.
"""


class RiskEngine:

    def __init__(self):
        self.levels = [
            "NORMAL",
            "CAUTION",
            "WARNING",
            "CRITICAL"
        ]

    def evaluate(self, distance, visibility, object_detected):
        """
        Evaluate the current risk condition.

        distance:
            Distance to detected object in meters.

        visibility:
            Visibility percentage.
            100 = clear
            0 = extremely poor

        object_detected:
            True if an object/hazard is detected.
        """

        if not object_detected:
            return "NORMAL"

        if distance <= 10 or visibility <= 20:
            return "CRITICAL"

        if distance <= 25 or visibility <= 40:
            return "WARNING"

        if distance <= 50 or visibility <= 60:
            return "CAUTION"

        return "NORMAL"

    def get_action(self, risk_level):

        actions = {
            "NORMAL": "Continue normal operation.",
            "CAUTION": "Maintain attention.",
            "WARNING": "Reduce speed and stay alert.",
            "CRITICAL": "Immediate hazard! Apply configured emergency response."
        }

        return actions.get(
            risk_level,
            "Unknown safety condition."
        )
