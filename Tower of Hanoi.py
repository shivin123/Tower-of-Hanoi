#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This program lists the moves to solve the Tower of hanoi optimally and displays the number of moves required 
#Be careful with the number of disks you wisk it to solve as the number of moves grows expontially
from IPython.display import clear_output
class stack:
    def __init__(self, listx):
        self.listx = listx
        self.count=len(listx)
         
    def push(self, val):
        self.listx.append(val)
        self.count += 1

    def pop(self):
        val = self.listx[-1]
        del self.listx[-1]
        self.count -= 1
        return val
    
    def see(self):
        try:
            val = self.listx[-1]
            return val
        except:
            return (N+1)
while True:    
    print("Warning entering numbers greater than 20 will take significant time and numbers above 25 are not advisable.")
    x=input("Enter an intger here: ")
    if x.isdigit():
        x=int(x)
        break
    else:
        print("You have not entered a integer please try again...")

clear_output(wait=True)        
while True:
    print("Warning when entering numbers larger than 10 consider turning printing off as the number of print statments grows exponentialy.")
    p=input("Enter 1 to print every move or enter 0 to only print the start and ending: ")
    if p.isdigit():
        p=int(p)
        if p==0 or p==1:
            break
        else:
            print("You have entered an invalid number please try again")
    else:
        print("You have not entered a integer please try again...")
clear_output(wait=True)
X=[]
while x>0:
    X.append(x)
    x-=1

list1=stack(X)
list2=stack([])
list3=stack([])
list4=[list1, list2, list3]
counter=0
N=len(X)
print("N=", N, sep="")
print("______")
print(list1.listx)
print(list2.listx)
print(list3.listx)
print("______")


def pushpop(pus, po):
    pus.push(po.pop())
    if p==1:
        print(list1.listx)
        print(list2.listx)
        print(list3.listx)
        print("______")
    
def findsmall():
    if list1.see()<list2.see() and list1.see()<list3.see():
        return list1
    elif list2.see()<list1.see() and list2.see()<list3.see():
        return list2
    elif list3.see()<list1.see() and list3.see()<list2.see():
        return list3
    
def small():
    if N%2!=0:
        pushto=list4.index(findsmall())-1
    if N%2==0:
        pushto=list4.index(findsmall())+1
    if pushto>(2):
        pushto=0
    
    pushpop(list4[pushto], findsmall())
        
        
        
def findother():
    if list1.see()<list2.see() and list1.see()<list3.see():
        if list2.see()<list3.see():
            pushfrom=list2
            pushto=list3
        else:
            pushfrom=list3
            pushto=list2
    elif list2.see()<list1.see() and list2.see()<list3.see():
        if list1.see()<list3.see():
            pushfrom=list1
            pushto=list3
        else:
            pushfrom=list3
            pushto=list1
    elif list3.see()<list1.see() and list3.see()<list2.see():
        if list1.see()<list2.see():
            pushfrom=list1
            pushto=list2
        else:
            pushfrom=list2
            pushto=list1
    
    pushpop(pushto, pushfrom)

    
while len(list3.listx)<N:
    try:
        small()
        counter+=1
        findother() 
        counter+=1
    except:
        break
        
if p==0:        
    print(list1.listx)
    print(list2.listx)
    print(list3.listx)
    print("______")
print("Counter: ", counter, sep="")
print("END")
    


# In[ ]:




