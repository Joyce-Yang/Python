import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = sys.argv[1]
content = open(url,"rb").read()

wordList = content.split("/ ")
# wordList2 = []
freq = {}
for word in wordList:
  freq[word] = freq.get(word, 0) + 1
#keyList = freq.keys()
#for key in keyList:
#  print "%-10s %d" % (key, freq[key])
keyList = sorted(freq.items(), key = lambda item:item[1], reverse = True)
count_f = open("count.file","w")
for key in keyList:
#  print "%-10s %d" % (key[0], key[1])
  kstr = key[0] + ',' + str(key[1])
  kstr.encode('utf-8')
  count_f.write(kstr)
  count_f.write('\n')
count_f.close()
 
