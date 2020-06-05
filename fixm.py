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
    "40" : {"1" : "Market", "2" : "Limit", "3" : "Stop", "4" : "Stop Limit", "5" : "Market on close"},
    "54" : {"1" : "BUY", "2" : "SELL"},
    "59" : {"0" : "DAY", "1" : "GTC", "2" : "OPG", "3" : "IOC", "4" : "FOK", "6" : "GTD"},
    "150" : {"0" : "NEW", "1" : "Partial fill", "2" : "Fill", "3" : "Done for Day", "4" : "Canceled", "5" : "Replaced", "6" : "Pending Cancel", "8" : "Rejected", "E" : "Pending Replace"}
    }

    return fix_dictionary, fix_description

def make_list(fix_tag):
    list1 = []
    for item in fix_tag:
        list1.append(fix_tag)
        list1 = sorted(list1)
        return list1

def fix_translation(fixm):
    fix_dictionary, fix_description = fix_spec()
    for tags in fixm:
        tags = tags.strip()
        fix_tag = tags[:tags.find("=")]
        fix_tag = fix_tag.replace(" ","")
        #add fix tags to an empty list to sort numerically and output them back as type str
        fix_value = tags[tags.find("="):len(tags)].replace("=", "")
        if fix_tag == '':
            continue
        elif fix_tag in fix_dictionary and fix_tag not in fix_description:
            print(fix_tag.rjust(6," ") + ":" + str(fix_dictionary[fix_tag]).rjust(25," ") + " " + "=" + " " + str(fix_value).ljust(40," "))
        elif fix_tag in fix_description:
            print(fix_tag.rjust(6," ") + ":" + str(fix_dictionary[fix_tag]).rjust(25," ") + " " + "=" + " " + str(fix_value + "(" + fix_description[fix_tag][fix_value] + ")").ljust(40," "))
        else:
            print(fix_tag.rjust(6," ") + ":" + str(fix_value).rjust(25," ") + " " + "=" + " " + "not found in fix dictionary".ljust(40," "))

result = fix_spec()
print(result)

fix_message = input("Please enter a fix message: ")
fixm = fix_message.split('|')
fix_translation(fixm)
