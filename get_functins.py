import os

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
		i+=1
	return (Files)

def get_start(lst, i):
    while i > 0:
        i -= 1
    return i

def get_end(lst, i):
    while i >= 0 and lst[i] != '(':
        i -= 1
    return i - 1

def	remove_returnval(str):
	i = 0
	size = 0
	while str[i] != '\0' and str[i] != ' ' and str[i] != '\t':
		i += 1
	while str[i] != '\0' and str[i] != ' ' and str[i] == '\t':
		i += 1
	while str[i] != '\0':
		size += 1
		i += 1
	i -= 1
	while i >= 0 and str[i] != ' ' and str[i] != '\t':
		i -= 1
	i += 1
	new_str = [' '] * (size + 1)
	index = 0
	while str[i] != '\0':
		new_str[index] = str[i]
		i += 1
		index += 1
	new_str[index] = '\0'
	return new_str

def creat_string(str, start, end):
	size = (end - start + 1) + 1
	new_str = [' '] * size
	i = 0
	while start <= end:
		new_str[i] = str[start]
		start+=1
		i+=1
	new_str[i] = "\0"
	return remove_returnval(new_str)

def get__created_function(FilePath):
	if FilePath == "non":
		return
	data = open(FilePath, 'r')
	chars = [list(line) for line in data]
	j = 0
	end = 0
	start = 0
	flag = 0
	ft_idx = 0
	function = []
	while j < len(chars):
		i = 0
		while i < len(chars[j]):
			if chars[j][i] == '{':
				if i == 0 :
					end = get_end(chars[j - 1], len(chars[j-1]) - 1)
					start = get_start(chars[j - 1], len(chars[j-1]) - 1)
					flag = 1
				else:
					end = get_end(chars[j], i)
					start = get_start(chars[j], i)
					flag = 0
				substring = creat_string(chars[j - flag], start, end)
				function.append(substring)
				ft_idx += 1
				break
			i += 1
		j+=1
	return function

def get_all_fts(Files):
	functions = []
	for j in range(len(Files)):
