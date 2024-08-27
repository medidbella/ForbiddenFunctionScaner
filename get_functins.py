import os
import checker
g_index = 0

def get_start(lst, j, i):
	global g_index
	flag = 0
	while j >= 0:
		i = len(lst[j]) - 1
		while i >= 0:
			if lst[j][i] == '(':
				flag = 1
				break
			i -= 1
		if flag == 1:
			break
		j -= 1
	flag = 0
	if i == 0 or (lst[j][i - 1] == ' ' or lst[j][i - 1] == '\t'):
		while j >= 0:
			i = len(lst[j]) - 1
			while i >= 0:
				if lst[j][i] != '\t' and lst[j][i] != ' ':
					flag  = 1
					break
				i -= 1
			if flag == 1:
				break
			j -= 1
	i -= 1
	while i >= 0 and lst[j][i] != '\t' and lst[j][i] != ' ':
		i -= 1
	g_index = j
	return i + 1

def get_end(lst, start):
	global g_index
	i = start
	while i < len(lst[g_index]) and lst[g_index][i] != '(':
		i += 1
	return i - 1 

def creat_string(str, start, end):
	size = (end - start )
	new_str = [' '] * (size + 1)
	i = 0
	while start <= end:
		new_str[i] = str[start]
		start+=1
		i += 1
	return new_str

def in_quote(string, i):
	i -= 1
	while i >= 0:
		if string[i] == 39 or string[i] == 34:
			return 1
		i -= 1
	return 0

def is_called(list, j, i):
	i += 1
	while (j < len(list)):
		while (i < len(list[j])):
			if (list[j][i] == '{' and not in_quote(list[j], i)):
				return 0
			if (list[j][i] == ';' and not in_quote(list[j], i)):
				return 1
			i += 1
		i = 0
		j += 1
	return 0

def is_alpha_numirique(c):
	return ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9') or c == '_')

def is_empty(list, i):
	while i >= 0:
		if (list[i] != '\n' and list[i] != ' ' and list[i] != '\t'):
			return (0)
		i -= 1
	return (1)

def get_end_2(list, j, i):
	global g_index
	i -= 1
	if i < 0:
		i = len(list[j - 1])
		j -= 1
	while is_empty(list[j], i):
		j -= 1
		i = len(list[j]) - 1
	g_index = j
	while (i >= 0):
		if list[j][i] != '\n' and list[j][i] != ' ' and list[j][i] != '\t':
			return i
		i -= 1
	g_index = j
	return i

def get_start_2(list, i):
	i -= 1
	while list[i] == ' ' or list[i] == '\t':
		i -= 1
	while i >= 0:
		if not is_alpha_numirique(list[i]):
			return i + 1
		i -= 1
	return i + 1

def is_function(list, j, i):
	i -= 1
	flag = 0
	while j >= 0:
		while i >= 0:
			if list[j][i] != '\n' and list[j][i] != '\t' and list[j][i] != ' ':
				flag = 1
				break
			i -= 1
		if flag == 1:
			break
		j -= 1
		i = len(list[j]) - 1
	index = 0
	while i >= 0 and is_alpha_numirique(list[j][i]):
			i -= 1
	if i < 0 or (list[j][i] != '\n' and list[j][i] != '\t' and list[j][i] != ' '):
		return (0)
	return (1)

def get_files(DirectoryPath):
	Files = []
	if not os.path.exists(DirectoryPath):
		print("no such file or directory: " + DirectoryPath)
		exit(1)
	for root, dirs, files in os.walk(DirectoryPath):
		for file in files:
			Files.append(os.path.join(root, file))
	if not Files:
		print("there are no .c files in " + DirectoryPath)
		exit(1)
	tab = [-1] * len(Files)
	index = 0
	for j in range(len(Files)):
		if ".c" not in Files[j]:
			tab[index] = j
			index += 1
	i = 0
	while tab[i] != -1:
		Files[tab[i]] = "non"
		i += 1
	return (Files)

def file_optimizer(file):
	i = 0
	j = 0
	flag = 0

	while j < len(file):
		i = 0
		while i < len(file[j]):
			if file[j][i] == '{' and not in_quote(file[j], i):
				if flag == 0:
					flag += 1
				else:
					file[j][i] = '<'
					flag += 1
			if file[j][i] == '}' and not in_quote(file[j], i):
				flag -= 1
			i += 1
		j += 1


def get_used_function(FilePath, Functions):
	global g_index
	data = open(FilePath, 'r')
	chars = [list(line) for line in data]
	j = 0
	end = 0
	start = 0
	while j < len(chars):
		i = 0
		while i < len(chars[j]):
			if chars[j][i] == '(' and is_called(chars, j, i) and is_function(chars, j, i):
				end = get_end_2(chars, j, i)
				start = get_start_2(chars[g_index], end)
				result = creat_string(chars[g_index], start, end)
				if not checker.is_operator(result) and not checker.already_there(Functions, result):
					Functions.append(result)
			i += 1
		j += 1

def get_created_function(FilePath, Functions):
	global g_index
	data = open(FilePath, 'r')
	chars = [list(line) for line in data]

	j = 0
	end = 0
	start = 0
	file_optimizer(chars)
	while j < len(chars):
		i = 0
		while i < len(chars[j]):
			if chars[j][i] == '{':
				start = get_start(chars, j, i)
				end = get_end(chars, start)
				result = creat_string(chars[g_index], start, end)
				if not checker.already_there(Functions, result):
					Functions.append(result)
			i += 1
		j += 1

def get_all_fts(dir, CreatedFunctions, UsedFunctions):
	Files = get_files(dir)
	j = 0
	while j < len(Files):
		if (Files[j] != "non"):
			get_created_function(Files[j], CreatedFunctions)
			get_used_function(Files[j], UsedFunctions)
		j += 1
	return UsedFunctions