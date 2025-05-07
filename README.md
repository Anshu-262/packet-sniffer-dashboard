# packet-sniffer-dashboard
🕵️‍♂️ Live Packet Sniffer Web App
This is a simple web-based packet sniffer built with Python, Flask, and Scapy. It captures network packets from a specified interface and displays real-time data on a web dashboard.

📁 Project Structure
bash
Copy
Edit
├── app.py                  # Flask app that runs the web server and displays packet data
├── sniffer.py              # Packet capturing logic using Scapy
├── templates/
│   └── index.html          # HTML frontend for displaying packets
⚙️ How It Works
sniffer.py:

Uses Scapy to sniff packets on the interface (eth0 by default).

Filters and processes IP, DNS, and HTTP data.

Puts relevant packet info into a queue.Queue.

app.py:

Runs a Flask web server.

Starts a background thread to run start_sniffing().

Provides two routes:

/: Renders the frontend page (index.html).

/packets: Returns the latest 50 captured packets as JSON.

templates/index.html:

A minimal dashboard that:

Polls /packets every 3 seconds.

Displays packet type, source/destination, and details (e.g. DNS queries or HTTP headers).

🚀 Getting Started
1. Requirements
Python 3.x

Scapy

Flask

Install them via:

bash
Copy
Edit
pip install scapy flask
2. Run the Application
bash
Copy
Edit
sudo python3 app.py
Note: You must run as sudo to allow Scapy to access network interfaces.

3. Access the Dashboard
Open your browser and navigate to:

arduino
Copy
Edit
http://localhost:5000
🔍 Features
Captures and displays:

DNS queries

HTTP headers (from raw TCP payloads)

Live update every 3 seconds

Runs in the background via a separate thread

🖥️ Interface Used
The default interface is "eth0". You can change it by modifying this line in app.py:

python
Copy
Edit
sniff_thread = threading.Thread(target=start_sniffing, args=("eth0",), daemon=True)
Replace "eth0" with the desired interface, such as "wlan0" or "lo".

🛡️ Disclaimer
This tool is intended for educational and ethical use only. Do not use it on networks without proper authorization.
