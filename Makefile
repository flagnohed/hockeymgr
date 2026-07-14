CC = gcc
CFLAGS = -g -Wextra -Wall -Wfloat-equal -Wshadow -Wpointer-arith \
         -Wcast-align -Wstrict-prototypes -O2 -std=c99
OBJS = main.o player.o

hockeymgr: $(OBJS)
	$(CC) -o hockeymgr $(OBJS) -lm

objs/%.o: %.c
	$(CC) -c -o $@ $^ $(CFLAGS)

clean:
	rm -rf *.o
	rm -f hockeymgr
