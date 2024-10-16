from colorama import Fore, Back, Style

def is_operator(name):
	i = 0
	tab = ["if", "else", "else if", "switch", "case", "default",
	"for", "while", "break", "continue", "return", "goto"]
	while i < len(tab):
		if name == list(tab[i]):
			return 1
		i += 1
	return 0

def already_there(list, name):
	if not list:
		return (0)
	for fn in list:
		if fn == name:
			return (1)
	return (0)

def forbidden_function_print(foo):
	for char in foo:
		print(Fore.RED, end="")
		print(char, end="")
		print(Style.RESET_ALL, end="")

def main_checker(allowed, used):
	print(Fore.BLACK + Back.CYAN + "\n--------------------------------RESULTS------------\
--------------------\n"+ Style.RESET_ALL)
	forbidden_fts = []
	index  = 0
	while index < len(used):
		if not already_there(allowed, used[index]):
			forbidden_fts.append(used[index])
		index += 1
	if not forbidden_fts:
		print(Fore.GREEN + Back.BLACK + "ALL THE FUNCTIONS USED ARE ALLOWED 👍\n" + Style.RESET_ALL)
		exit(0)
	print(Fore.RED + Back.BLACK + "FORBIDDEN FUNCTIONS ARE DETECTED:\n" + Style.RESET_ALL)
	for fn in forbidden_fts:
		print("👉", end='')
		forbidden_function_print(fn)
		print()
		