import random
x = input ('請決定數字上限')
y = input ('請決定數字下限')
x = int (x)
y = int (y)
r = random.randint(x,y)
count = 0
while True :
	number = input ('隨便猜一個數字吧!')
	number = int (number)
	count = count+1
	if number == r :
		print ('猜對了ㄟ!')
		break
	elif number > r :
		print ('太大了!')
	else :
		print ('太小了!')
print ('你猜了',count,'次')

