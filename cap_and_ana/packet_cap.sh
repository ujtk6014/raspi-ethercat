#!/bin/bash
FILENAME=sample
DATE=`date "+%F-%T"`
PCAP_FILE=./cap_result/${FILENAME}_${DATE}.pcap
PCAP_IFACE=eth0
PROTO=0x88a4

sudo /usr/sbin/tcpdump -w $PCAP_FILE -i $PCAP_IFACE ether proto $PROTO
