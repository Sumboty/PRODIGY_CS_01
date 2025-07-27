# Task 5: Network Packet Analyzer
# IMPORTANT: This tool is for educational purposes ONLY.
# Do NOT use on networks you do not own or have explicit permission to monitor.
# Unauthorized packet sniffing is illegal and unethical.

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
import datetime

# Define a simple packet handler function
def packet_callback(packet):
    """
    Callback function to process each sniffed packet.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{timestamp}] --- New Packet ---")

    # Check for IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"  Source IP: {ip_layer.src}")
        print(f"  Destination IP: {ip_layer.dst}")
        # Protocol number mapping for common protocols
        protocol_name = "UNKNOWN"
        if ip_layer.proto == 6:
            protocol_name = "TCP"
        elif ip_layer.proto == 17:
            protocol_name = "UDP"
        elif ip_layer.proto == 1:
            protocol_name = "ICMP"
        print(f"  Protocol: {protocol_name} ({ip_layer.proto})")

        # Check for TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"    Source Port: {tcp_layer.sport}")
            print(f"    Destination Port: {tcp_layer.dport}")
            print(f"    Flags: {tcp_layer.flags}")
            if Raw in packet: # Check for raw payload data
                print(f"    TCP Payload: {packet[Raw].load}")

        # Check for UDP layer
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"    Source Port: {udp_layer.sport}")
            print(f"    Destination Port: {udp_layer.dport}")
            if Raw in packet: # Check for raw payload data
                print(f"    UDP Payload: {packet[Raw].load}")

        # Check for ICMP layer
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f"    ICMP Type: {icmp_layer.type}")
            print(f"    ICMP Code: {icmp_layer.code}")
            if Raw in packet: # Check for raw payload data
                print(f"    ICMP Payload: {packet[Raw].load}")
    else:
        # For non-IP packets (e.g., ARP, spanning tree, etc.)
        print(f"  Non-IP Packet (Type: {packet.type})")
        print(f"  Packet Summary: {packet.summary()}")


def start_sniffer(interface=None, count=0, timeout=None):
    """
    Starts the packet sniffing process.

    Args:
        interface (str, optional): The network interface to sniff on (e.g., 'eth0', 'wlan0').
                                   If None, Scapy tries to find one.
        count (int, optional): Number of packets to sniff. 0 means sniff indefinitely.
        timeout (int, optional): Stop sniffing after this many seconds.
    """
    print("--------------------------------------------------")
    print("WARNING: This is an educational tool for Task 5.")
    print("         Do NOT use without explicit permission.")
    print("--------------------------------------------------")
    print(f"[*] Starting packet sniffer on interface: {interface if interface else 'default'}")
    print(f"[*] Capturing {count if count > 0 else 'infinite'} packets. Press Ctrl+C to stop.")

    try:
        sniff(prn=packet_callback, iface=interface, count=count, timeout=timeout, store=0)
        print("\n[*] Sniffing stopped.")
    except PermissionError:
        print("\nError: Insufficient privileges. Try running with 'sudo'.")
        print("       Example: sudo python3 network_analyzer.py")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # --- Configuration ---
    # You might need to find your active network interface name.
    # Use 'ifconfig' or 'ip a' in your Kali terminal to find it (e.g., 'eth0', 'wlan0').
    # If left as None, Scapy tries to pick one, but it's more reliable to specify.
    network_interface = input("Enter network interface (e.g., eth0, wlan0, leave blank for default): ")
    if not network_interface:
        network_interface = None # Scapy will try to auto-detect

    # Number of packets to capture. Set to 0 for infinite capture (until Ctrl+C)
    num_packets_to_capture = input("Enter number of packets to capture (0 for infinite, then Ctrl+C to stop): ")
    try:
        num_packets_to_capture = int(num_packets_to_capture)
    except ValueError:
        print("Invalid number of packets. Defaulting to infinite.")
        num_packets_to_capture = 0

    # Optional: Timeout in seconds (e.g., 60 for 1 minute)
    # sniffing_timeout = 60 # Uncomment and set a value if you want a time limit

    # Start the sniffer
    start_sniffer(interface=network_interface, count=num_packets_to_capture)
