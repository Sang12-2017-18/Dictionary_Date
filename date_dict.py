#!/usr/bin/env python3
import re
import time
import datetime
def checkDiff(t1,t2):
	if(t1[0] == t2[0]):
		if(t1[1] == t2[1]):
			return 2
		else:
			return 1
	else:
		return 0

def convertStr(num):
	if num<=0:
		return "NUll"
	str1=str(num)
	if num < 10:
		str1='0'+str(num)
	return str1
	
def addDay(D1,t1,t2):
	day1=t1[2]
	month=t1[1]
	year=t1[0]
	m1=convertStr(month)
	day2=t2[2]
	#day1=day1+1
	while day1!=(day2+1):
		d3=convertStr(day1)
		str1="-".join([str(year),m1,d3])
		#print("Date inserted: ",str1)
		#time.sleep(2.0)
		if D1.get(str1,-2)<0: 
			#print("Date inserted: ",str1)
			D1[str1]=0
		day1=day1+1
def leapYear(y):
	if y%4==0:
		if y%100==0:
			if y%400==0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def addMonth(D1,t1,t2):
	day1=t1[2]
	day2=t2[2]
	month1=t1[1]
	month2=t2[1]
	year=t1[0]
	day_end=0
	while month1!=month2:
		#print("Inside month while loop")
		if month1 in (4,6,9,11):
			day_end=30
		elif month1 in (1,3,5,7,8,10,12):
			day_end=31
		else:
			if leapYear(year):
				day_end=29
			else:
				day_end=28
		tup1=(year,month1,day1)
		tup2=(year,month1,day_end)
		addDay(D1,tup1,tup2)
		month1=month1+1
		day1=1
	#print("Outside month while loop")
	tup1=(year,month1,day1)
	addDay(D1,tup1,t2)

def addYear(D1,t1,t2):
	day1=t1[2]
	day2=t2[2]
	month1=t1[1]
	month2=t2[1]
	year1=t1[0]
	year2=t2[0]
	while year1!=year2:
		#print("Inside year while loop: ")
		m_end=12
		d_end=31
		tup1=(year1,month1,day1)
		tup2=(year1,m_end,d_end)
		addMonth(D1,tup1,tup2)
		year1=year1+1
		month1=day1=1
	#print("Outside year while loop")
	#print("Year: ",year1,"Month: ",month1,"Day: ",day1)
	tup1=(year1,month1,day1)
	addMonth(D1,tup1,t2)

def countDays(elem1,elem2):
	t1=datetime.datetime(elem1[0],elem1[1],elem1[2])
	t2=datetime.datetime(elem2[0],elem2[1],elem2[2])
	c=t2-t1
	#print("Difference: ",c.days)
	return c.days	

def addValues(D1,t1,t2,str1,str2,diff):
	val1=D1[str1]
	keylist=list(sorted(D1.keys()))
	#print("Keylist: ",keylist)
	#print("Val1: ",val1)
	pos=0
	pos1=0
	for i in range(len(keylist)):
		if keylist[i] == str1:
			pos=i
			break 

	for i in range(len(keylist)):
		if keylist[i] == str2:
			pos1=i
			break
	k=1
	for i in range(pos+1,pos1+1):
		D1[keylist[i]]=round(val1+diff*k)
		k=k+1
	
	
def solution(D):
	D1=dict(sorted(D.items()))
	list1=[]
	for elem in D1.keys(): 
		y,m,d=tuple(elem.split('-'))
		list1.append((int(y),int(m),int(d)))

	for i in range((len(list1)-1)): 
		elem1=list1[i]
		elem2=list1[i+1]
		str1="-".join([str(elem1[0]),convertStr(elem1[1]),convertStr(elem1[2])])
		str2="-".join([str(elem2[0]),convertStr(elem2[1]),convertStr(elem2[2])])
		index=checkDiff(elem1,elem2) 
		if index==2:
			addDay(D1,elem1,elem2)
		if index==1:
			addMonth(D1,elem1,elem2)
		if index==0:
			addYear(D1,elem1,elem2)
		n=countDays(elem1,elem2)
		val1=D[str1]
		val2=D[str2]
		diff=(val2-val1)/n
		addValues(D1,elem1,elem2,str1,str2,diff)
	return D1

D={'2019-01-25':10,'2019-02-03':20}
D2=solution(D)
print(dict(sorted(D2.items())))
