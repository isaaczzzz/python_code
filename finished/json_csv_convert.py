import csv
import json
import sys

method = sys.argv[1]
input_name = sys.argv[2]


def csv_2_json(filename):
    devices_list = []

    header = ["id","name","type","hardware_model","hardware_sn","software_version","software_last_update","nic_1_type","nic_1_mac","nic_1_ipv4" \
        , "nic_2_type","nic_2_mac","nic_2_ipv4", "state"]

    with open(filename, "r", encoding="UTF-8") as f:
        csv_reader = csv.reader(f)
        for device_csv in csv_reader:
            tmp_dict = {}
            for i in range(0, 3):
                tmp_dict[header[i]] = device_csv[i]

            tmp_dict_2 = {}
            tmp_dict_2["model"] = device_csv[3]
            tmp_dict_2["sn"] = device_csv[4]
            tmp_dict["hardware"] = tmp_dict_2

            tmp_dict_3 = {}
            tmp_dict_3["version"] = device_csv[5]
            tmp_dict_3["last_update"] = device_csv[6]
            tmp_dict["software"] = tmp_dict_3

            tmp_dict_4 = {}
            tmp_list = []
            if device_csv[7] != "":
                tmp_dict_4["type"] = device_csv[7]
                tmp_dict_4["mac"] = device_csv[8]
                tmp_dict_4["ipv4"] = device_csv[9]
                tmp_list.append(tmp_dict_4)
            
            tmp_dict_5 = {}
            if device_csv[10] != "":
                tmp_dict_5["type"] = device_csv[10]
                tmp_dict_5["mac"] = device_csv[11]
                tmp_dict_5["ipv4"] = device_csv[12]
                tmp_list.append(tmp_dict_5)
            tmp_dict["nic"] = tmp_list
 
            tmp_dict["state"] = device_csv[13]
            
            devices_list.append(tmp_dict)

    output_name = filename[:-4] + ".json"
    with open(output_name, "w") as f:
        json.dump(devices_list, f, indent=4)

def json_2_csv(filename):
    result = ""
    with open(filename, "r") as f:
        list = json.load(f)
        for dict in list:
            devices_list = []
            i = 0
            for item in dict.items():
                # print(item[1])

                if i == 3 or i == 4:
                    for item1 in item[1].items():
                        devices_list.append(item1[1])
                    i+=1
                    continue
                
                if i == 5:
                    j = 0
                    for item1 in item[1]:
                        j += 1
                        for item2 in item1.items():
                            devices_list.append(item2[1])

                    while j < 2:
                        for k in range(0, 3):
                            devices_list.append("")
                        j += 1

                    i+=1
                    continue

                devices_list.append(item[1])
                i+=1
            
            s = ",".join(devices_list)
            result = result + s + "\n"

    fin_result = result[:-1]
    output_name = filename[:-5] + ".csv"
    with open(output_name, "w") as f_out:
        f_out.write(fin_result)

        
if method == "-b":
    csv_2_json(input_name)
elif method == "-p":
    json_2_csv(input_name)
