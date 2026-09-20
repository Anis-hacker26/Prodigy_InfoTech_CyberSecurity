from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from keylogger_simulator import (
    KeyboardEvent,
    SessionLogger,
    create_event,
    format_event,
    format_session,
    generate_security_report,
    validate_event,
)


def test_create_normal_key_event():
    """Verify creation of a normal keyboard event."""
    event = create_event("A", "KEY")

    assert isinstance(event, KeyboardEvent)
    assert event.key == "A"
    assert event.event_type == "KEY"


def test_create_special_key_event():
    """Verify creation of an allowed special-key event."""
    event = create_event("ENTER", "SPECIAL")

    assert isinstance(event, KeyboardEvent)
    assert event.key == "ENTER"
    assert event.event_type == "SPECIAL"


def test_reject_empty_key():
    """Verify that empty keys are rejected."""
    with pytest.raises(ValueError):
        validate_event("", "KEY")


def test_reject_multi_character_normal_key():
    """Verify that KEY events contain exactly one character."""
    with pytest.raises(ValueError):
        validate_event("ABC", "KEY")


def test_reject_unknown_event_type():
    """Verify that unsupported event types are rejected."""
    with pytest.raises(ValueError):
        validate_event("A", "UNKNOWN")


def test_reject_unknown_special_key():
    """Verify that unsupported special keys are rejected."""
    with pytest.raises(ValueError):
        validate_event("F1", "SPECIAL")


def test_session_logger_records_events():
    """Verify that the session logger records simulated events."""
    logger = SessionLogger()

    logger.record("H", "KEY")
    logger.record("i", "KEY")
    logger.record("ENTER", "SPECIAL")

    assert logger.event_count() == 3
    assert len(logger.get_events()) == 3


def test_session_logger_clear():
    """Verify that clearing a session removes its events."""
    logger = SessionLogger()

    logger.record("A", "KEY")
    logger.record("B", "KEY")

    assert logger.event_count() == 2

    logger.clear()

    assert logger.event_count() == 0
    assert logger.get_events() == []


def test_format_normal_key():
    """Verify formatting of a normal key event."""
    event = create_event("A", "KEY")

    assert format_event(event) == "[KEY] A"


def test_format_special_key():
    """Verify formatting of a special key event."""
    event = create_event("SPACE", "SPECIAL")

    assert format_event(event) == "[SPACE]"


def test_format_session():
    """Verify formatting of multiple events."""
    logger = SessionLogger()

    logger.record("H", "KEY")
    logger.record("i", "KEY")
    logger.record("SPACE", "SPECIAL")
    logger.record("ENTER", "SPECIAL")

    expected = "\n".join(
        [
            "[KEY] H",
            "[KEY] i",
            "[SPACE]",
            "[ENTER]",
        ]
    )

    assert format_session(logger.get_events()) == expected


def test_format_empty_session():
    """Verify formatting of an empty session."""
    assert format_session([]) == "No keyboard events recorded."


def test_security_report():
    """Verify that the security report contains defensive information."""
    report = generate_security_report(10)

    assert "Simulated events analyzed: 10" in report
    assert "EDR" in report
    assert "MFA" in report
    assert "least-privilege" in report


def test_security_report_rejects_negative_count():
    """Verify that negative event counts are rejected."""
    with pytest.raises(ValueError):
        generate_security_report(-1)


def test_security_report_rejects_invalid_count():
    """Verify that non-integer event counts are rejected."""
    with pytest.raises(TypeError):
        generate_security_report("10")