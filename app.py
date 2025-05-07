                                                                                                  
from flask import Flask, render_template, jsonify
from sniffer import packet_queue, start_sniffing
import threading

app = Flask(__name__)
packets = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packets")
def get_packets():
    while not packet_queue.empty():
        packets.append(packet_queue.get())
    return jsonify(packets[-50:])  # Last 50 packets

if __name__ == "__main__":
    sniff_thread = threading.Thread(target=start_sniffing, args=("eth0",), daemon=True)
    sniff_thread.start()
    app.run(debug=True)
