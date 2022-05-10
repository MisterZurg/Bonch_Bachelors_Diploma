import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

print("Операция по умолчанию содержит: {}".format(defop.text))
print("Тестовая опция содержит: {}".format(testop.text))
