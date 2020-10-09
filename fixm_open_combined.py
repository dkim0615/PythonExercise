#!/opt/bb/bin/python3.6
import re

def fix_spec():
    fix_description = {}
    fix_dictionary = {}

    # myfile = open("quickfix.txt")
    # txt = myfile.readlines()
    current_tag = ""
    current_enum_tag = ""

    with open("quickfix.txt") as fd:
        for line in fd:
            if str("field number=") in line:
                result = re.findall('field number="(.+)" name="(.+)" ', line)
                if len(result) !=0:
                    tag_num = result[0][0]
                    # print(tag_num)
                    current_tag = tag_num
                    tag_val = result[0][1]
                    # print(tag_val)
                    fix_dictionary[tag_num] = tag_val
                    # print(fix_description, "this is fix description")

            if str("value enum=") in line:
                result_2 = re.findall('value enum="(.+)" description="(.+)"', line)
                if len(result_2) !=0:
                    val_enum = result_2[0][0]
                    # print(val_enum)
                    current_enum_tag = val_enum
                    des_val = result_2[0][1]
                    # print(des_val)
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
