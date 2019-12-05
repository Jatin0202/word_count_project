from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def jj(request):
    return HttpResponse("<h1>My name is Jatin Dhingra</h1>")

def dhingra(request):
    return render(request,'first web page.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    wordcountdictionary={}
    for word in wordlist:
        if word in wordcountdictionary:
            #increase
            wordcountdictionary[word]+=1
        else:
            wordcountdictionary[word]=1
    sortedWords=sorted(wordcountdictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'no':len(wordlist),'sortedwords':sortedWords})