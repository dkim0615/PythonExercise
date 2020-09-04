#!/opt/bb/bin/python3.6

def fix_spec():
    fix_description = {}
    fix_dictionary = {}

    myfile = open("quickfix.txt")
    txt = myfile.readlines()
    current_tag = ""
    current_enum_tag = ""

    for line in txt:
        if str("field number=") in line:
            tag_num = line[line.find("number="):line.find(" name")]
            int_val_b= tag_num.replace("number=","")
            int_val = int_val_b.strip("\"")
            current_tag = int_val
        
            tag_val = line[line.find("name="):line.find(" type")]
            str_val_b = tag_val.replace("name=","")
            str_val = str_val_b.strip("\"")
            
            fix_dictionary[current_tag] = str_val

        elif str("value enum") in line: 
            enum_num = line[line.find("enum="):line.find(" description")]
            int_num_b = enum_num.replace("enum=","")
            int_num = int_num_b.strip("\"")
            current_enum_tag = int_num

            enum_val = line[line.find("description="):line.find("/>")]
            des_val_b = enum_val.replace("description=","")
            des_val = des_val_b.strip("\"")
            
            if current_tag not in fix_description:
                fix_description[current_tag] = {}
            fix_description[current_tag][current_enum_tag] = des_val

    return fix_dictionary, fix_description

def make_list(fixm):
    fix_dictionary, fix_description = fix_spec()
    empty_list = []
    values_list = []
    sorted_list = []

    for item in fixm:
        if item =='':
            continue
        num = item[:item.find("=")]
        num = int(num)
        empty_list.append(num)
        fix_value = item[item.find("="):len(item)].replace("=","")
        values_list.append(fix_value)

    zip(empty_list, values_list)
    sorted_list = list(zip(empty_list, values_list))
    sorted_list.sort()
    print("\n")
    #print(sorted_list)
    
    for sorted_item in sorted_list:
        if str(sorted_item[0]) in fix_dictionary and str(sorted_item[0]) not in fix_description:
            print(str(sorted_item[0]).rjust(6," ") + ":" + str(fix_dictionary[str(sorted_item[0])]).rjust(20," "),"=", sorted_item[1].ljust(40," "))
        elif str(sorted_item[0]) in fix_description:
            print(str(sorted_item[0]).rjust(6," ") + ":" + str(fix_dictionary[str(sorted_item[0])]).rjust(20," "),"=", sorted_item[1] + "(" + fix_description[str(sorted_item[0])][sorted_item[1]] + ")".ljust(40," "))
        else:
            print(str(sorted_item[0]).rjust(6," ") + ":" + str(sorted_item[0]).rjust(20," "),"=", sorted_item[1].ljust(40," "))

result = fix_spec()
#print(result)

fix_message = input("Please enter a fix message: ")
fixm = fix_message.split('|')
make_list(fixm)
