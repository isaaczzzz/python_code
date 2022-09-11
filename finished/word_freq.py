import string
import sys

def output(obj):
    import json
    print(json.dumps(obj))

input_name = sys.argv[1]

with open(input_name, "r") as f:
    string = f.read()
    
    string = string.replace('\n', ' ')
    string = string.lower()

    # 将单词存入列表
    s_list = string.split(sep=' ')

    for i in range(0, len(s_list) - 1):
        s_list[i] = s_list[i].strip('.')
        s_list[i] = s_list[i].strip('?')
        s_list[i] = s_list[i].strip('!')

    # 去除空字符
    s_list.remove('')

    dict = {}
    for word in s_list:
        dict[word] = dict.get(word, 0) + 1

    output(dict)
