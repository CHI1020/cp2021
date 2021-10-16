import urllib.request
from bs4 import BeautifulSoup
import sys, codecs
from pybean import Store, SQLiteWriter

# 將系統輸出語系編碼設為 utf8
sys.stdout = codecs.getwriter("utf8")(sys.stdout.detach())
# 表示要讀入的文章檔名為 wed.txt
filename = "wed"
 
"""
 Project: Concordancer Jr.
 File name: concordance.py
 Description:  Counts up the number of each unique word in a block of plain text.
 
 Copyright (C) 2010 Steve Osborne, srosborne (at) gmail.com
 http://yakinikuman.wordpress.com/
 *******
 This program is free software; you can redistribute it and/or modify 
 it under the terms of the GNU General Public License as published by 
 the Free Software Foundation; either version 2 of the License, or 
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful, but 
 WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
 or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
 for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
 *******
 Version history:
 1.0   Oct 27 2010
 2.0      Nov 11, 2010 - put into a class.  Can now be called with any block of text.
 
"""
 
class Concordancer:
    def __init__(self):
        #from http://www.duboislc.org/EducationWatch/First100Words.html
        #some common words a little fishy... "water"? "oil"??  But no "am"???
        self.common = ['the','of','and','a','to','in','is','you','that','it',
            'he','was','for','on','are','as','with','his','they','i',
            'at','be','this','have','from','or','one','had','by','word',
            'but','not','what','all','were','we','when','your','can','said',
            'there','use','an','each','which','she','do','how','their','if',
            'will','up','other','about','out','many','then','them','these','so',
            'some','her','would','make','like','him','into','time','has','look',
            'two','more','write','go','see','number','no','way','could','people',
            'my','than','first','water','been','call','who','oil','its','now',
            'find','long','down','day','did','get','come','made','may','part']
 
        self.wordIndex = dict() #will be a count of each word in the input text
        self.total = 0 #total words
        self.unique = 0 #unique words
 
    def getCommon(self):
        return self.common
 
    def updateCommon(self,newCommon):
        #newCommon is a list of words to be used on future calls to topWordsNotCommon
        self.common = newCommon
 
    def extendCommon(self,newCommon):
        #newCommon is a list of words to be added to self.common
        self.common.extend(newCommon)
 
    def populateIndex(self,data):
        #data is a block of text
        #splits up data and adds each word to the index
        #repeated calls to populateIndex will NOT clear the index - will just keep adding up words in new block of text
        for word in data.split():#splits at and removes whitespace
            self.addword(word)
        self.calculateUniqueWords()
        self.calculateTotalWords()
 
    def addword(self,word):
        word = word.translate("0123456789.!?,;:*\)\(\[\]\\\n/'\"")#remove punctuation, numbers, and newlines
 
        if len(word) > 5 and word.isalpha():
            word = word.lower()#convert to lower case
            #special case of dashes "--": separate into two words
            if "--" in word:
                words = word.replace('--',' ')
                for w in words.split():
                    self.addword(w)
            elif word in self.wordIndex:
                self.wordIndex[word] = self.wordIndex[word] + 1
            else:
                self.wordIndex[word] = 1
 
    def getSortedIndex(self):
        #note - sorted returns a list of tuples, not a dictionary
        s1 = sorted(list(self.wordIndex.items()),key=lambda item:item[0]) #secondary key: sort alphabetically
        s2 = sorted(s1,key=lambda item:item[1], reverse=True) #primary key: sort by count
        return s2
 
    def calculateUniqueWords(self):
        self.unique = len(self.wordIndex)
 
    def calculateTotalWords(self):
        total = 0
        for word in list(self.wordIndex.keys()):
            total = total + self.wordIndex[word]
        self.total = total
 
    def topWords(self,n,fExcludeCommon=1):
        #run only after "populateIndex" for meaningful output
        #returns list of top min(n,unique) words in the index
        #fExcludeCommon: if 1 [default], excludes any words in self.common.  Set to 0 to include all words.
        #returns list of (word,count) pairs for the top n words.  'count' is the count of that word.
        s2 = self.getSortedIndex()
        lwords = []
        i = 0
        while len(lwords) < n and i < self.unique:
            key = s2[i][0]
            value = s2[i][1]
            item = (key,value)
            if fExcludeCommon:
                if key not in self.common:
                    lwords.append(item)
            else:
                lwords.append(item)
            i = i + 1
        return lwords
 
# 以上為統計文章中單字出現次數的類別
 
def chk_dictec(vocabulary):
    # eng -> chinese
    url = 'http://dictionary.sina.com.hk/p/word/'
    urlee = 'http://dictionary.sina.com.hk/p/ee/word/'
    urles = 'http://dictionary.sina.com.hk/p/sentence/'
    response = urllib.request.urlopen(url+vocabulary)
    text = response.read()
    return text
    
def chk_dictee(vocabulary):
    # eng -> eng
    urlec = 'http://dictionary.sina.com.hk/p/word/'
    url = 'http://dictionary.sina.com.hk/p/ee/word/'
    urles = 'http://dictionary.sina.com.hk/p/sentence/'
    response = urllib.request.urlopen(url+vocabulary)
    text = response.read()
    return text
    
def chk_dictes(vocabulary):
    # eng -> sentence
    urlec = 'http://dictionary.sina.com.hk/p/word/'
    urlee = 'http://dictionary.sina.com.hk/p/ee/word/'
    url = 'http://dictionary.sina.com.hk/p/sentence/'
    response = urllib.request.urlopen(url+vocabulary)
    text = response.read()
    return text
 
def parse_doc(html):
    all_text = ""
    soup = BeautifulSoup(html, "lxml")
    div_tag = soup.findAll('p',{'class',"font15_grey kingsoft_ei"})
    for i in range(len(div_tag)):
        all_text += div_tag[i].get_text()+"\n\n"
    div_tag = soup.findAll('span',{'class',"font14_blue kingsoft_ei"})
    for i in range(len(div_tag)):
        all_text += div_tag[i].get_text()+"\n\n"
    #print(all_text+"\n")
    return all_text+"\n"
 
# 用來統計單字次序的全域變數
word_count = 0

library = Store(SQLiteWriter("words.sqlite", frozen=False))

def checkWord(word):
    global word_count
    # create vocabulary table
    vocabulary = library.new("vocabulary")
    # set word field data
    vocabulary.word = word
    ec_html = chk_dictec(word)
    ec_text = parse_doc(ec_html)
    # set ec field of vocabulary table as our_text
    if ec_text != "\n\n\n":
        # set ec field data
        vocabulary.ec = ec_text
        ee_html = chk_dictee(word)
        ee_text = parse_doc(ee_html)
        # set ee field data
        vocabulary.ee = ee_text
        es_html = chk_dictes(word)
        es_text = parse_doc(es_html)
        # set es field data
        vocabulary.es = es_text
        library.save(vocabulary)
        # commit modification into library
        library.commit()
        word_count += 1
        word_def = str(word_count)+". "+word+":\n"
        word_def += ec_text + ee_text + es_text
        word_def += "_"*50+"\n"
    return word_def
 
# 檔案是要將結果存檔用的 handle
fileHandle = open("words_"+filename+".txt", "w", encoding="utf-8")
 
# 以下為統計文章單字用的程式呼叫
concord = Concordancer()
file = filename+'.txt'
f = open(file,'rt',encoding="utf-8")
data = f.read()#the whole file as one big string
concord.populateIndex(data)
 
n = concord.unique
print("Top %s words:" % n)
top = concord.topWords(n)
 
# 隨後的 key 就是單字
order = 0
all_text = ""
debug = False
num = 5
count = 0
for item in top:
    count += 1
    order += 1
    key = item[0]
    value = item[1]
    #print(order,"%s:%s" % (key,value))
    if debug:
        if count <= num:
            print(order,key,value)
            all_text += checkWord(key)
    else:
        #print(order,key,value)
        try:
            all_text = checkWord(key)
            fileHandle.write(all_text)
        except:
            pass
            
print("done")