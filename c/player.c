#include "player.h"
#include <stdio.h>
#include <stdlib.h>

#define ATTR_VAL_MIN 60
#define ATTR_VAL_MAX 80

uint8_t
generate_random_attr_val() {
    int rn = rand();
    return rn % (ATTR_VAL_MAX - ATTR_VAL_MIN + 1) + ATTR_VAL_MIN;
}


Player_t *
create_random_player(Position_t pos) {
    Player_t *p;
    /* Start by adding the general info. */
    p->name = "";
    switch (pos) {
        case POS_G:    
            break;
        case POS_LD:
        case POS_RD:
        case POS_LW:
        case POS_RW:
        case POS_C:
            break;
        default:
            break;
    }

    return p; 
}
