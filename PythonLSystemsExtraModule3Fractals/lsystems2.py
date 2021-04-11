

def expand(currgen):
	global rule
	nextgen =""
	for char in currgen:
		if char == "F":
			nextgen+=rule
		else:
			nextgen+=char
	return nextgen
	
def cntChr(lst, str):
	#list of characters
	count = 0
	for i in str:
		if i in lst:
			count =count +1
			
	return count

axiom="F"
rule="FF[-F][+F]"
dna=axiom
for g in range(1,4):
	dna = expand(dna)
	print('this is gen', g, 'dna len', len(dna), 'dna', dna)
	print("number of Fs",cntChr(["F"],dna))
	print("number of terminal chr",cntChr(["+","-","[","]"],dna))
	print("total number of chars:",len(dna))



