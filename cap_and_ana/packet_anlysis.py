#!/usr/bin/env python
# coding: shift-jis

from scapy.all import *
from datetime import datetime
import tkinter
from tkinter import filedialog

idir = './cap_result'
file_name = tkinter.filedialog.askdirectory(initialdir = idir)

PCAP_filename = file_name

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