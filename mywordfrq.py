from collections import Counter
import re

inStr = "T*&^he scientist does not&% study nature because it is useful; he studies it because he delights in it, and he delights in it because it is beautiful. If nature were not beautiful it would not be worth knowing, and if nature were not worth knowing, life would not be worth living"

# cleaning the text

lstr = inStr.lower()  # make lower case

pfstr = re.sub(r'[^\w\s]','',lstr) # removing punctuation using regular expressions

mycount = Counter(pfstr.split()) # actuall calling Counter on a list by first calling split()

print(inStr)
print(lstr)
print(pfstr)
print(mycount)
