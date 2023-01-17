"""
Regex lista : Korjaa, malli on Moodlessa
"""

import re

print (f"{'Input':30s} {'Find':45s} {'Regexp':15s} {'Output':30s}")
print (f"{30 * '-':30s} {45 * '-':45s} {15 * '-':15s} {30 * '-':30s}")

txt ="hello planet"
find = "ends with planet"
regex = "planet$"
output = re.findall(regex, txt)
WriteLine(txt, find, regex, output)

