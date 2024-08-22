NAME = philo
FILES = philo_main.c before_simulatoin.c extra_functoins.c thread_safe_functoins.c
OBJ_FILES = $(FILES:.c=.o)
CFLAGS =  -Wall -Wextra -Werror 

$(NAME): $(OBJ_FILES)
	cc $(OBJ_FILES) -o $(NAME)

all:$(NAME)

clean:
	rm -f $(OBJ_FILES)

fclean: clean
	rm -f $(NAME)

re: fclean all
