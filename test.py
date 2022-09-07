with open ("input.txt", "r") as f:
    line = f.readline()
    while line:
        s = "".join(filter(str.isnumeric, line))
        print(s)
        line = f.readline()
    