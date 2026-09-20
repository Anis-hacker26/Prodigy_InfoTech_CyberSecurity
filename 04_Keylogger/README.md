# Task 04 — Simple Keylogger Simulator

## Overview

The **Simple Keylogger Simulator** is a Python-based cybersecurity project developed as part of the **Prodigy InfoTech Cyber Security Internship**.

This project demonstrates the fundamental concept of keyboard-event monitoring through a **controlled and simulated environment**. Instead of capturing real system-wide keystrokes, the application works with predefined keyboard events to demonstrate how keyboard activity can be represented, validated, recorded, formatted, and analyzed.

The project also explores the cybersecurity risks associated with unauthorized keylogging, including potential credential exposure, and highlights defensive controls such as **Endpoint Detection and Response (EDR), anti-malware protection, least-privilege access, Multi-Factor Authentication (MFA), and endpoint behavior monitoring**.

> **Security Disclaimer:** This project is an educational keylogger simulator. It does **not** capture system-wide keyboard input, collect real credentials, establish persistence, operate covertly, evade security controls, or transmit captured information.

---

## Objectives

The main objectives of this task are:

1. Understand the fundamental concept of keylogging.
2. Understand why unauthorized keylogging represents an endpoint-security risk.
3. Model keyboard events programmatically using Python.
4. Differentiate between normal and special keyboard events.
5. Validate simulated keyboard events before processing them.
6. Record events within a controlled session.
7. Format keyboard events into readable logs.
8. Generate a defensive cybersecurity analysis.
9. Understand the potential impact of credential exposure.
10. Identify defensive controls against malicious keylogging.
11. Implement error handling and input validation.
12. Validate the implementation using automated tests.
13. Practice secure and ethical cybersecurity development.
14. Document the implementation and testing process using GitHub and Markdown.

---

## Features

### 1. Keyboard Event Modeling

Each simulated keyboard action is represented using a `KeyboardEvent` dataclass.

Every event contains three primary attributes:

```text
key
event_type
timestamp
```

Example:

```python
KeyboardEvent(
    key="A",
    event_type="KEY",
    timestamp=...
)
```

This provides a structured representation of an individual simulated keyboard event.

---

### 2. Normal Key Event Handling

Normal keyboard characters are represented using the `KEY` event type.

Examples include:

```text
A
H
7
!
```

A normal `KEY` event must contain exactly one character.

Example:

```python
create_event("A", "KEY")
```

Invalid multi-character normal-key values such as:

```text
ABC
Hello
```

are rejected by the validation system.

---

### 3. Special Key Handling

The simulator supports predefined special keyboard events.

Supported special keys include:

```text
SPACE
ENTER
BACKSPACE
TAB
```

Example:

```python
create_event("ENTER", "SPECIAL")
```

Special events are displayed using a readable format.

Example:

```text
[ENTER]
```

Other supported examples include:

```text
[SPACE]
[BACKSPACE]
[TAB]
```

---

### 4. Event Validation

Every simulated keyboard event is validated before it can be created or recorded.

Supported event types are:

```text
KEY
SPECIAL
```

The validation system checks for:

- Empty key values
- Unsupported event types
- Multi-character normal keys
- Unsupported special keys
- Invalid key data types
- Invalid event-type data types

This ensures that malformed events cannot enter the simulated session.

---

### 5. Timestamped Event Creation

The `create_event()` function validates the supplied keyboard information and creates a timestamped `KeyboardEvent`.

Example:

```python
create_event("H", "KEY")
```

Special-key example:

```python
create_event("ENTER", "SPECIAL")
```

Each generated event receives a timestamp using Python's `datetime` functionality.

---

### 6. Session-Based Event Logging

The `SessionLogger` class manages simulated keyboard events during the current application session.

The session logger can:

- Record events
- Retrieve recorded events
- Count events
- Clear recorded events

Example:

```python
logger = SessionLogger()

logger.record("H", "KEY")
logger.record("i", "KEY")
logger.record("ENTER", "SPECIAL")
```

The logger can then report:

```text
Event count: 3
```

The application does not create a permanent database of captured keystrokes.

---

### 7. Event Formatting

The application converts simulated keyboard events into a readable event-log format.

Normal key:

```text
[KEY] A
```

Special key:

```text
[ENTER]
```

Example session:

```text
[KEY] H
[KEY] e
[KEY] l
[KEY] l
[KEY] o
[SPACE]
[KEY] S
[KEY] O
[KEY] C
[ENTER]
```

This representation makes the simulated keyboard activity easier to analyze.

---

### 8. Security Analysis

After processing the simulated keyboard events, the application generates a defensive security report.

The report includes:

- Number of simulated events analyzed
- Purpose of the simulation
- Security risks associated with unauthorized keylogging
- Defensive mitigation recommendations

Example:

```text
==================================================
           SECURITY ANALYSIS
==================================================

Simulated events analyzed: 10

Purpose:
Demonstrate how keyboard-monitoring software could
observe keyboard events.

Risk:
Unauthorized keystroke monitoring can expose
sensitive information such as credentials.
```

---

### 9. Defensive Mitigation Recommendations

The security report includes several defensive recommendations:

```text
- Use endpoint detection and response (EDR).
- Maintain updated anti-malware protection.
- Apply least-privilege access controls.
- Enable multi-factor authentication (MFA).
- Monitor unusual endpoint behavior.
```

These recommendations demonstrate how organizations can reduce the risks associated with compromised endpoints and credential exposure.

---

## Components

The project is divided into several logical components to maintain a clean and modular implementation.

### `KeyboardEvent`

The `KeyboardEvent` dataclass represents a single simulated keyboard event.

It stores:

- Keyboard key
- Event type
- Timestamp

Example:

```python
KeyboardEvent(
    key="A",
    event_type="KEY",
    timestamp=...
)
```

---

### `ALLOWED_EVENT_TYPES`

The application defines the event types that the simulator is permitted to process.

```python
ALLOWED_EVENT_TYPES = {
    "KEY",
    "SPECIAL",
}
```

This prevents unsupported event categories from being processed.

---

### `ALLOWED_SPECIAL_KEYS`

Only a predefined collection of special keyboard events is supported.

```text
SPACE
ENTER
BACKSPACE
TAB
```

This ensures that the simulator remains predictable and controlled.

---

### `validate_event()`

The `validate_event()` function validates keyboard events before they are processed.

Its responsibilities include:

- Verifying that the key is a string
- Verifying that the event type is a string
- Rejecting empty keys
- Rejecting unsupported event types
- Ensuring `KEY` events contain exactly one character
- Rejecting unsupported special keys

Invalid input results in a `TypeError` or `ValueError`.

---

### `create_event()`

The `create_event()` function:

1. Receives a key and event type.
2. Passes them through `validate_event()`.
3. Generates a timestamp.
4. Creates a `KeyboardEvent`.
5. Returns the event object.

Simplified flow:

```text
Input
  |
  v
Validation
  |
  v
Timestamp
  |
  v
KeyboardEvent
```

---

### `SessionLogger`

The `SessionLogger` class stores keyboard events during a controlled session.

Available operations include:

```text
record_event()
record()
get_events()
event_count()
clear()
```

The logger only accepts valid `KeyboardEvent` objects.

---

### `format_event()`

The `format_event()` function converts a single keyboard event into readable output.

Normal event:

```text
[KEY] A
```

Special event:

```text
[ENTER]
```

---

### `format_session()`

The `format_session()` function converts all events within a session into a readable event log.

Example:

```text
[KEY] H
[KEY] i
[SPACE]
[ENTER]
```

If no events are available, the application returns:

```text
No keyboard events recorded.
```

---

### `SECURITY_ANALYSIS`

The project contains defensive security information explaining:

- The purpose of the simulation
- Risks associated with unauthorized keyboard monitoring
- Recommended defensive controls

This keeps the project focused on cybersecurity awareness rather than unauthorized monitoring.

---

### `generate_security_report()`

The `generate_security_report()` function generates the defensive report displayed after the simulation.

The report contains:

```text
Number of simulated events
Purpose
Risk
Defensive mitigations
```

The function also validates the event count before generating the report.

---

### `run_demo()`

The `run_demo()` function executes the controlled demonstration.

It uses predefined simulated events:

```text
H
e
l
l
o
SPACE
S
O
C
ENTER
```

These events are processed by the same validation, creation, logging, and formatting components used throughout the application.

---

### `main()`

The `main()` function acts as the application entry point.

When the Python file is executed directly:

```python
if __name__ == "__main__":
    main()
```

the controlled demonstration is started.

---

## Implementation Approach

The project follows a modular event-processing approach.

```text
                 Simulated Input
                       |
                       v
                Input Validation
                       |
                       v
                  Event Creation
                       |
                       v
                  KeyboardEvent
                       |
                       v
                 SessionLogger
                       |
                       v
                 Event Formatting
                       |
                       v
               Security Analysis
                       |
                       v
                   CLI Report
```

### Detailed Processing Flow

```text
Simulated Event
      |
      v
validate_event()
      |
      v
create_event()
      |
      v
KeyboardEvent Object
      |
      v
SessionLogger.record()
      |
      v
Recorded Session
      |
      v
format_event()
      |
      v
format_session()
      |
      v
generate_security_report()
      |
      v
Final CLI Output
```

This separation makes the project easier to understand, test, maintain, and document.

---

## Example Demonstration

The controlled demonstration uses the following predefined keyboard events:

```text
H
e
l
l
o
SPACE
S
O
C
ENTER
```

These events represent:

```text
Hello SOC
```

The simulator displays them as individual keyboard events:

```text
==================================================
       EDUCATIONAL KEYLOGGER SIMULATOR
==================================================

Controlled simulated events:

[KEY] H
[KEY] e
[KEY] l
[KEY] l
[KEY] o
[SPACE]
[KEY] S
[KEY] O
[KEY] C
[ENTER]

Total events: 10
```

The application then generates a defensive security report:

```text
==================================================
           SECURITY ANALYSIS
==================================================

Simulated events analyzed: 10

Purpose:
Demonstrate how keyboard-monitoring software could observe keyboard events.

Risk:
Unauthorized keystroke monitoring can expose sensitive information such as credentials.

Defensive mitigations:
- Use endpoint detection and response (EDR).
- Maintain updated anti-malware protection.
- Apply least-privilege access controls.
- Enable multi-factor authentication (MFA).
- Monitor unusual endpoint behavior.
```

---

## Security Analysis

### What Is Keylogging?

Keylogging refers to the monitoring or recording of keyboard input.

While keyboard-event monitoring can have legitimate uses in authorized environments, unauthorized keylogging can create significant privacy and security risks.

Malicious keylogging may be associated with attempts to obtain information such as:

```text
Usernames
Passwords
Authentication information
Personal information
Sensitive business information
```

For this reason, unexpected keyboard-monitoring behavior on an endpoint may require investigation by security teams.

---

### Credential Exposure Risk

One of the major security concerns associated with malicious keylogging is credential exposure.

A simplified risk chain can be represented as:

```text
Unauthorized Keyboard Monitoring
              |
              v
      Sensitive Input Observed
              |
              v
      Credentials Exposed
              |
              v
      Account Compromise Risk
```

This project does not perform credential collection. It demonstrates the concept using predefined simulated events.

---

### Endpoint Security Perspective

From a defensive cybersecurity perspective, suspicious input-monitoring behavior may be investigated as part of endpoint analysis.

A simplified defensive workflow is:

```text
Suspicious Process
       |
       v
Unexpected Endpoint Behavior
       |
       v
Potential Input Monitoring
       |
       v
Security Investigation
       |
       v
Containment
       |
       v
Remediation
```

---

### Endpoint Detection and Response

**Endpoint Detection and Response (EDR)** solutions can help security teams monitor endpoint activity and investigate suspicious behavior.

EDR can provide security analysts with visibility into processes, system activity, and other endpoint events that may require investigation.

---

### Anti-Malware Protection

Maintaining updated anti-malware protection can help identify and block known malicious software.

Endpoint protection should be maintained alongside operating-system and software updates.

---

### Least Privilege

The principle of least privilege means that users and applications should receive only the permissions required to perform legitimate activities.

Reducing unnecessary privileges can help reduce the potential impact of compromised software.

---

### Multi-Factor Authentication

**Multi-Factor Authentication (MFA)** requires an additional authentication factor beyond a password.

When properly implemented, MFA can reduce the impact of password compromise because possession of the password alone may not be sufficient for authentication.

---

### Endpoint Behavior Monitoring

Security teams should monitor endpoints for unusual behavior and investigate suspicious processes or unexpected activity.

Defensive monitoring may include:

```text
Process activity
Unexpected application behavior
Security alerts
Authentication activity
Endpoint telemetry
Suspicious persistence attempts
Unusual network communication
```

---

## Project Structure

```text
04_Keylogger/
│
├── README.md
│
├── screenshots/
│   ├── 01_simulated_events.png
│   ├── 02_event_log.png
│   ├── 03_security_analysis.png
│   └── 04_automated_tests.png
│
├── src/
│   ├── __init__.py
│   └── keylogger_simulator.py
│
└── tests/
    └── test_keylogger_simulator.py
```

### Directory Description

| Path | Description |
|---|---|
| `README.md` | Complete Task 04 documentation |
| `src/` | Main Python source code |
| `src/__init__.py` | Marks the source directory as a Python package |
| `src/keylogger_simulator.py` | Main simulator implementation |
| `tests/` | Automated test suite |
| `tests/test_keylogger_simulator.py` | Pytest tests for the simulator |
| `screenshots/` | Evidence of execution and testing |

---

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3.11** | Core application development |
| **Python Dataclasses** | Structured keyboard-event representation |
| **Python `datetime`** | Event timestamp generation |
| **Pytest** | Automated testing |
| **Visual Studio Code** | Development environment |
| **PowerShell** | Command-line execution |
| **Git** | Version control |
| **GitHub** | Repository hosting and project documentation |
| **Markdown** | README documentation |

---

## Requirements

The project requires:

- Python **3.11 or later**
- Pytest
- Git
- A Python-compatible development environment

### Verify Python

Run:

```powershell
python --version
```

Example:

```text
Python 3.11.9
```

### Install Pytest

If Pytest is not installed:

```powershell
python -m pip install pytest
```

Verify the installation:

```powershell
python -m pytest --version
```

---

## Running the Application

Open PowerShell from the repository root:

```text
Prodigy_InfoTech_CyberSecurity
```

Run:

```powershell
python .\04_Keylogger\src\keylogger_simulator.py
```

### Expected Output

```text
==================================================
       EDUCATIONAL KEYLOGGER SIMULATOR
==================================================

Controlled simulated events:

[KEY] H
[KEY] e
[KEY] l
[KEY] l
[KEY] o
[SPACE]
[KEY] S
[KEY] O
[KEY] C
[ENTER]

Total events: 10

==================================================
           SECURITY ANALYSIS
==================================================

Simulated events analyzed: 10

Purpose:
Demonstrate how keyboard-monitoring software could observe keyboard events.

Risk:
Unauthorized keystroke monitoring can expose sensitive information such as credentials.

Defensive mitigations:
- Use endpoint detection and response (EDR).
- Maintain updated anti-malware protection.
- Apply least-privilege access controls.
- Enable multi-factor authentication (MFA).
- Monitor unusual endpoint behavior.
```

> **Important:** All keyboard events shown by the application are predefined simulated events. The application does not monitor the user's actual keyboard.

---

## Testing

Testing was performed at multiple levels to verify that the simulator behaves as expected.

### Syntax Validation

The main Python source file can be checked using:

```powershell
python -m py_compile .\04_Keylogger\src\keylogger_simulator.py
```

Successful execution without output indicates that no Python syntax error was detected.

---

### Manual Testing

The application was manually executed using:

```powershell
python .\04_Keylogger\src\keylogger_simulator.py
```

The manual test verified:

- Event creation
- Event validation
- Session logging
- Event counting
- Event formatting
- Special-key formatting
- Security report generation
- Defensive mitigation output

---

### Automated Testing

The project includes an automated test suite using **Pytest**.

The tests verify both expected behavior and invalid-input handling.

The automated test suite contains **15 tests**.

---

## Running the Automated Tests

From the repository root, run:

```powershell
python -m pytest .\04_Keylogger\tests\ -v
```

### Test Coverage

The test suite validates:

1. Normal keyboard-event creation
2. Special-key event creation
3. Empty-key rejection
4. Multi-character normal-key rejection
5. Unsupported event-type rejection
6. Unsupported special-key rejection
7. Session event recording
8. Session clearing
9. Normal-key formatting
10. Special-key formatting
11. Multiple-event session formatting
12. Empty-session formatting
13. Security-report generation
14. Negative event-count rejection
15. Invalid event-count type rejection

### Test Result

The completed implementation successfully passes all automated tests:

```text
15 passed in 0.12s
```

This confirms that the implemented validation, event management, formatting, and security-report functionality behaves as expected under the tested conditions.

---

## Privacy and Safe Testing

Privacy and authorization are important considerations when working with keyboard-monitoring concepts.

This project intentionally avoids capturing real keyboard input.

The demonstration should use only simulated or non-sensitive test information.

Safe example data:

```text
Hello SOC
DemoInput
Test123
```

Do not use real sensitive information such as:

```text
Real passwords
Banking credentials
Email passwords
Authentication codes
Work credentials
Production credentials
Personal sensitive information
```

The application does **not**:

- Capture system-wide keyboard input
- Monitor another user's keyboard
- Store real passwords
- Collect credentials
- Transmit event data
- Create remote connections
- Establish persistence
- Hide its execution
- Disable security controls
- Evade endpoint detection

> Only perform cybersecurity testing on systems and data that you own or are explicitly authorized to test.

---

## Limitations

This project intentionally uses a controlled simulation for educational and safety purposes.

It does **not**:

- Monitor actual keyboard hardware
- Capture system-wide keyboard events
- Install global keyboard hooks
- Perform covert monitoring
- Establish persistence
- Start automatically with the operating system
- Hide its execution
- Capture real credentials
- Exfiltrate information
- Communicate with remote infrastructure
- Disable security software
- Evade endpoint detection
- Perform credential theft
- Reproduce a complete malicious keylogger infection

The simulator also uses a predefined set of supported special keys:

```text
SPACE
ENTER
BACKSPACE
TAB
```

Therefore, the project should be considered an **educational keyboard-event simulator designed to demonstrate keylogging concepts**, rather than a production keylogging system.

---

## Learning Outcomes

Completing this task provided practical experience across cybersecurity, Python programming, testing, and software engineering.

### Python Programming

The project provided experience with:

- Python functions
- Dataclasses
- Classes
- Type checking
- Exception handling
- Lists
- Dictionaries
- Constants
- Date and time handling
- Modular programming
- Object-oriented design concepts

---

### Input Validation

The project reinforced the importance of validating data before processing it.

Validation included:

```text
Type validation
Empty-value validation
Event-type validation
Character-length validation
Special-key validation
Event-count validation
```

---

### Cybersecurity Concepts

The project reinforced concepts related to:

- Keylogging
- Endpoint monitoring
- Credential threats
- Credential exposure
- Endpoint security
- EDR
- Anti-malware protection
- Least privilege
- MFA
- Endpoint behavior monitoring
- Ethical cybersecurity testing

---

### Security Analysis

The task helped connect a programming concept with defensive cybersecurity analysis.

The project demonstrates the relationship:

```text
Keyboard Monitoring Concept
          |
          v
Potential Credential Exposure
          |
          v
Endpoint Security Risk
          |
          v
Detection and Investigation
          |
          v
Defensive Security Controls
```

---

### Automated Testing

The project provided experience creating and executing automated tests using Pytest.

The test suite verifies both:

```text
Expected application behavior
              +
Invalid input handling
```

All **15 automated tests** passed successfully.

---

### Software Engineering

The project also provided practical experience with:

- Modular project organization
- Separation of responsibilities
- Error handling
- Security-focused design
- Test-driven verification
- Technical documentation
- Maintainable Python code

---

### Development Workflow

The project involved:

- Visual Studio Code
- PowerShell
- Python
- Pytest
- Git
- GitHub
- Markdown

This provided practical experience with a complete development workflow from implementation through testing and documentation.

---

## Evidence

Evidence of implementation and testing is stored in:

```text
04_Keylogger/screenshots/
```

### Evidence Files

| Screenshot | Description |
|---|---|
| `01_simulated_events.png` | Controlled simulated keyboard events |
| `02_event_log.png` | Formatted keyboard-event log |
| `03_security_analysis.png` | Defensive cybersecurity analysis |
| `04_automated_tests.png` | Successful automated Pytest execution |

---

### Evidence 01 — Simulated Events

The first screenshot demonstrates the controlled keyboard-event simulation.

Example output:

```text
[KEY] H
[KEY] e
[KEY] l
[KEY] l
[KEY] o
[SPACE]
[KEY] S
[KEY] O
[KEY] C
[ENTER]
```

The demonstration contains:

```text
10 simulated keyboard events
```

---

### Evidence 02 — Event Log

The second screenshot demonstrates readable formatting of normal and special keyboard events.

Example:

```text
[KEY] H
[KEY] i
[SPACE]
[KEY] S
[KEY] O
[KEY] C
[ENTER]
```

This verifies the behavior of the event-formatting functions.

---

### Evidence 03 — Security Analysis

The third screenshot demonstrates the defensive security report.

The report includes recommendations involving:

- Endpoint Detection and Response
- Anti-malware protection
- Least privilege
- Multi-Factor Authentication
- Endpoint behavior monitoring

---

### Evidence 04 — Automated Tests

The fourth screenshot demonstrates the successful execution of the automated test suite.

Result:

```text
15 passed in 0.12s
```

This provides evidence that the tested functionality completed successfully.

---

## Ethical Disclaimer

This project was developed strictly for **educational and cybersecurity learning purposes**.

The objective is to understand:

- How keyboard events can be represented programmatically
- Why unauthorized keyboard monitoring is dangerous
- How credential exposure can occur
- Why endpoint monitoring is important
- How defensive controls can reduce security risks

The implementation intentionally avoids:

```text
Real keyboard capture
Real credential collection
Covert monitoring
Persistence
Security evasion
Data exfiltration
Remote communication
Unauthorized endpoint monitoring
```

The project should only be used in controlled and authorized environments.

> **Never monitor another person's device, keyboard activity, credentials, or private information without explicit authorization.**

---

## Internship Context

| Field | Details |
|---|---|
| **Organization** | Prodigy InfoTech |
| **Program** | Cyber Security Internship |
| **Task** | Task 04 |
| **Project** | Simple Keylogger |
| **Implementation** | Controlled Educational Keylogger Simulator |
| **Cybersecurity Focus** | Endpoint Monitoring / Credential Threats |
| **Primary Language** | Python |
| **Testing Framework** | Pytest |
| **Version Control** | Git |
| **Repository Platform** | GitHub |

This task forms part of the practical cybersecurity assignments completed during the **Prodigy InfoTech Cyber Security Internship**.

---

## Author

**Anisha Prasad**

Cybersecurity Learner | SOC Analyst Aspirant

---

## Summary

The **Simple Keylogger Simulator** demonstrates the fundamental concept of keyboard-event monitoring through a controlled and safe Python simulation.

The complete workflow can be summarized as:

```text
Simulated Keyboard Events
           |
           v
     Event Validation
           |
           v
      Event Creation
           |
           v
      Session Logging
           |
           v
      Event Formatting
           |
           v
     Security Analysis
           |
           v
 Defensive Recommendations
           |
           v
     Automated Testing
```

The project combines:

```text
Keyboard Event Modeling
        +
Input Validation
        +
Timestamped Events
        +
Session Management
        +
Event Formatting
        +
Endpoint Security Analysis
        +
Defensive Mitigations
        +
Automated Testing
        +
Technical Documentation
```

The project demonstrates how simulated keyboard events can be represented, validated, processed, logged, and analyzed while maintaining strict boundaries against unauthorized monitoring and credential collection.

Key cybersecurity lessons from this task include:

- Understanding the concept of keylogging
- Recognizing the security risks of unauthorized keyboard monitoring
- Understanding potential credential exposure
- Understanding endpoint-security monitoring
- Applying least-privilege principles
- Understanding the role of EDR and anti-malware protection
- Understanding the security value of MFA
- Practicing ethical and authorized cybersecurity testing
- Implementing input validation and error handling
- Validating functionality through automated testing

The final implementation successfully passes:

```text
15 automated tests
```

This task provided practical experience combining **Python programming, cybersecurity fundamentals, endpoint-security awareness, secure software design, automated testing, Git, GitHub, and technical documentation**.

---

**Task 04 completed as part of the Prodigy InfoTech Cyber Security Internship.**