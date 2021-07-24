import random
r = random.randint(1,100)
while True :
	number = input ('隨便猜一個數字吧!')
	number = int (number)
	if number == r :
		print ('猜對了ㄟ!')
		break
	elif number > r :
		print ('太大了!')
	else :
		print ('太小了!')
		