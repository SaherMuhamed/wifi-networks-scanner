import os
import sys
import time
from threading import Thread
import pandas as pd
import scapy.all as scapy
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt, Dot11

if sys.version_info < (3, 0):
    sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
    sys.stderr.write("Please update and make sure you use the command python3 wifi_scanner.py <interface>\n\n")
    sys.exit(0)

networks = pd.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Encryption"])
networks.set_index("BSSID", inplace=True)


def process_packet(packet):
    """this function get executed whenever a packet is sniffed to process it"""
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2  # get the MAC addresses of the networks
        ssid = str(packet[Dot11Elt].info, encoding="UTF-8")  # get the name of the networks
        ssid = "<Hidden>" if ssid == "" else str(packet[Dot11Elt].info, encoding="UTF-8")  # check if the network
        # doesn't broadcast its name (ternary operator)
        dbm_signal = packet.dBm_AntSignal  # get the signal strength of the networks

        stats = packet[Dot11Beacon].network_stats()  # extract network stats <channel, rate, encryption, etc..>
        channel = stats.get("channel")  # get the channel number of the networks
        enc = stats.get("crypto")  # get the encryption of the networks

        networks.loc[bssid] = (ssid, dbm_signal, channel, enc)  # putting all together


def print_networks():
    """this function clear terminal every 0.7s and print wi-fi networks again"""
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.7)


def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <interface>" % sys.argv[0])
        print("[+] Example: %s wlan0" % sys.argv[0] + "\n")
        sys.exit(-1)
    interface = sys.argv[1]  # interface name in monitor mode
    Thread(target=print_networks, daemon=True).start()  # print all sniffed networks
    scapy.sniff(prn=process_packet, iface=interface)  # start sniffing


if __name__ == "__main__":
    main()
