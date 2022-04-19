import re

with open('./files/names.txt') as file:
    file_by_line = file.readlines()
for line in file_by_line:
    # group_1 = re.compile(r'([A-Z][a-zA-z]+)')
    twitter_pattern = re.compile(r'@')
    # group_2 = re.compile(r'(\s@\w+)')
    # name = group_1.findall(line)
    twitter_pattern = twitter_pattern.findall(line)
    # print(name)
    print(twitter_pattern)
    # print(twitter)

    # with open("./files/names.txt") as file:
#     data = file.readlines()
    
# for line in data:
#     name_search = re.compile(r"([A-Z][a-z]+)?,[\s][\w]+")
#     twitter_search = re.compile(r"([\s]@[\w]+)")
#     name = name_search.match(line)
#     twitter = twitter_search.findall(line)
#     start, stop = name.span()
#     full_name_split = (line[start:stop]).split(", ")
#     full_name = full_name_split[1] + " " + full_name_split[0]
#     if twitter:
#         print(full_name + " / " + twitter[0].lstrip())