#Regular Expressions

import re
#abcd, book, desk
#ca?e
#care, cafe, case, cave
#caae, cabe, cace, cade, ....

p = re.compile("ca.e")
# . (ca.e): denote a text (letter in this case) > care, cafe, case (o) | caffe (x)
# ^ (^de): denote the start of string > desk, destination (o) | fade (x)
# $ (se$): denote the end of string > case, base (o) | face (x)

def print_match(m):
    if m:
        print("m.group():", m.group()) # returns matching string
        print("m.string:", m.string) # returns inputted string
        print("m.start():", m.start()) # starting index of matching string
        print("m.end():", m.end()) # ending index of the matching string
        print("m.span():", m.span()) # starting index and ending index of the matching string 

    else:
        print("No match")

# m = p.match("careless") # match: check from the beginning 
# print_match(m)

#print(m.group()) # if it does not match, error occurs

# m = p.search("good care") # search: check if anything matches
# print_match(m)

# lst = p.findall("good care cane") # findall : return all matching string in list form
# print(lst)

# 1. p = re.compile ("wanted form")
# 2. m = p.match ("string to compare") : does given string match from the beginning?
# 3. m = p.search("string to compare") : does given string match at all?
# 4. lst = p.findall("string to compare") : return everything that matches in list form

# Wanted forms : regular Expressions 
# . (ca.e): denote a text (letter in this case) > care, cafe, case (o) | caffe (x)
# ^ (^de): denote the start of string > desk, destination (o) | fade (x)
# $ (se$): denote the end of string > case, base (o) | face (x)

