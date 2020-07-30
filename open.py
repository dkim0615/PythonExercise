#!/opt/bb/bin/python3.6

# open fix44.xml 
# read line by line
# if the line includes field number=x, name=y, and the next line is not value enum=z 
# add the num and name to Dict 1 and move on to the next line
# if the line includes field number=x, name=y, and the next line is value enum=z
# add the num and name and enum to Dict 2


EMPTY_DICT = {}
TEMP_DICT = {}
NEW_DICT = {}

myfile = open("example.txt")
txt = myfile.readlines()
current_tag = ""
current_enum_tag = ""

for line in txt:
    # print(line[:-1])

    if str("field number=") in line:
        tag_num = line[line.find("number="):line.find(" name")]
        int_val = tag_num.replace("number=","")
        # print("int_val", int_val)
        current_tag = int_val
    
        tag_val = line[line.find("name="):line.find(" type")]
        str_val = tag_val.replace("name=","")
        # print("str_val", str_val)

        EMPTY_DICT[current_tag] = str_val
        print("EMPTY DICT", EMPTY_DICT)

    if str("value enum=") in line:
        value_dict={}
        enum_num = line[line.find("enum="):line.find(" description")]
        int_num = enum_num.replace("enum=","")
        # print("int_num", int_num)
        current_enum_tag = int_num

        enum_val = line[line.find("description="):line.find(" />")]
        des_val = enum_val.replace("description=","")
        # print("des_val", des_val)

        value_dict[current_enum_tag] = des_val
        print("VALUE DICT", VALUE_DICT)
        TEMP_DICT
        # print(current_tag, "current tag")

    # NEW_DICT[current_tag] = VALUE_DICT
    # print("NEW DICT", NEW_DICT)

    
# print("EMPTY DICT", EMPTY_DICT)

myfile.close()



### this is example.txt ###
  <field number='35' name='MsgType' type='STRING'>
   <value enum='0' description='HEARTBEAT' />
   <value enum='1' description='TEST_REQUEST' />
   <value enum='2' description='RESEND_REQUEST' />
   <value enum='3' description='REJECT' />
   <value enum='4' description='SEQUENCE_RESET' />
   <value enum='5' description='LOGOUT' />
  <field number='54' name='Side' type='STRING'>
   <value enum='0' description='BUY' />
   <value enum='1' description='SELL' />
