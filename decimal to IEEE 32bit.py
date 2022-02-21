# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 02:16:21 2022

@author: User
"""

number = input("Enter decimal: ")
number=float(number)


sign_bit=0
if number<0:
    sign_bit=1
number=abs(number)


integer=int(number)
int_bin=bin(integer)[2:]

number=str(number)
comma_index=number.find(".")
fraction="0"+number[comma_index:]
fraction=float(fraction)

#print(int_bin, fraction)

bin_frac = str()

#print(fraction)
while (fraction):
         
        fraction=fraction*2
        #print(fraction)
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
           # print(fraction)
        else:
            int_part = 0

        bin_frac += str(int_part)
        if (len(bin_frac)==23):
            break
        
#print(bin_frac)

exponent=int()
manti=str()

if str(int_bin)=="0":
    
    ind1=bin_frac.index('1')+1
    ind=int("-"+str(ind1))
    
    exponent=(128-1+(ind))
    exponent=str(bin(exponent)[2:])
    while len(exponent)<8:
        exponent='0'+exponent
        print(exponent)
    
    manti=bin_frac[ind1:(23+ind1)]
    while (len(manti)<23):
        manti=manti+"0"
        
    
    
else:
    int_bin=str(int_bin)
    
    exponent=str(bin(128-1+(len(int_bin)-1))[2:])
    #print(expoent)
    manti=int_bin[1:]+bin_frac
    manti=manti[:23]
    while (len(manti)<23):
        manti=manti+"0"
        
print(sign_bit," ",exponent," ",manti)
   
    
    

    
    
    
    
    