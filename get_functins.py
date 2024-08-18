import os

def get_files(DirectoryPath):
	Files  = os.listdir(DirectoryPath)
	for i in range(len(Files)):
		Files[i] = DirectoryPath + "/" + Files[i]
	return (Files)