>>>import urllib2
>>># urllib2 is use to download the html content of the web link
>>>response = urllib2.urlopen('http://python.org/')
>>># You can read the entire content of a file using read() method
>>>html = response.read()
>>>print len(html)

>>># Regular expression based split the string
>>>tokens = [tok for tok in html.split()]
>>>print "Total no of tokens :"+ str(len(tokens))
>>># First 100 tokens
>>>print tokens[0:100]

>>>import re
>>># using the split function
>>>#https://docs.python.org/2/library/re.html
>>>tokens = re.split('\W+',html)
>>>print len(tokens)
>>>print tokens[0:100]

>>>import nltk
>>># http://www.nltk.org/api/nltk.html#nltk.util.clean_html
>>>clean = nltk.clean_html(html)
>>># clean will have entire string removing all the html noise
>>>tokens = [tok for tok in clean.split()]
>>>print tokens[:100]


>>>import operator
>>>freq_dis={}
>>>for tok in tokens:
>>>		if tok in freq_dis:
>>>    		freq_dis[tok]+=1
>>>		else:
>>>    		freq_dis[tok]=1


>>>import nltk
>>>Freq_dist_nltk=nltk.FreqDist(tokens)
>>>print Freq_dist_nltk
>>>for k,v in Freq_dist_nltk.items():
>>>    print str(k)+':'+str(v)

>>>Freq_dist_nltk.plot(50, cumulative=False)


>>>stopwords=[word.strip().lower() for word in open("PATH/english.stop.txt")]
>>>clean_tokens=[tok for tok in tokens if len(tok.lower())>1 and (tok.
lower() not in stopwords)]
>>>Freq_dist_nltk=nltk.FreqDist(clean_tokens)
>>>Freq_dist_nltk.plot(50, cumulative=False)