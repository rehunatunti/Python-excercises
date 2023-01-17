import re

def listToString(s):
  string = " "
  return (string.join(s))


def WriteLine(txt, find, regex, output):
  if type(output) == list:
    print (f"{txt:60s} {find:80s} {regex:15s} {listToString(output):30s}")
  else:
    print (f"{txt:60s} {find:80s} {regex:15s} {output:30s}")

  
#header = "Input" + tab * 3 + "Find" + tab * 5 + "Regexp" + tab * 3  + "Output"

i = 'Input'
f= 'Find'
r = 'Regexp'
o = 'Output'
print()
print (f"{i:60s} {f:80s} {r:15s} {o:30s}")
print (f"{60 * '-':60s} {80 * '-':80s} {15 * '-':15s} {30 * '-':30s}")
 

"""tab = "\t"
header = "Input" + tab * 3 + "Find" + tab * 5 + "Regexp" + tab * 3  + "Output"
d1 = "--------------------" + tab
d2 = "----------------------------------" + tab
d3 = "--------------------" + tab
d4 = "--------------------" + tab
dash = d1 + d2 + d3 + d4 
print(header)
print(dash)"""

txt = "The rain in Spain"
find = "Starts 'The' & ends 'Spain'"
regex = "^The.*Spain$"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "The rain in Spain"
find = "'Portugal' in the string"
regex = "Portugal"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "The rain in Spain"
find = "Lower case between + 'a' & 'm'"
regex = "[a-m]"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "That will be 59 dollars"
find = "All digits"
regex = "\d"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "hello hell helo planet"
find = "Starts with 'he' & 2 chars & 'o'"
regex = "he..o"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

#Check if the string starts with 'hello':

txt = "hello planet"
find = "Starts with 'hello'"
regex = "^hello"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "hello planet"
find = "ends with 'planet'"
regex = "planet$"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "hello he heio planet"
find = "starts with 'he', & >=0 chars & 'o'"
regex = "he.?o"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "hello planet"
find = "-\"- followed by 0 or more  (any) characters, and an \"o\"z"
regex = "he.*o"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "hello planet"
find = "starts with \"he\", followed excactly 2 (any) characters, and an \"o\""
regex = "he.{2}o"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

txt = "The rain in Spain falls mainly in the plain!"
find = "Check if the string contains either \"falls\" or \"stays\""
regex = "falls|stays"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)