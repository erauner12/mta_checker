#!/usr/bin/python3.6

import xml.etree.ElementTree as ET
import pprint

mtauseruser = ET.parse('silentmta.xml')
myroot = mtauseruser.getroot()

# This is to parse the usernames in the file
mill = {}
apps = {}

mill["mill_user"] = []
apps["mill_app"] = []
for user_list in myroot:
    for users in user_list:
        for usernames in users:
            if usernames.tag == 'UserName':
                mill["mill_user"].append(usernames.text)
#            for app in usernames:
#                stringtest=app.tag
#                if stringtest != "Application":
#                    break
#                else:
#                    apps["mill_app"].append(app.text)
                


millname = mill["mill_user"]
appname = apps["mill_app"]

pprint.pprint(millname)
