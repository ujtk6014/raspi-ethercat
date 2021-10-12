#!/usr/bin/env python
# coding: shift-jis

from scapy.all import *
from datetime import datetime

# ----->　設定値ここから
PCAP_filename = "sample.pcap"
# <-----　設定値ここまで

def parse_pcap(filename):

    packets = rdpcap(filename)

    print("----------------------------------")
    for cnt, packet in enumerate(packets, 1):
        datetime_text = datetime.fromtimestamp(packet.time).isoformat()
        print("No:", cnt, " ", datetime_text, " ", packet.summary())
    print("----------------------------------")

if __name__ == "__main__":

    parse_pcap(PCAP_filename)

    print("completed.")