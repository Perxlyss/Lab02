with open('copy.txt', 'w') as a:
    with open('sample.txt', 'r') as b:
        for line in b:
            a.write(line) 
 