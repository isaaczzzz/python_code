import string
import sys

input_name = sys.argv[1]
output_name = sys.argv[2]

with open (input_name, "r") as f:
    line = f.readline()
    result = ""

    while line:
        # 去除特殊字符
        s = "".join(filter(str.isnumeric, line))
        
        list_s = list(s)
        ite = 0
        for c in list_s:
            if (ite + 1) % 4 == 0:
                list_s.insert(ite, "-")
            ite += 1
        
        s = "".join(list_s)
        result = result + s + "\n"
        line = f.readline()

with open (output_name, "w") as f:
    f.write(result)
    
