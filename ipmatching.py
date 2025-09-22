import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30"

print(re.findall(pattern, text))