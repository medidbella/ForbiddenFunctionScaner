import os

g_index = 0

def get_files(DirectoryPath):
	Files = []
	for root, dirs, files in os.walk(DirectoryPath):
		for file in files:
			Files.append(os.path.join(root, file))
	
	tab = [-1] * len(Files)
	index = 0
	for j in range(len(Files)):
		if ".c" not in Files[j] and ".h" not in Files[j]:
			tab[index] = j
			index += 1
	i = 0
	while tab[i] != -1:
		Files[tab[i]] = "non"
		i += 1
	return (Files)

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
	size = (end - start + 1) + 1
	new_str = [' '] * (size + 1)
	i = 0
	while start <= end:
		new_str[i] = str[start]
		start+=1
		i += 1
	new_str[i] = "\0"
	return new_str

def in_quote(string, i):
	i -= 1
	while i >= 0:
		if string[i] == 39 or string[i] == 34:
			return 1
		i -= 1
	return 0

def file_optimizer(file):
	i = 0
	j = 0
	flag = 0

	while j < len(file):
		i = 0
		while i < len(file[j]):
			if file[j][i] == '{' and in_quote(file[j], i) == 0:
				if flag == 0:
					flag += 1
				else:
					file[j][i] = '<'
					flag += 1
			if file[j][i] == '}' and in_quote(file[j], i) == 0:
				flag -= 1
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
				substring = creat_string(chars[g_index], start, end)
				Functions.append(substring)
			i += 1
		j+=1

# def get_used_fts(FilePath, Functions):
# 	data = open(FilePath, 'r')
# 	chars = [list(line) for line in data]
# 	j = 0
# 	end = 0
# 	start = 0
# 	ft_idx = 0
# 	while j < len(chars):
# 		i = 0
# 		while i < len(chars):
# 			if chars[j][i] == '(':
# 				end = get_end()

def get_all_fts(dir):
	Files = get_files(dir)
	CreatedFunctions = []
	j = 0
	while j < len(Files):
		if (Files[j] != "non"):
			get_created_function(Files[j], CreatedFunctions)
		j += 1
	return CreatedFunctions