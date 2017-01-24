#encoding-utf8
import re
m = re.search("output_(\d{4})", "output_1986.txt")
print(m.group(1))

#(?P<name>...) name the group
m = re.search("output_(?P<year>\d{4})", "output_1986.txt")
print(m.group("year"))