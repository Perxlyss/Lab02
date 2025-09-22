import re
ips = []

with open('auth.log', 'r') as f:
    for line in f:
        print(line.strip())

        ip_pattern = r"\d+\.\d+\.\d+\.\d+"
        found_ips = re.findall(ip_pattern,line)
        for ip in found_ips:
            ips.append(ip)
    print (ips)

    unique_ips = set(ips)

    print("\nUnique IPs:")
    for ip in unique_ips:
        print(ip)

    with open("unique_ips.txt", "w") as out:
        for ip in unique_ips:
            out.write(ip + "\n")