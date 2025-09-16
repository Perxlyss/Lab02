with open('sample.txt', 'r') as f:
    line_num = 1
    for line in f:
        print(str(line_num) + ":", line.strip())
        line_num += 1