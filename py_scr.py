import sys
import random

def main():
	if len(sys.argv) > 2:
		method = sys.argv[1]
		param = sys.argv[2]
		fun = func_list(method, param)
		print(fun)
	else:
		print('no metod`s paramrtrs')

def ex(param):
	print(param)

def genering_key(input_line):
	ls = list(input_line)
	random.shuffle(ls)
	psw = ''.join([random.choice(ls) for x in range(len(input_line))])
	return psw

def func_list(method, param):
	functions = {
	'genering_key':genering_key,
	}
	if sys.argv[1] in functions:
		return functions[method](param)
	else:
		return 'Error'


if __name__ == '__main__':
	main()
