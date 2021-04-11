import random

rules = {
   "S": [
    ["The", "N", "V"]
   ],
 "N": [
  ["cat"],
    ["dog"]
   ],
"V": [
  ["meows"],
  ["barks"]   ] }
  
def expand(start,expansion):
	if start in rules:
		pick = random.choice(rules[start])
		for elem in pick:
			expand(elem,expansion)
	else:
		expansion.append(start)
	return expansion
			
	
print(rules)
print(rules["S"], len(rules["S"][0]))
print(random.choice(rules["N"]))
if "S" in rules: #will be recursive escape cond
	print("yes there is")
else:
	print("no there isn't")

print(expand("S",[]))