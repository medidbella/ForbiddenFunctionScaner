import get_functins
import sys

def main():
	ProjectPath = input("INSERT THE PROJECT PATH: ")
	print("INSERT THE PROJECT ALLOWED FUNCTIONS THEN PRESS CTR+D: ")
	UserInput = sys.stdin.read()
	AllowedFunctions = UserInput.split(',')
	for i in range(len(AllowedFunctions)):
		AllowedFunctions[i] = AllowedFunctions[i].strip()
	i += 1
	print(AllowedFunctions)
	print(get_functins.get_files(ProjectPath))

main()