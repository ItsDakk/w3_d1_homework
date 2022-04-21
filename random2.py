import re

with open('./files/regex-test.txt') as file:
    file_by_line = file.readlines()
    first_name = re.compile(r"([A-Z]\w+) (.+\w) ([A-Z]\w+)")
    for f_names in re.findall(first_name, str(file_by_line)):
        print(f_names)
   
    
    
         

    

