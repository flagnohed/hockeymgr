CC = gcc
CFLAGS = -g -Wextra -Wall -Wfloat-equal -Wshadow -Wpointer-arith \
         -Wcast-align -Wstrict-prototypes -O2
OBJS = objs/main.o objs/player.o objs/team.o

hockeymgr: $(OBJS)
	$(CC) -o hockeymgr $(OBJS)

objs/%.o: %.c
	$(CC) -c -o $@ $^ $(CFLAGS)

clean:
	rm -rf objs/*
	rm -f hockeymgr
