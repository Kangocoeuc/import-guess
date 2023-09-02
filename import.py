import random
r = random.randint(1, 100)
while True:
	try_input = input('请猜一下数字: ')
	try_input = int(try_input)
	if try_input == r:
		print('恭喜你猜对了')
		break
	elif try_input < r:
		print('你猜的小了点')
	elif try_input > r:
		print('你猜的大了点')