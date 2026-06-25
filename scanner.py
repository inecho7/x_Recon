import ipaddress
import socket
import time
from concurrent.futures import ThreadPoolExecutor

timeout = 0.1

THREAT_PROFILES = {
    21 = "FTP (Plaintext credentials transfer risk)",
    22 = "SSH (Remote Access Management - Verify authentication strength)",
    23 = "Telnet (Unencryoted remote administration hazard)",
    25 = "SMTP (Mail relay tracking required)",
    53 = "DNS (Potential zone transfer or amplification vector)",
    80 = "HTTP (Cleartext web traffic)",
    443 = "HTTPS (Encrypted web traffic - Check certificate validity)",
    445 = "SMB (File sharing - High Priority inspection for legacy exploits)"
}

target_input = input("Enter the target Network (e.g. 192.168.1.0/24)")
network = ipaddress.ip_network(target_input, strict=False)
host_list = network.hosts()
def scan_port(ip, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((str(ip), port))
        if result == 0:
            print(f"Host {ip} {port} is active!")
        s.close()
    except:
        pass

print("Select the type of scan you want")
print("1. Fast Scan (Scan top 10 most common ports)")
print("2. Deep Scan (Scan a range of ports (1, 1025))")

choice = input("Enter choice (1 or 2): ")
if choice == "1":
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]
elif choice == "2":
    ports_to_scan = list(range(1, 1025))
else:
    print("Error: Please enter a valid choice")
    ports_to_scan = []

start_time = time.time()

detected_services = []

for ip in host_list:
    print(f"\n Scanning host: {ip}...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports_to_scan:
            executor.submit(scan_port, ip, port, timeout)

end_time = time.time()
total_time = end_time - start_time
print("\n" + "="*50)
print("Scan Complete")
print("Asset & Threat Profile Advisory")
print(f"Total Time Elapsed: {total_time:.2f} seconds")
print("="*50)

if not detected_services:
    print("No active common services identified in this scope.")
else:
    for port in sorted(set(detected_services)):
        profile = THREAT_PROFILES.get(port, "Unknown / Custom Service")
        print(f"[!] Port {port} Open - {profile} ")
print("="*50)        