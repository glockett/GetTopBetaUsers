import imaplib
import email
import json
import time
import collections

with open('config.json') as json_data:
    data = json.load(json_data)

# Set conf to environment from config.json (test, android or ios)
conf = 'android'

cf_host = data[conf]['host']
cf_login = data[conf]['login']
cf_password = data[conf]['password']

# Connect to GMail account
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(cf_login, cf_password)


# split an address list into list of tuples of (name,address)
def split_addrs(s):
    if not (s): return []
    outQ = True
    cut = -1
    res = []
    for i in range(len(s)):
        if s[i] == '"': outQ = not (outQ)
        if outQ and s[i] == ',':
            res.append(email.utils.parseaddr(s[cut + 1:i]))
            cut = i
    res.append(email.utils.parseaddr(s[cut + 1:i + 1]))
    return res


while True:
    try:
        FOLDER = raw_input("Enter the folder to search: \n")
        mail.select(FOLDER)
        result, data = mail.search(None, "ALL")
        ids = data[0].split()
        print("Processing Folder...")
        break
    except Exception:
        print("Oops!  That was not a valid Folder.  Try again...")
        continue

msgs = mail.fetch(','.join(ids), '(BODY.PEEK[HEADER])')[1][0::2]
addr = []


# Set temp file to store and write the list
tempFile = open('temp1.txt', 'w')

emailList = list()

tempFile.close()

# Traverse the GMail folder and add the email address to temp file
for x, msg in msgs:
    msgobj = email.message_from_string(msg)
    addr.extend(split_addrs(msgobj['from']))
    emailList.append(msgobj['from'])

topList = collections.Counter(emailList).most_common(10)

# Generate output file
output = open('topUsers.txt', 'w')
output.write("Top 10 users from " + FOLDER + ": - " + time.strftime("%d/%m/%Y %H:%M:%S"))
output.write("\n*********************************************\n\n")
output.write("\n".join(map(lambda x: str(x), topList)))
output.close()

# Remove the host from the list of addresses
f = open('topUsers.txt', 'r')
keyword = [cf_host]
lst = []
for line in f:
    for word in keyword:
        if word in line:
            line = line.replace(line, '')
    lst.append(line)
f.close()
f = open('topUsers.txt', 'w')
for line in lst:
    f.write(line)
f.close()

print ("Process complete")
