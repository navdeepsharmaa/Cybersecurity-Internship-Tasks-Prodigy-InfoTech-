from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source: {ip_layer.src} --> Destination: {ip_layer.dst} | Protocol: {ip_layer.proto}")

# Start sniffing (you may change 'count' to limit or iface for specific interface)
print("Sniffing started... Press Ctrl+C to stop.")
sniff(filter="ip", prn=packet_callback, count=10)
