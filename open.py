#!/opt/bb/bin/python3.6

# open fix44.xml 
# read line by line
# if the line includes field number=x, name=y 
# add the number and name to Dict 1 and move on to the next line
# if the line includes value enum=z, description=a
# add the enum and description to Dict 2
# Dict 2 is the value to the key, Dict 1

EMPTY_DICT = {}
FINAL_DICT = {}

myfile = open("example.txt")
txt = myfile.readlines()
current_tag = ""
current_enum_tag = ""

for line in txt:
    # print(line[:-1])
    value_dict = {}

    if str("field number=") in line:
        tag_num = line[line.find("number="):line.find(" name")]
        int_val = tag_num.replace("number=","")
        current_tag = int_val
    
        tag_val = line[line.find("name="):line.find(" type")]
        str_val = tag_val.replace("name=","")

        EMPTY_DICT[current_tag] = str_val
        print("EMPTY DICT", EMPTY_DICT)

    elif str("value enum=") in line:
        enum_num = line[line.find("enum="):line.find(" description")]
        int_num = enum_num.replace("enum=","")
        current_enum_tag = int_num

        enum_val = line[line.find("description="):line.find(" />")]
        des_val = enum_val.replace("description=","")

        value_dict[current_enum_tag] = des_val
        value_dict[current_enum_tag].append(des_val) ##AttributeError...why?
        print(value_dict)
    
    FINAL_DICT[current_tag] = value_dict
    print(FINAL_DICT)

myfile.close()
