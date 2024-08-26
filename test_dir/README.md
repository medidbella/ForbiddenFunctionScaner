This project aims to code a small data exchange program using UNIX signals.
the challenge is that

you can only use one global variable per program, also you can only use 
two signals (SIGUSR1 and SIGUSR2)

--------------------------------------------HOW TO USE IT---------------------------------------

-1 after cloning the run the make file by typing "make"

-2 then you will have two programs (server and client) run the server first (its ID will be printed)

-3 in another terminal run the client program like this (./cleint ("the-server-id" "any message you want to send")

lastly, you will see that the same message is printed in the first terminal where the server is running

if the message printed by the server is different try to increase the value given
to the usleep function in the "client.c" file make it for example 500
