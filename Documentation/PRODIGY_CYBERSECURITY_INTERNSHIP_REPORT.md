# Prodigy InfoTech — Cyber Security Internship Report

## Internship Overview

This repository contains the work completed during my **Cyber Security Internship at Prodigy InfoTech**.

### Internship Details

| Detail | Information |
|---|---|
| Organization | Prodigy InfoTech |
| Program | Cyber Security Internship |
| Internship Start | 1 September 2026 |
| Internship End | 30 September 2026 |
| Submission Deadline | 5 October 2026 |
| Repository | Prodigy_InfoTech_CyberSecurity |
| Primary Language | Python |
| Development Environment | Visual Studio Code |
| Version Control | Git and GitHub |

---

# Internship Objectives

The internship focused on developing practical cybersecurity skills through implementation-based tasks.

The major objectives were:

- Understand fundamental cybersecurity concepts.
- Practice Python programming for cybersecurity applications.
- Understand basic cryptography concepts.
- Explore image/data confidentiality concepts.
- Understand password security and complexity.
- Study endpoint and keylogging-related security risks.
- Understand network packet structures and traffic analysis.
- Practice input validation and automated testing.
- Apply defensive cybersecurity principles.
- Document security-related implementations professionally.
- Maintain a structured GitHub repository.
- Understand ethical and legal boundaries in cybersecurity.

---

# Repository Structure

```text
Prodigy_InfoTech_CyberSecurity/
│
├── 00_Internship_Documents/
│
├── 01_Caesar_Cipher/
│   ├── README.md
│   ├── screenshots/
│   ├── src/
│   └── tests/
│
├── 02_Image_Encryption/
│   ├── README.md
│   ├── sample_images/
│   ├── screenshots/
│   ├── src/
│   └── tests/
│
├── 03_Password_Complexity/
│   ├── README.md
│   ├── screenshots/
│   ├── src/
│   └── tests/
│
├── 04_Keylogger/
│   ├── README.md
│   ├── screenshots/
│   ├── src/
│   └── tests/
│
├── 05_Network_Packet_Analyzer/
│   ├── README.md
│   ├── screenshots/
│   ├── src/
│   └── tests/
│
├── Documentation/
│
└── README.md
```

---

# Task 01 — Caesar Cipher

## Objective

The first task focused on implementing a Caesar Cipher to understand the fundamentals of classical substitution-based encryption.

## Implementation

The implementation supports:

- Text encryption.
- Text decryption.
- User-defined shift values.
- Alphabet wrapping.
- Preservation of spaces.
- Preservation of punctuation.
- Preservation of numeric characters.
- Input validation.

## Example

Input:

```text
HELLO WORLD
```

Shift:

```text
3
```

Encrypted output:

```text
KHOOR ZRUOG
```

Decrypting the encrypted text with the same shift restores:

```text
HELLO WORLD
```

## Edge Cases Tested

The implementation was tested with:

- Lowercase characters.
- Uppercase characters.
- Mixed-case text.
- Spaces.
- Punctuation.
- Numbers.
- Shift values greater than 26.
- Invalid shift input.

## Automated Testing

The final automated test suite contained:

```text
12 tests
```

Result:

```text
12 passed
```

## Security Learning

This task introduced:

- Encryption and decryption concepts.
- Substitution ciphers.
- Key/shift-based transformations.
- Character wrapping.
- Limitations of classical cryptography.

The Caesar Cipher is educational and should not be considered suitable for protecting sensitive information in modern systems.

---

# Task 02 — Pixel Manipulation Image Encryption

## Objective

The second task focused on image encryption through controlled pixel manipulation.

## Technologies

- Python
- Pillow

## Implementation

The project uses a reversible XOR-based transformation to manipulate image pixel values.

The workflow is:

```text
Original Image
      ↓
Pixel Transformation
      ↓
Encrypted Image
      ↓
Reverse Transformation
      ↓
Decrypted Image
```

## Demonstration

A controlled sample image was used to demonstrate:

1. Original image.
2. Encrypted image.
3. Decrypted image.

The decrypted image was verified against the original image.

## Verification

The implementation verified that:

- Image dimensions were preserved.
- RGB mode was preserved for the tested images.
- Encryption changed the pixel data.
- Decryption restored the original pixel data.

## Automated Testing

Final result:

```text
6 passed
```

## Security Learning

This task demonstrated:

- Data confidentiality concepts.
- Pixel-level data manipulation.
- Reversible transformations.
- Image processing.
- Automated verification.

### Security Limitation

The XOR transformation used in this educational implementation is **not modern secure encryption**.

A fixed-key XOR transformation should not be used as a replacement for established cryptographic algorithms.

---

# Task 03 — Password Complexity Checker

## Objective

The third task focused on evaluating password characteristics and providing strength feedback.

## Password Characteristics

The checker evaluates:

- Password length.
- Uppercase characters.
- Lowercase characters.
- Numeric characters.
- Special characters.
- Common or predictable patterns.

## Strength Classification

The implementation provides three primary classifications:

```text
Weak
Moderate
Strong
```

## Examples

### Weak Password

```text
abc
```

Result:

```text
Score: 1/6
Strength: Weak
```

### Moderate Password

```text
BlueSky2026
```

Result:

```text
Strength: Moderate
```

### Strong Password

```text
Secure@2026Pass!
```

Result:

```text
Score: 6/6
Strength: Strong
```

### Predictable Password

```text
password123
```

The implementation identifies the predictable/common pattern and provides security feedback.

## Automated Testing

Final result:

```text
9 passed
```

## Security Learning

This task demonstrated:

- Password complexity analysis.
- Authentication security concepts.
- Input validation.
- Common password risks.
- Predictable password patterns.
- Security feedback generation.

Password complexity alone does not guarantee protection against:

- Dictionary attacks.
- Brute-force attacks.
- Password reuse.
- Credential stuffing.

Additional security practices include:

- Password managers.
- Multi-factor authentication.
- Unique passwords.
- Secure password storage.

---

# Task 04 — Simple Keylogger

## Objective

The fourth task explored keylogging concepts from a controlled defensive cybersecurity perspective.

Because unrestricted keylogging can capture sensitive information, the implementation was intentionally designed as a **controlled keylogger simulator**.

## Security Boundaries

The simulator does not perform:

- System-wide keyboard hooking.
- Real credential capture.
- Covert monitoring.
- Persistence.
- Startup execution.
- Evasion.
- Security-software disabling.
- Network exfiltration.
- Remote communication.

Instead, it processes predefined simulated keyboard events.

## Implementation

The project includes:

- `KeyboardEvent` data structure.
- Event validation.
- Simulated keyboard events.
- Session logging.
- Human-readable event formatting.
- Defensive security analysis.

## Demonstration

The controlled demonstration processes simulated events representing:

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

## Automated Testing

Final result:

```text
15 passed
```

## Security Learning

This task provided practical understanding of:

- Keylogging threats.
- Endpoint monitoring.
- Credential theft risks.
- Event logging.
- Security monitoring.
- Defensive detection concepts.

Potential defensive controls include:

- Endpoint Detection and Response.
- Anti-malware solutions.
- Least-privilege access.
- Multi-factor authentication.
- Security event monitoring.

---

# Task 05 — Network Packet Analyzer

## Objective

The fifth task focused on network packet analysis and basic traffic inspection.

## Technologies

- Python
- Scapy
- Pytest

## Packet Information Extracted

The analyzer extracts:

- Source IP.
- Destination IP.
- Protocol.
- Source port.
- Destination port.
- Packet length.
- Basic traffic observation.

## Supported Protocols

The implementation recognizes:

- TCP
- UDP
- ICMP
- IP
- UNKNOWN

## Traffic Observations

The controlled demonstration includes:

```text
TCP + 443 → HTTPS traffic detected.
TCP + 80  → HTTP traffic detected.
UDP + 53  → DNS traffic detected.
TCP + 22  → SSH traffic detected.
ICMP      → ICMP traffic detected.
```

These observations are descriptive and are not independent security verdicts.

## Traffic Statistics

The demonstration analyzes four controlled packets.

Result:

```text
Total packets: 4

TCP: 2
UDP: 1
ICMP: 1
```

## Traffic Filtering

The analyzer supports filtering using:

- Protocol.
- Destination port.
- Protocol + destination port.

Example:

```text
Filter: TCP traffic to destination port 443
Matching packets: 1
```

## Automated Testing

Final result:

```text
27 passed
```

## Syntax Verification

The implementation was also verified using:

```text
python -m py_compile .\05_Network_Packet_Analyzer\src\packet_analyzer.py
```

The command completed without syntax errors.

## SOC Analyst Perspective

Network traffic can provide useful evidence during security investigations.

For example, analysts may investigate:

- Unexpected connections.
- Unknown destinations.
- Unusual protocols.
- Unexpected service ports.
- Repeated communication.
- Potential command-and-control indicators.
- Potential data-transfer activity.
- Network reconnaissance indicators.

Network information can be correlated with:

- DNS logs.
- Endpoint processes.
- Authentication events.
- Firewall logs.
- IDS/IPS alerts.
- EDR telemetry.

A single packet attribute should not automatically be treated as proof of malicious activity.

---

# Testing Summary

The completed projects include automated testing.

| Task | Test Result |
|---|---:|
| Caesar Cipher | 12 passed |
| Image Encryption | 6 passed |
| Password Complexity Checker | 9 passed |
| Keylogger Simulator | 15 passed |
| Network Packet Analyzer | 27 passed |

Total automated tests across the five tasks:

```text
69 tests
```

All documented task test suites passed successfully.

---

# Technologies Used

## Programming

- Python

## Cybersecurity / Technical Libraries

- Scapy
- Pillow

## Testing

- Pytest

## Development

- Visual Studio Code

## Version Control

- Git
- GitHub

---

# Cybersecurity Concepts Practiced

During the internship, the projects provided practical exposure to:

- Classical cryptography.
- Data confidentiality.
- Image data manipulation.
- Password security.
- Authentication security.
- Endpoint monitoring.
- Keylogging threats.
- Network protocols.
- Packet analysis.
- Traffic filtering.
- Security event interpretation.
- Input validation.
- Automated testing.
- Security documentation.
- Ethical cybersecurity practices.

---

# Defensive Security Perspective

The projects were approached from an educational and defensive cybersecurity perspective.

The work demonstrates how security concepts can be implemented and analyzed while maintaining controlled testing boundaries.

The projects emphasize:

- Authorized testing.
- Controlled demonstrations.
- Input validation.
- Automated verification.
- Privacy awareness.
- Security monitoring.
- Ethical use of cybersecurity knowledge.

---

# Privacy and Ethical Considerations

Cybersecurity tools can interact with sensitive information and systems.

Therefore, these projects were developed with controlled and educational use in mind.

Important principles include:

- Only analyze systems and data for which authorization exists.
- Do not capture credentials without explicit authorization.
- Do not perform covert monitoring.
- Do not deploy persistence mechanisms.
- Do not exfiltrate captured information.
- Do not disable security controls.
- Do not perform unauthorized network monitoring.
- Protect sensitive information during testing.

Cybersecurity knowledge should be applied responsibly and within applicable laws, policies, and organizational authorization.

---

# Evidence

Each task contains dedicated evidence screenshots.

## Task 01

Evidence includes:

- Basic encryption.
- Basic decryption.
- Edge cases.
- Automated tests.

Location:

```text
01_Caesar_Cipher/screenshots/
```

## Task 02

Evidence includes:

- Original image.
- Encrypted image.
- Decrypted image.
- Automated tests.

Location:

```text
02_Image_Encryption/screenshots/
```

## Task 03

Evidence includes:

- Weak password.
- Moderate password.
- Strong password.
- Predictable password.
- Automated tests.

Location:

```text
03_Password_Complexity/screenshots/
```

## Task 04

Evidence includes:

- Simulated events.
- Event log.
- Security analysis.
- Automated tests.

Location:

```text
04_Keylogger/screenshots/
```

## Task 05

Evidence includes:

- Packet analysis.
- Traffic statistics.
- Filtered traffic.
- Automated tests.

Location:

```text
05_Network_Packet_Analyzer/screenshots/
```

---

# GitHub Repository

The complete internship repository is hosted on GitHub:

https://github.com/Anis-hacker26/Prodigy_InfoTech_CyberSecurity

The repository contains:

- Source code.
- Automated tests.
- Task-specific README files.
- Evidence screenshots.
- Internship documentation.
- Git version history.

---

# Version Control

Git was used throughout the project to maintain the development history.

Major task commits include:

```text
feat: implement caesar cipher task

feat: implement image encryption task

feat: implement password complexity checker

feat: implement keylogger simulator task

feat: implement network packet analyzer task
```

The final Network Packet Analyzer implementation was committed and pushed to the `main` branch.

---

# Overall Learning Outcomes

The internship provided practical experience in applying programming concepts to cybersecurity tasks.

The work helped develop understanding of:

1. How basic encryption transformations work.
2. How reversible data transformations can be implemented.
3. How password characteristics can be evaluated.
4. Why password complexity is only one part of authentication security.
5. How keylogging represents an endpoint security threat.
6. How defensive monitoring can be used to identify suspicious activity.
7. How network packets contain useful metadata.
8. How traffic can be categorized and filtered.
9. Why individual indicators require additional context during investigations.
10. How automated testing improves reliability.
11. How security projects should include ethical and privacy considerations.
12. How cybersecurity projects can be documented and maintained using Git and GitHub.

---

# Final Completion Summary

All five assigned cybersecurity tasks were implemented and documented:

| Task | Project | Status |
|---|---|---|
| 01 | Caesar Cipher | Completed |
| 02 | Pixel Manipulation Image Encryption | Completed |
| 03 | Password Complexity Checker | Completed |
| 04 | Controlled Keylogger Simulator | Completed |
| 05 | Network Packet Analyzer | Completed |

The repository includes source code, automated tests, documentation, and visual evidence for each completed task.

---

# Internship Task Completion Checklist

- [x] Task 01 — Caesar Cipher
- [x] Task 02 — Image Encryption
- [x] Task 03 — Password Complexity Checker
- [x] Task 04 — Keylogger Simulator
- [x] Task 05 — Network Packet Analyzer
- [x] Automated testing
- [x] Evidence screenshots
- [x] Task documentation
- [x] Git version control
- [x] GitHub repository
- [x] Ethical and legal considerations
- [x] Security-focused documentation

---

# Final Status

## Cyber Security Internship — Prodigy InfoTech

**Five assigned tasks completed and documented.**

The repository represents practical work covering cryptography fundamentals, data confidentiality, authentication security, endpoint security concepts, and network traffic analysis.

---

# Author

**Anisha Prasad**

Cyber Security Intern  
Prodigy InfoTech

GitHub:

https://github.com/Anis-hacker26

---

## Disclaimer

This repository is intended for educational and authorized cybersecurity purposes only.

The projects should not be used for unauthorized access, surveillance, credential theft, network interception, data exfiltration, or any activity that violates applicable laws, policies, or permissions.
