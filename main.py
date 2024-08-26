import get_functins
import sys

def main():
	ProjectPath = "./test_dir" #just for testing
	#input("INSERT THE PROJECT PATH: ")
	# print("INSERT THE PROJECT ALLOWED FUNCTIONS FOLLOWD BY A NEWLINE THEN PRESS CTR+D: ")
	# UserInput = sys.stdin.read()
	UserInput = "readline, rl_clear_history, rl_on_new_line, rl_replace_line, rl_redisplay, add_history,printf, malloc,\n free, write, access, open, read,close, \nfork, wait, waitpid, wait3, wait4, signal,sigaction, sigemptyset, sigaddset, kill, exit,getcwd, chdir, stat, lstat, fstat, unlink, execve,dup, dup2, pipe, opendir, readdir, closedir,strerror, perror, isatty, ttyname, ttyslot, ioctl,getenv, tcsetattr, tcgetattr, tgetent, tgetflag, tgetnum, tgetstr, tgoto, tputs"
	AllowedFunctions = UserInput.split(',')
	for i in range(len(AllowedFunctions)):
		AllowedFunctions[i] = AllowedFunctions[i].strip()
	tab = []
	tab = get_functins.get_all_fts(ProjectPath)
	for i in range(len(tab)):
		for j in range(len(tab[i])):
			print(tab[i][j], end="")
		print()
main()