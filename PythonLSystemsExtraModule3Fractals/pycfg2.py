import random
rules2 = {
  'S': [
    ['NP', 'VP'],
    ['Interj', 'NP', 'VP']
  ],
  'NP': [
    ['Det', 'N'],
    ['Det', 'N', 'that', 'VP'],
    ['Det', 'Adj', 'N']
  ],
  'VP': [['Vtrans', 'NP'], ['Vintr']],
  'Interj': [['oh'], ['my'], ['wow'], ['darn']],
  'Det': [['this'], ['that'], ['the']],
  'N': [
    ['amoeba'],
    ['dichotomy'],
    ['seagull'],
    ['trombone'],
    ['staff'],
    ['corsage']
  ],
  'Adj': [
    ['bald'],
    ['smug'],
    ['important'],
    ['tame'],
    ['overstaffed'],
    ['corsage']
  ],
  'Vtrans': [['computes'], ['examines'], ['foregrounds']],
  'Vintr': [['coughs'], ['daydreams'], ['whines']]
}
rules = {
   "S": [
    [ "N", "V"]
   ],
 "N": [
  "cat",
    "dog"
   ],
"V": [
  "meows",
  "barks"  ] }
  
def validSent(mysent):
  mylist = mysent.split(' ')
  print(mylist)
  print(rules["S"][0])
  for elmt in rules["S"][0]:
  	print(rules[elmt],"waw")
  	for word in mylist:
  		if word in rules[elmt]:
  			print(word,"is ok")
  		else:
  			return False
  return True
  
  
def expand(start,expansion):
	if start in rules2:
		pick = random.choice(rules2[start])
		for elem in pick:
			expand(elem,expansion)
	else:
		expansion.append(start)
	return ' '.join(expansion)
			
	
print(rules)
print(rules["S"], len(rules["S"][0]))
print(random.choice(rules["N"]))
if "S" in rules: #will be recursive escape cond
	print("yes there is")
else:
	print("no there isn't")

print(expand('S',[]))
print(validSent('dog barks'))