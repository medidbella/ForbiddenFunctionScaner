import os

def get_files(DirectoryPath):
	Files = []
	Files  = os.listdir(DirectoryPath)
	tab = [-1] * len(Files)
	index = 0
	for j in range(len(Files)):
		if ".c" not in Files[j] and ".h" not in Files[j]:
			tab[index] = j
			index += 1
	for i in range(len(Files)):
		Files[i] = DirectoryPath + "/" + Files[i]
	return (Files)

def get_file_lines(FilePath):
	data = open(FilePath, 'r')
	for line in data:
		print(line)