import re


pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30, good login from 6.6.6.6"
print(re.findall(pattern, text))
