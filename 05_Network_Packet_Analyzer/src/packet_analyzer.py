"""
Network Packet Analyzer
-----------------------

Educational packet-analysis tool for inspecting controlled packet data.

The analyzer extracts basic network metadata such as:
- Source IP
- Destination IP
- Protocol
- Source port
- Destination port

It is designed for authorized cybersecurity learning and testing.
"""

from dataclasses import dataclass
from typing import Any

from scapy.layers.inet import ICMP, IP, TCP, UDP
from scapy.packet import Packet


@dataclass
class PacketAnalysis:
    """Store the extracted information from one network packet."""

    source_ip: str
    destination_ip: str
    protocol: str
    source_port: int | None
    destination_port: int | None
    packet_length: int
    observation: str


def detect_protocol(packet: Packet) -> str:
    """
    Detect the primary network protocol represented by a packet.

    Returns:
        A protocol name such as TCP, UDP, ICMP, or IP.
    """

    if packet.haslayer(TCP):
        return "TCP"

    if packet.haslayer(UDP):
        return "UDP"

    if packet.haslayer(ICMP):
        return "ICMP"

    if packet.haslayer(IP):
        return "IP"

    return "UNKNOWN"


def get_ports(packet: Packet) -> tuple[int | None, int | None]:
    """
    Extract source and destination ports from TCP or UDP packets.

    Returns:
        A tuple containing source port and destination port.
    """

    if packet.haslayer(TCP):
        return packet[TCP].sport, packet[TCP].dport

    if packet.haslayer(UDP):
        return packet[UDP].sport, packet[UDP].dport

    return None, None


def generate_observation(
    protocol: str,
    destination_port: int | None,
) -> str:
    """
    Generate a basic defensive observation for the packet.
    """

    if protocol == "TCP" and destination_port == 443:
        return "HTTPS traffic detected."

    if protocol == "TCP" and destination_port == 80:
        return "HTTP traffic detected."

    if protocol == "UDP" and destination_port == 53:
        return "DNS traffic detected."

    if protocol == "TCP" and destination_port == 22:
        return "SSH traffic detected."

    if protocol == "ICMP":
        return "ICMP traffic detected."

    if protocol in {"TCP", "UDP"}:
        return f"{protocol} traffic detected."

    if protocol == "IP":
        return "IP packet detected."

    return "Unknown or unsupported packet type."


def analyze_packet(packet: Packet) -> PacketAnalysis:
    """
    Analyze a single controlled packet.

    Raises:
        ValueError: If the packet does not contain an IP layer.
    """

    if not isinstance(packet, Packet):
        raise TypeError("packet must be a Scapy Packet object.")

    if not packet.haslayer(IP):
        raise ValueError("Packet does not contain an IP layer.")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    protocol = detect_protocol(packet)

    source_port, destination_port = get_ports(packet)

    packet_length = len(packet)

    observation = generate_observation(
        protocol,
        destination_port,
    )

    return PacketAnalysis(
        source_ip=source_ip,
        destination_ip=destination_ip,
        protocol=protocol,
        source_port=source_port,
        destination_port=destination_port,
        packet_length=packet_length,
        observation=observation,
    )


def format_analysis(
    analysis: PacketAnalysis,
    packet_number: int = 1,
) -> str:
    """Format packet-analysis results for terminal output."""

    return "\n".join(
        [
            "=" * 50,
            f"PACKET #{packet_number}",
            "=" * 50,
            "",
            f"Source IP       : {analysis.source_ip}",
            f"Destination IP  : {analysis.destination_ip}",
            f"Protocol        : {analysis.protocol}",
            f"Source Port     : {analysis.source_port or 'N/A'}",
            f"Destination Port: {analysis.destination_port or 'N/A'}",
            f"Packet Length   : {analysis.packet_length} bytes",
            "",
            f"Observation     : {analysis.observation}",
        ]
    )


def analyze_packets(packets: list[Packet]) -> list[PacketAnalysis]:
    """Analyze multiple controlled packets."""

    if not isinstance(packets, list):
        raise TypeError("packets must be provided as a list.")

    return [analyze_packet(packet) for packet in packets]

def filter_packets(
    analyses: list[PacketAnalysis],
    protocol: str | None = None,
    destination_port: int | None = None,
) -> list[PacketAnalysis]:
    """
    Filter analyzed packets by protocol and/or destination port.

    Args:
        analyses: List of analyzed packets.
        protocol: Optional protocol filter such as TCP, UDP, or ICMP.
        destination_port: Optional destination-port filter.

    Returns:
        A list containing packets matching all supplied filters.
    """

    if not isinstance(analyses, list):
        raise TypeError("analyses must be provided as a list.")

    if protocol is not None and not isinstance(protocol, str):
        raise TypeError("protocol must be a string or None.")

    if destination_port is not None and not isinstance(destination_port, int):
        raise TypeError("destination_port must be an integer or None.")

    normalized_protocol = protocol.upper() if protocol else None

    filtered = []

    for analysis in analyses:
        if (
            normalized_protocol is not None
            and analysis.protocol != normalized_protocol
        ):
            continue

        if (
            destination_port is not None
            and analysis.destination_port != destination_port
        ):
            continue

        filtered.append(analysis)

    return filtered

def generate_statistics(
    analyses: list[PacketAnalysis],
) -> dict[str, Any]:
    """Generate basic statistics from analyzed packets."""

    if not isinstance(analyses, list):
        raise TypeError("analyses must be provided as a list.")

    protocol_counts: dict[str, int] = {}

    for analysis in analyses:
        protocol_counts[analysis.protocol] = (
            protocol_counts.get(analysis.protocol, 0) + 1
        )

    return {
        "total_packets": len(analyses),
        "protocol_counts": protocol_counts,
    }


def run_demo() -> None:
    """Run the controlled packet-analysis demonstration."""

    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=49152, dport=443),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=53),
        IP(src="192.168.1.20", dst="192.168.1.10")
        / ICMP(),
        IP(src="192.168.1.15", dst="192.168.1.30")
        / TCP(sport=50000, dport=22),
    ]

    analyses = analyze_packets(packets)

    print("\n" + "=" * 50)
    print("        NETWORK PACKET ANALYZER")
    print("=" * 50)

    for index, analysis in enumerate(analyses, start=1):
        print()
        print(format_analysis(analysis, index))

    statistics = generate_statistics(analyses)

    print("\n" + "=" * 50)
    print("             TRAFFIC STATISTICS")
    print("=" * 50)

    print(f"\nTotal packets: {statistics['total_packets']}")

    print("\nProtocol counts:")

    for protocol, count in statistics["protocol_counts"].items():
        print(f"- {protocol}: {count}")

    https_packets = filter_packets(
        analyses,
        protocol="TCP",
        destination_port=443,
    )

    print("\n" + "=" * 50)
    print("             FILTERED TRAFFIC")
    print("=" * 50)

    print("\nFilter: TCP traffic to destination port 443")
    print(f"Matching packets: {len(https_packets)}")

    for index, analysis in enumerate(https_packets, start=1):
        print(
            f"- {analysis.source_ip} -> "
            f"{analysis.destination_ip}:{analysis.destination_port}"
        )

def main() -> None:
    """Application entry point."""

    run_demo()


if __name__ == "__main__":
    main()