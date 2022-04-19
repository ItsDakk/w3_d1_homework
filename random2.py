import re

with open('./files/regex-test.txt') as file:
    file_by_line = file.readlines()
    name_pattern = re.compile(r'([A-Z][\w]+) ([A-Z][\w]+)')
    found = name_pattern.findall(file_by_line)
    print(found)
