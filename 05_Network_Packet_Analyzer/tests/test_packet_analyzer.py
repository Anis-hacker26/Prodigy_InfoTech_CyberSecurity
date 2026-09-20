from pathlib import Path
import sys

import pytest
from scapy.layers.inet import ICMP, IP, TCP, UDP

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from packet_analyzer import (
    PacketAnalysis,
    analyze_packet,
    analyze_packets,
    detect_protocol,
    filter_packets,
    format_analysis,
    generate_observation,
    generate_statistics,
    get_ports,
)


def test_detect_tcp_protocol():
    """Verify TCP protocol detection."""
    packet = IP(src="192.168.1.10", dst="192.168.1.20") / TCP(
        sport=50000,
        dport=443,
    )

    assert detect_protocol(packet) == "TCP"


def test_detect_udp_protocol():
    """Verify UDP protocol detection."""
    packet = IP(src="192.168.1.10", dst="8.8.8.8") / UDP(
        sport=53000,
        dport=53,
    )

    assert detect_protocol(packet) == "UDP"


def test_detect_icmp_protocol():
    """Verify ICMP protocol detection."""
    packet = IP(src="192.168.1.10", dst="192.168.1.20") / ICMP()

    assert detect_protocol(packet) == "ICMP"


def test_detect_ip_protocol():
    """Verify detection of an IP packet without TCP, UDP, or ICMP."""
    packet = IP(src="192.168.1.10", dst="192.168.1.20")

    assert detect_protocol(packet) == "IP"


def test_get_tcp_ports():
    """Verify extraction of TCP source and destination ports."""
    packet = IP(src="192.168.1.10", dst="192.168.1.20") / TCP(
        sport=49152,
        dport=443,
    )

    assert get_ports(packet) == (49152, 443)


def test_get_udp_ports():
    """Verify extraction of UDP source and destination ports."""
    packet = IP(src="192.168.1.10", dst="8.8.8.8") / UDP(
        sport=53000,
        dport=53,
    )

    assert get_ports(packet) == (53000, 53)


def test_get_icmp_ports():
    """Verify that ICMP has no transport-layer ports."""
    packet = IP(src="192.168.1.10", dst="192.168.1.20") / ICMP()

    assert get_ports(packet) == (None, None)


def test_generate_https_observation():
    """Verify HTTPS traffic identification."""
    assert (
        generate_observation("TCP", 443)
        == "HTTPS traffic detected."
    )


def test_generate_dns_observation():
    """Verify DNS traffic identification."""
    assert (
        generate_observation("UDP", 53)
        == "DNS traffic detected."
    )


def test_generate_ssh_observation():
    """Verify SSH traffic identification."""
    assert (
        generate_observation("TCP", 22)
        == "SSH traffic detected."
    )


def test_generate_icmp_observation():
    """Verify ICMP traffic identification."""
    assert (
        generate_observation("ICMP", None)
        == "ICMP traffic detected."
    )


def test_analyze_packet():
    """Verify complete packet analysis."""
    packet = IP(
        src="192.168.1.10",
        dst="192.168.1.20",
    ) / TCP(
        sport=49152,
        dport=443,
    )

    result = analyze_packet(packet)

    assert isinstance(result, PacketAnalysis)
    assert result.source_ip == "192.168.1.10"
    assert result.destination_ip == "192.168.1.20"
    assert result.protocol == "TCP"
    assert result.source_port == 49152
    assert result.destination_port == 443
    assert result.packet_length > 0
    assert result.observation == "HTTPS traffic detected."


def test_analyze_icmp_packet():
    """Verify analysis of an ICMP packet."""
    packet = IP(
        src="192.168.1.20",
        dst="192.168.1.10",
    ) / ICMP()

    result = analyze_packet(packet)

    assert result.protocol == "ICMP"
    assert result.source_port is None
    assert result.destination_port is None


def test_reject_non_packet_input():
    """Verify that non-Scapy packet input is rejected."""
    with pytest.raises(TypeError):
        analyze_packet("not a packet")


def test_reject_packet_without_ip_layer():
    """Verify that packets without an IP layer are rejected."""
    packet = TCP(sport=50000, dport=443)

    with pytest.raises(ValueError):
        analyze_packet(packet)


def test_analyze_multiple_packets():
    """Verify analysis of multiple packets."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=53),
        IP(src="192.168.1.20", dst="192.168.1.10")
        / ICMP(),
    ]

    results = analyze_packets(packets)

    assert len(results) == 3
    assert results[0].protocol == "TCP"
    assert results[1].protocol == "UDP"
    assert results[2].protocol == "ICMP"


def test_reject_invalid_packet_list():
    """Verify that analyze_packets requires a list."""
    with pytest.raises(TypeError):
        analyze_packets("not a list")


def test_generate_statistics():
    """Verify protocol statistics generation."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=53),
        IP(src="192.168.1.20", dst="192.168.1.10")
        / ICMP(),
        IP(src="192.168.1.15", dst="192.168.1.30")
        / TCP(sport=50001, dport=22),
    ]

    analyses = analyze_packets(packets)
    statistics = generate_statistics(analyses)

    assert statistics["total_packets"] == 4
    assert statistics["protocol_counts"]["TCP"] == 2
    assert statistics["protocol_counts"]["UDP"] == 1
    assert statistics["protocol_counts"]["ICMP"] == 1


def test_generate_statistics_empty_list():
    """Verify statistics for an empty analysis list."""
    statistics = generate_statistics([])

    assert statistics["total_packets"] == 0
    assert statistics["protocol_counts"] == {}


def test_reject_invalid_statistics_input():
    """Verify that statistics require a list."""
    with pytest.raises(TypeError):
        generate_statistics("not a list")


def test_format_analysis():
    """Verify formatted packet-analysis output."""
    analysis = PacketAnalysis(
        source_ip="192.168.1.10",
        destination_ip="192.168.1.20",
        protocol="TCP",
        source_port=49152,
        destination_port=443,
        packet_length=40,
        observation="HTTPS traffic detected.",
    )

    output = format_analysis(analysis, packet_number=1)

    assert "PACKET #1" in output
    assert "192.168.1.10" in output
    assert "192.168.1.20" in output
    assert "TCP" in output
    assert "49152" in output
    assert "443" in output
    assert "40 bytes" in output
    assert "HTTPS traffic detected." in output
    
def test_filter_packets_by_protocol():
    """Verify filtering packets by protocol."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=53),
        IP(src="192.168.1.20", dst="192.168.1.10")
        / ICMP(),
    ]

    analyses = analyze_packets(packets)

    filtered = filter_packets(analyses, protocol="tcp")

    assert len(filtered) == 1
    assert filtered[0].protocol == "TCP"


def test_filter_packets_by_destination_port():
    """Verify filtering packets by destination port."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
        IP(src="192.168.1.15", dst="192.168.1.30")
        / TCP(sport=50001, dport=22),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=53),
    ]

    analyses = analyze_packets(packets)

    filtered = filter_packets(
        analyses,
        destination_port=443,
    )

    assert len(filtered) == 1
    assert filtered[0].destination_port == 443


def test_filter_packets_by_protocol_and_port():
    """Verify combined protocol and port filtering."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
        IP(src="192.168.1.15", dst="192.168.1.30")
        / TCP(sport=50001, dport=22),
        IP(src="192.168.1.10", dst="8.8.8.8")
        / UDP(sport=53000, dport=443),
    ]

    analyses = analyze_packets(packets)

    filtered = filter_packets(
        analyses,
        protocol="TCP",
        destination_port=443,
    )

    assert len(filtered) == 1
    assert filtered[0].protocol == "TCP"
    assert filtered[0].destination_port == 443


def test_filter_packets_no_matches():
    """Verify filtering when no packets match."""
    packets = [
        IP(src="192.168.1.10", dst="192.168.1.20")
        / TCP(sport=50000, dport=443),
    ]

    analyses = analyze_packets(packets)

    filtered = filter_packets(
        analyses,
        protocol="UDP",
    )

    assert filtered == []


def test_filter_packets_rejects_invalid_protocol():
    """Verify invalid protocol input is rejected."""
    with pytest.raises(TypeError):
        filter_packets([], protocol=123)


def test_filter_packets_rejects_invalid_port():
    """Verify invalid destination-port input is rejected."""
    with pytest.raises(TypeError):
        filter_packets([], destination_port="443")