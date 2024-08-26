
srv = server
clt = client
CC = cc
CFLAGS = -Wall -Wextra -Werror
utils = minitalk_utils.c


all: $(srv) $(clt)

$(srv): server.c $(utils)
	$(CC) $(CFLAGS) $(utils) server.c -o $(srv)

$(clt): client.c $(utils)
	$(CC) $(CFLAGS) $(utils) client.c -o $(clt)

clean:
	rm -f $(srv) $(clt)

fclean: clean

re: fclean all
