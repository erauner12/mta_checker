#!/usr/bin/python3.6


import xml.etree.ElementTree as ET

tree = ET.parse('silentmta.xml')
#tree = ET.parse('test.xml')
root = tree.getroot()


# one specific item attribute
print('Item #2 attribute:')
print(root[1][0].attrib)

''' 
print("--")

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

print("--")

# one specific item's data
print('\nItem #2 data:')
print(root[0][1].text)
print("--")


# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)
        print("--") '''