#!/usr/bin/env python
# encoding: utf-8
import random

def creatMnemonica():
	deck=reversedeck(faroshuffle(getnewdeck()),26,0)
	deck1=outfaro(deck[0:18],deck[18:36])
	deck=cutToBottom(deck1+deck[36:52],9)
	return deck
	

	
def faroshuffle(deck,level=1,time=4):
	for x in range(4):
		deck1=deck[0:26]
		deck2=deck[26:52]
		deck=outfaro(deck1,deck2)
	return deck
def outfaro(deck1,deck2):
	deck3=[]
	for i in range(len(deck1)):
			deck3.append(deck1[i])
			deck3.append(deck2[i])
	return deck3
def reversedeck(deck,end=0,begin=0):
	deck1=deck[0:begin]
	deck2=deck[begin:end]
	deck3=deck[end:52]
	deck2.reverse()
	deck=deck1+deck2+deck3
	return deck
def cutToBottom(deck,topnum):
	deck=deck[topnum:52]+deck[0:topnum]
	return deck
def guessCardInorder():
	i=0;
	count=0;
	guesscount=0;
	print("----------------------------------------------------")
	print("输入0退出，输入*显示结果,任意键开始")
	print("答案示例：club 2，heart 4，diamond 5，spade Q,heart A")
	print("----------------------------------------------------")
	type_in=input()
	state=0
	while type_in!='0':
		state=0
		i=i+1;
		count=count+1
		print ("请输入 ",i," 位置对应的牌：")
		type_in=input()
		guesscount=guesscount+1
		if(i==52) :
			i=0
			guesscount=0;
		while state==0:
			if type_in==deck[i-1]:
			    state=1
			    print("right answer!")
			elif type_in=='0':
				break;
			elif type_in=='*':
				print(deck[i-1])
				count=count-1
				break
			else:
				print("Wrong answer,guess again:")
				type_in=input()
				guesscount=guesscount+1
	print("Score:  ",100*i*i/guesscount/52)
	mainu()
		
def showMnemonica():
	ss=""
	for i in range(52):
		ss=ss+"     "+str(i+1)+"   "+deck[i]
		if((i+1)%4==0):
			ss=ss+"\n"
	print(ss)
	mainu()
def randomguess():
	pass
def randomGuessCard():
	i=0;
	count=0;
	guesscount=0;
	print("----------------------------------------------------")
	print("输入0退出，输入*显示结果,任意键开始")
	print("答案示例：club 2，heart 4，diamond 5，spade Q,heart A")
	print("----------------------------------------------------")
	type_in=raw_input()
	state=0
	while type_in!='0':
		key=random.randint(1,52)
		count=count+1
		print ("请输入",key,"位置的牌：")
		type_in=input()
		guesscount=guesscount+1
		while state==0:
			if type_in=='*':
				print(deck[key-1])
				count=count-1
				break
			elif type_in=='0':
				break
			elif type_in==deck[key-1]:
				state=1
				print("right answer!")	
			else:
				print("Wrong answer,guess again:")
				type_in=input()
				guesscount=guesscount+1
	print("Score:  ",count*count/guesscount*10)
	mainu()


def randomGUessNum():
	i=0;
	count=0;
	guesscount=0;
	print("----------------------------------------------------")
	print("输入0退出，输入*显示结果,任意键开始")
	print("答案示例：club 2，heart 4，diamond 5，spade Q,heart A")
	print("----------------------------------------------------")
	type_in=input()
	state=0
	while type_in!='0':
		key=random.randint(1,52)
		print ("请输入",deck[key-1],"位置数字：")
		type_in=input()
		guesscount=guesscount+1
		while state==0:
			if type_in=='*':
				print(key)
				break
			elif type_in=='0':
				break
			elif int(type_in,10)==key:
				state=1
				print("right answer!")	
			else:
				print("Wrong answer,guess again:")
				type_in=input()
				guesscount=guesscount+1
	mainu()


def setMaxGuessNum():
	pass
def WrongLog():
	pass

	
def getnewdeck():
	#suits=("♠","♥","♣","♦")
	#suits=("♤","♡","♧","♢")
	suits=("spade","heart","club","diamond")
	nums=("A","2","3","4","5","6","7","8","9","10","J","Q","K")
	deck=[]
	deck1=[]
	deck2=[]
	count=0;
	for i in suits:
		for j in nums:
			deck.append(i+" "+j)
	deck=reversedeck(deck,52,26)
	return deck
def mainu():
	print("--------------------------------------------------------------------")
	print("0 退出  | 1 show Mnemonica  | 2 顺序猜牌  | 3 随机猜数字 | 4 随机猜牌" )
	print("--------------------------------------------------------------------")
	i=input()
	if i=='0':
		exit()
	elif i=='1':
		showMnemonica()
	elif i=='3':
		randomGUessNum()
	elif i=='2':
		guessCardInorder()
	elif i=='4':
		randomGuessCard()


deck=creatMnemonica()
mainu()


def movecard():
	pass