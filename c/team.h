#include "player.h"


#define NUM_SKATERS_MAX 15

typedef struct {
    int id;
    char name[NAME_LEN_MAX];
    Player_t *skaters[NUM_SKATERS_MAX + 1];
    Player_t *goalie;
}   Team_t;


Team_t *create_random_team(uint8_t num_skaters);
