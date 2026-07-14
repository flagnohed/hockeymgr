#ifndef _PLAYER_H_
#define _PLAYER_H_

#include <stdbool.h>

#define NUM_ATTRS 5  /* NOT including the total. */

typedef enum {
    POS_GOALIE,
    POS_DEFENSEMAN,
    POS_FORWARD,
}   Position_t;

typedef struct {
    unsigned int shooting;
    unsigned int passing;
    unsigned int skating;
    unsigned int hitting;
    unsigned int defense;
    unsigned int total;
}   Attributes_t;

typedef struct {
    const char *name;
    char hand;
    unsigned int age;
    unsigned int height;
    unsigned int weight;
    Position_t position;
    Attributes_t *attrs;
}   Player_t;

void player_print(Player_t *player, bool skip_attrs);
void player_set_random_attrs(Attributes_t *attrs);

#endif
