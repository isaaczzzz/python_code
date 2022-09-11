import string

with open("test.txt", "r") as f:
    string = f.read()
    
    string = string.lower()
    s_list = string.split(sep=' ')

    for i in range(0, len(s_list) - 1):
        s_list[i] = s_list[i].rstrip('.')
        s_list[i] = s_list[i].rstrip('?')
        s_list[i] = s_list[i].rstrip('!')

    print(s_list)
