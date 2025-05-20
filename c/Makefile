CC = gcc
CFLAGS = -g -Wextra -Wall -Wfloat-equal -Wshadow -Wpointer-arith \
         -Wcast-align -Wstrict-prototypes -O2
OBJS = main.o player.o team.o

hockeymgr: $(OBJS)
  $(CC) -o hockeymgr $(OBJS)

%.o: %.c
  $(CC) -c -o $@ $^ $(CFLAGS)
