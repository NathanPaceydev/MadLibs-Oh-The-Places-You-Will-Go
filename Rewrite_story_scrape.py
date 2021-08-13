#!/usr/bin/env python
# coding: utf-8

# In[1]:


#first time scraping program
## I wanted to do something static to start and just have fun with the outcome
# import libraries
import requests
from bs4 import BeautifulSoup


# In[2]:


# scraping the staic website 
URL = "http://denuccio.net/ohplaces.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#print(page.text) # prints the text obj, ie the html code


# In[3]:


result = soup.find_all("p")
StringDict = []
#print(result)
for results in result:
    StringDict.append(str(results.get_text()))

    
print("Oh the Places You Will Go\nDr.Suess")    
print(StringDict[1])
#iteratable container
#job_elements = results.find_all("p")


# In[4]:


#User Input
print("Enter a Body part")
NounB = input()
print("\nEnter a Verb")
Verb1 = input()
print("\nEnter a 2nd Verb")
Verb2 = input()
print("\nEnter Your Name")
YourName = input()
print("\nEnter a Place")
place = input()
print("Enter an Adjective")
Adjective1 = input()
print("Enter a number")
num = input()

stringPrint = "\n"+YourName+" Entered a noun: "+NounB+", a verb of: "+Verb1+" and "+Verb2+", in a location of "+ place
print(stringPrint)


# In[5]:


stringT = (StringDict[1].strip()).split("***")
string = stringT[0]
#print(Noun)
string = string.replace("brain",NounB)
string = string.replace("foot",NounB)
string = string.replace("the guy", YourName)
string = string.replace("You", YourName)
string = string.replace("town",place)
string = string.replace("head straight",Verb1)
string = string.replace("fliers",Verb2)
string = string.replace("prowl",Verb2)
string = string.replace("The Waiting Place",place)
string = string.replace("Great",Adjective1)
string = string.replace("Buxbaum",str(YourName[0]+"uxbaum"))
string = string.replace("Bixby",str(YourName[0]+"ixby"))
string = string.replace("Bray",str(YourName[0]+"ray"))
string = string.replace("98",num)


print("The New Updated Story Just for You:\n\n")
print(string)

