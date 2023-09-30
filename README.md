# WiFi Scanner

<p align="center">
  <img src="assets/wifi.png" />
</p>

This Python script, allows you to scan and display nearby Wi-Fi networks using a specified network interface in monitor mode. It utilizes Scapy to sniff Wi-Fi packets and extract relevant information about the networks.

## Usage
- Make sure you have `Python 3.0` or later installed. To run this script, use the following command:
    ```commandline
    python3 wifi_scanner.py <interface>
    ```

- Replace `<interface>` with the name of the network interface in **monitor mode**.

- Example: `python3 wifi_scanner.py wlan0`

## Screenshot
![](screenshots\Screenshot_2023-09-30_10-29-25.png)

## Requirements
- `Python 3.0` or later
- `Scapy` library
- wireless card in monitor mode

## How to enable monitor mode in linux OS?
#### Run these native linux commands in order:
```bash
ifconfig <interface> down
airmon-ng check kill
iwconfig <interface> mode monitor
ifconfig <interface> up
```

## Functionality
The script will continuously scan for Wi-Fi networks and display relevant information such as **BSSID (MAC address)**, **SSID (network name)**, **signal strength (in dBm)**, **channel**, and **encryption type**.

## How It Works
1. The script uses Scapy to sniff Wi-Fi packets on the specified network interface.

2. It processes the packets and extracts information about nearby Wi-Fi networks.

3. The information is displayed in a tabular format, refreshed every 0.7 seconds, providing real-time updates on the detected networks.

## Code Overview
- **process_packet(packet):** Function to process each packet and extract network information.

- **print_networks():** Function to clear the terminal and print the network information periodically every 0.7s.

- **main():** Main function to start the network scanning process.

- Network data is stored in a DataFrame and displayed in a tabular format.


Feel free to contribute to this project by providing feedback, opening issues, or submitting pull requests.
