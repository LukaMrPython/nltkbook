>>>lst=[1,2,3,4]
>>>print lst


>>> print ''First element :'' +str(lst[0])
>>> print ''last element :'' +str(lst[-1])
>>> print ''first three elements :'' +str(lst[0:2])
>>> print ''last three elements :''+str(lst[-3:])
>>> dir(lst)

>>> help(lst.index)
>>> mystring=""Monty Python !  And the holy Grail ! \n""
>>> print mystring.strip()

>>> print ""Converting the string into all capitals--> " +str(mystring.upper())"
>>> print "Replacing '!' from the string ---> ""+ mystring.replace('!','''')"

# regex 
>>> # We have to import re module to use regular expression
>>> import re
>>> if re.search('Python',mystring):
>>>     print ""We found python ""
>>> else:
>>>     print ""NO ""


>>># declare a dictionary
>>>word_freq={}
>>>for tok in string.split():
>>>		if tok in word_freq:
>>>    		word_freq [tok]+=1
>>>		else:
>>>    		word_freq [tok]=1
>>>print word_freq
