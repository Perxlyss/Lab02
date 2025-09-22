import re 
pattern = r"cat"
text = "The cat sat on the mat."

matches = re.findall(pattern, text)
print(matches)