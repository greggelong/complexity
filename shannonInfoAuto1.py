import math

def makeDict(inString):
    ''' turns string into a dictionary. the key is word. the
        value is number of times it appears in the string
        divided by the total word in the string
        '''
    mystring1= inString.strip()  # get rid of white space
    mylist = mystring1.split() # split into a list
    mytotal = len(mylist)
    mydict = {}                 # create dictionary

    for item in mylist:         # iterate through list counting number of times an item appears
        numOf = mylist.count(item)
        mydict[item] = numOf / mytotal
    
    return mydict  
    


def shannonH(messageDict):
    '''takes a dictionary and returns a number
       H - Shannon information       
       H(message source) = - sumM (p log2 p)
       Let M be the number of possible messages, and p
       be the probabilty of the message    
    '''
    H = 0
    
    for key in messageDict:
        value = messageDict[key]
        H = H + value * math.log(value,2)
        
    return -H  





# you can change the string
mystring = " to be or not to be  "


sdict = makeDict(mystring)

print(sdict)
print(mystring)
print(shannonH(sdict))

