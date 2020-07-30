#!/opt/bb/bin/python3.6
def fix_spec():
    fix_dictionary = {
    "1" : "ACCOUNT",
    "8" : "BEGINSTRING",
    "9" : "BODYLENGTH",
    "11" : "CLORDID",
    "15" : "CURRENCY",
    "17" : "EXECID",
    "21" : "HANDLINST",
    "22" : "IDSOURCE",
    "34" : "MSGSEQNUM",
    "35" : "MSGTYPE",
    "38" : "ORDERQTY",
    "40" : "ORDTYPE",
    "43" : "POSSDUPEFLAG",
    "48" : "SECURITYID",
    "49" : "SENDERCOMPID",
    "50" : "SENDERSUBID",
    "52" : "SENDINGTIME",
    "54" : "SIDE",
    "55" : "SYMBOL",
    "56" : "TARGETCOMPID",
    "57" : "TARGETSUBID",
    "58" : "TEXT",
    "59" : "TIF",
    "60" : "TRANSACTTIME",
    "100" : "EXDESTINATION",
    "115" : "ONBEHALFOFCOMPID",
    "116" : "ONBEHALFOFSUBID",
    "122" : "ORIGSENDINGTIME",
    "128" : "DELIVERTOCOMPID",
    "129" : "DELIVERTOSUBID",
    "142" : "SENDERLOCATIONID",
    "150" : "ExecType",
    "167" : "SECTYPE",
    "207" : "SECURITYEXCHANGE",
    "369" : "LASTMSGSEQNUMPROCESSED",
    "10" : "CHECKSUM"
    }

    fix_description = {
    "35" : {"0" : "Heartbeat", "1" : "Test Request", "2" : "Resend Request", "3" : "Reject", "4" : "Sequence Reset", "5" : "Logout", "8" : "Execution Report", "D" : "Order - Single", "Q" : "DK Trade"},
    "21" : {"1" : "AUTO", "2" : "AUTO/MAN", "3" : "MAN"},
    "22" : {"1" : "CUSIP", "2" : "SEDOL", "3" : "QUIK", "4" : "ISIN", "5" : "RIC"},
    "40" : {"1" : "Market", "2" : "Limit", "3" : "Stop", "4" : "Stop Limit", "5" : "Market on close"},
    "54" : {"1" : "BUY", "2" : "SELL"},
    "59" : {"0" : "DAY", "1" : "GTC", "2" : "OPG", "3" : "IOC", "4" : "FOK", "6" : "GTD"},
    "150" : {"0" : "NEW", "1" : "Partial fill", "2" : "Fill", "3" : "Done for Day", "4" : "Canceled", "5" : "Replaced", "6" : "Pending Cancel", "8" : "Rejected", "E" : "Pending Replace"}
    }

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
