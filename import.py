import random
start = input('请决定随机数字范围初始值: ')
end = input('请决定随机数字的结束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	try_input = input('请猜一下数字: ')
	try_input = int(try_input)
	if try_input == r:
		print('恭喜你猜对了')
		print('这是你猜的第', count, '次')
		break
	elif try_input < r:
		print('你猜的小了点')
	elif try_input > r:
		print('你猜的大了点')
	print('这是你猜的第', count, '次')