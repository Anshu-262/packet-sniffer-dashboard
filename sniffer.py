                                                                                                  
from scapy.all import sniff, IP, TCP, UDP, DNS, Raw
import queue

packet_queue = queue.Queue()

def process_packet(packet):
    data = {}

    if IP in packet:
        data["src"] = packet[IP].src
        data["dst"] = packet[IP].dst

    if packet.haslayer(DNS):
        data["type"] = "DNS"
        data["query"] = packet[DNS].qd.qname.decode() if packet[DNS].qd else "N/A"

    elif packet.haslayer(TCP) and packet.haslayer(Raw):
        try:
            payload = packet[Raw].load.decode(errors="ignore")
            if "HTTP" in payload or "Host:" in payload:
                data["type"] = "HTTP"
                data["http_data"] = payload.split("\r\n")[0]
        except:
            pass

    if data:
        packet_queue.put(data)

def start_sniffing(interface="eth0"):
    sniff(iface=interface, prn=process_packet, store=0)
