import get_functins
import sys

def main():
	ProjectPath = "../minishell"#input("INSERT THE PROJECT PATH: ")
	# print("INSERT THE PROJECT ALLOWED FUNCTIONS THEN PRESS CTR+D: ")
	# UserInput = sys.stdin.read()
	UserInput = "readline, rl_clear_history, rl_on_new_line, rl_replace_line, rl_redisplay, add_history,printf, malloc,\n free, write, access, open, read,close, \nfork, wait, waitpid, wait3, wait4, signal,sigaction, sigemptyset, sigaddset, kill, exit,getcwd, chdir, stat, lstat, fstat, unlink, execve,dup, dup2, pipe, opendir, readdir, closedir,strerror, perror, isatty, ttyname, ttyslot, ioctl,getenv, tcsetattr, tcgetattr, tgetent, tgetflag, tgetnum, tgetstr, tgoto, tputs"
	AllowedFunctions = UserInput.split(',')
	for i in range(len(AllowedFunctions)):
		AllowedFunctions[i] = AllowedFunctions[i].strip()
	# print(AllowedFunctions)
	# ProjectFiles = get_functins.get_files(ProjectPath)
	# for iter in range(len(ProjectFiles)):
	# 	if ProjectFiles[iter] != "non":
	# 		print(ProjectFiles[iter])
	# 	iter+=1
	functions = get_functins.get_file_lines("tst.txt")
	print(functions)
	# get_functins.get_file_lines(ProjectFiles[1])

main()