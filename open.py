#!/opt/bb/bin/python3.6

# open fix44.xml 
# read line by line
# if the line includes field number=x, name=y, and the next line is not value enum=z 
# add the num and name to Dict 1 and move on to the next line
# if the line includes field number=x, name=y, and the next line is value enum=z
# add the num and name and enum to Dict 2

EMPTY_DICT = {}
FINAL_DICT = {}

myfile = open("example.txt")
txt = myfile.readlines()
current_tag = ""
current_enum_tag = ""

for line in txt:
    # print(line[:-1])
    value_dict = {}
    any_dict = {}

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
        any_dict = any_dict.append(value_dict)
        print(any_dict) ##AttributeError: 'dict' object has no attribute 'append' really?!
    
    FINAL_DICT[current_tag] = any_dict
    print(FINAL_DICT)

myfile.close()
