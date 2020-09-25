x = input()


for i in range(1, x + 1):
	left = ''.join(map(str, range(1, i)))
	spaces = ' ' * (x - i)
	print(f'{spaces}{left}{i}{left[::-1]}')