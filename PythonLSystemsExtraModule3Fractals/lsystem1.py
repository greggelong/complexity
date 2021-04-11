

def expand(currgen):
	global rule
	nextgen =""
	for char in currgen:
		if char == "F":
			nextgen+=rule
		else:
			nextgen+=char
	return nextgen
	


axiom="F"
rule="FF[-F][+F]"
dna=axiom
for g in range(1,4):
	dna = expand(dna)
	print('this is gen', g, 'dna len', len(dna), 'dna', dna)


