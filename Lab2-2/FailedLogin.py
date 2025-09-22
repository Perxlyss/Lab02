from collections import defaultdict

LOGFILE = "Lab2-2/sample_auth_small.log"  # change filename if needed

def simple_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":
   

    counts = defaultdict(int)           # Create a dictionary to keep track of IPs

    with open(LOGFILE) as f:
        for line in f:
            if "Failed password" in line or "Invalid user" in line:
                # extract ip
                ip = simple_parser(line)
                counts[ip] += 1
    print(counts)