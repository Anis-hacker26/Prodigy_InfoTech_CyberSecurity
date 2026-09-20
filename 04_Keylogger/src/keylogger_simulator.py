"""
Educational Keylogger Simulator
--------------------------------

This module simulates keyboard events in a controlled environment.

It does NOT capture system-wide keyboard input, collect credentials,
run covertly, establish persistence, or transmit captured data.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class KeyboardEvent:
    """Represent one simulated keyboard event."""

    key: str
    event_type: str
    timestamp: datetime


ALLOWED_EVENT_TYPES = {"KEY", "SPECIAL"}

ALLOWED_SPECIAL_KEYS = {
    "SPACE",
    "ENTER",
    "BACKSPACE",
    "TAB",
}


def validate_event(key: str, event_type: str) -> None:
    """
    Validate a simulated keyboard event.

    Raises:
        TypeError: If key or event_type is not a string.
        ValueError: If the event contains unsupported values.
    """

    if not isinstance(key, str):
        raise TypeError("Key must be a string.")

    if not isinstance(event_type, str):
        raise TypeError("Event type must be a string.")

    if not key:
        raise ValueError("Key cannot be empty.")

    if event_type not in ALLOWED_EVENT_TYPES:
        raise ValueError(
            f"Unsupported event type: {event_type}. "
            f"Allowed types: {sorted(ALLOWED_EVENT_TYPES)}"
        )

    if event_type == "KEY":
        if len(key) != 1:
            raise ValueError(
                "KEY events must contain exactly one character."
            )

    if event_type == "SPECIAL":
        if key not in ALLOWED_SPECIAL_KEYS:
            raise ValueError(
                f"Unsupported special key: {key}. "
                f"Allowed keys: {sorted(ALLOWED_SPECIAL_KEYS)}"
            )


def create_event(key: str, event_type: str) -> KeyboardEvent:
    """Validate and create a simulated keyboard event."""

    validate_event(key, event_type)

    return KeyboardEvent(
        key=key,
        event_type=event_type,
        timestamp=datetime.now(),
    )

class SessionLogger:
    """Store simulated keyboard events for one controlled session."""

    def __init__(self) -> None:
        """Initialize an empty event session."""
        self.events: list[KeyboardEvent] = []

    def record_event(self, event: KeyboardEvent) -> None:
        """Record a validated keyboard event."""
        if not isinstance(event, KeyboardEvent):
            raise TypeError("Only KeyboardEvent objects can be recorded.")

        self.events.append(event)

    def record(self, key: str, event_type: str) -> KeyboardEvent:
        """Create and record a simulated keyboard event."""
        event = create_event(key, event_type)
        self.record_event(event)
        return event

    def get_events(self) -> list[KeyboardEvent]:
        """Return a copy of the current session events."""
        return list(self.events)

    def event_count(self) -> int:
        """Return the number of recorded events."""
        return len(self.events)

    def clear(self) -> None:
        """Clear all events from the current session."""
        self.events.clear()

def format_event(event: KeyboardEvent) -> str:
    """Convert a keyboard event into a readable log entry."""

    if not isinstance(event, KeyboardEvent):
        raise TypeError("Expected a KeyboardEvent object.")

    if event.event_type == "KEY":
        return f"[KEY] {event.key}"

    if event.event_type == "SPECIAL":
        return f"[{event.key}]"

    raise ValueError(f"Unsupported event type: {event.event_type}")


def format_session(events: list[KeyboardEvent]) -> str:
    """Format all events from a session into a readable report."""

    if not isinstance(events, list):
        raise TypeError("Events must be provided as a list.")

    if not events:
        return "No keyboard events recorded."

    return "\n".join(format_event(event) for event in events)

SECURITY_ANALYSIS = {
    "purpose": (
        "Demonstrate how keyboard-monitoring software "
        "could observe keyboard events."
    ),
    "risk": (
        "Unauthorized keystroke monitoring can expose "
        "sensitive information such as credentials."
    ),
    "mitigations": [
        "Use endpoint detection and response (EDR).",
        "Maintain updated anti-malware protection.",
        "Apply least-privilege access controls.",
        "Enable multi-factor authentication (MFA).",
        "Monitor unusual endpoint behavior.",
    ],
}


def generate_security_report(event_count: int) -> str:
    """Generate a defensive security analysis for the session."""

    if not isinstance(event_count, int):
        raise TypeError("Event count must be an integer.")

    if event_count < 0:
        raise ValueError("Event count cannot be negative.")

    lines = [
        "=" * 50,
        "           SECURITY ANALYSIS",
        "=" * 50,
        "",
        f"Simulated events analyzed: {event_count}",
        "",
        "Purpose:",
        SECURITY_ANALYSIS["purpose"],
        "",
        "Risk:",
        SECURITY_ANALYSIS["risk"],
        "",
        "Defensive mitigations:",
    ]

    for mitigation in SECURITY_ANALYSIS["mitigations"]:
        lines.append(f"- {mitigation}")

    return "\n".join(lines)

def run_demo() -> None:
    """Run a controlled keyboard-event simulation."""

    demo_events = [
        ("H", "KEY"),
        ("e", "KEY"),
        ("l", "KEY"),
        ("l", "KEY"),
        ("o", "KEY"),
        ("SPACE", "SPECIAL"),
        ("S", "KEY"),
        ("O", "KEY"),
        ("C", "KEY"),
        ("ENTER", "SPECIAL"),
    ]

    logger = SessionLogger()

    for key, event_type in demo_events:
        logger.record(key, event_type)

    print("\n" + "=" * 50)
    print("       EDUCATIONAL KEYLOGGER SIMULATOR")
    print("=" * 50)

    print("\nControlled simulated events:\n")
    print(format_session(logger.get_events()))

    print(f"\nTotal events: {logger.event_count()}")

    print("\n" + generate_security_report(logger.event_count()))


def main() -> None:
    """Application entry point."""

    run_demo()


if __name__ == "__main__":
    main()
