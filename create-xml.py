#!/usr/bini/python

import xml.etree.ElementTree as ET
from lxml import etree
from json import load

header = '<?xml version="1.0"?>'

with open('db2color.json') as json_file:
    db2color = load(json_file)

wallTypes = ET.Element('wall-types', default = '03')
for i in db2color.keys():
    element = ET.SubElement(wallTypes, 'type', id = str(i))
    key = ET.SubElement(element, 'key')
    key.text = str(i)
    name = ET.SubElement(element, 'name')
    name.text = str(i)
    width = ET.SubElement(element, 'width')
    width.text = '1'
    attenuation = ET.SubElement(element, 'attenuation')
    attenuation.text = str(i)
    color = ET.SubElement(element, 'color')
    color.text = db2color[str(i)]

xmldata = ET.tostring(wallTypes)
root = etree.fromstring(xmldata)
print(header)
print(etree.tostring(root, pretty_print=True).decode())
