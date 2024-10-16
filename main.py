import get_functins
import sys
import checker

if len(sys.argv) < 2:
    print("Usage: python3 main.py <project_path>")
    exit(1)
else:
    ProjectPath = sys.argv[1]

def main():
	print("INSERT THE PROJECT ALLOWED FUNCTIONS SEPRATED BY A ','\
	FOLLOWED BY A NEWLINE THEN PRESS CTR+D: ")
	UserInput = sys.stdin.read()
	AllowedFunctions = UserInput.split(',')
	for i in range(len(AllowedFunctions)):
		AllowedFunctions[i] = list(AllowedFunctions[i].strip())
	used_fts = []
	get_functins.get_all_fts(ProjectPath, AllowedFunctions, used_fts)
	checker.main_checker(AllowedFunctions, used_fts)
main()