import re
ips = []
count = 0
Logs = "Lab2-2/sample_auth_small.log"

with open(Logs, 'r') as f:
    for line in f:
        print(line.strip())

        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)

    unique_ips = set(ips)
 

    num_lines = sum(1 for count in open('Logs'))
        print("Total lines:", num_lines)

print("\nUnique IPs:")
for ip in sorted(unique_ips):
    count += 1 
    if count < 11:
        print(ip)
    