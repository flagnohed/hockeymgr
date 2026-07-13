#include "team.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>


#define LINE_SIZE 5  /* 2 defenders, 3 forwards. */


int last_team_id = 0;


Team_t *
create_random_team(uint8_t num_skaters) {
    if (num_skaters > NUM_SKATERS_MAX) {
        printf("Maximum skaters in a team is %d\n", NUM_SKATERS_MAX);
        exit(EXIT_FAILURE);
    }

    Team_t *t = malloc(sizeof(Team_t));
    t->id = ++last_team_id;
    const char *name = "Test HC";
    strncpy(t->name, name, NAME_LEN_MAX - 1);

    /* Count how many lines we can get from NUM_SKATERS.
     * Idk what to do with excess players (i.e., if we get for
     * example 13 players (2 lines + 3 players)). For now,
     * just ignore them. */
    uint8_t num_lines = floor((double) num_skaters/LINE_SIZE);
    for (size_t i = 0; i < num_lines; i++) {
        t->skaters[LINE_SIZE * i]     = create_random_player(POS_LD);
        t->skaters[LINE_SIZE * i + 1] = create_random_player(POS_RD);
        t->skaters[LINE_SIZE * i + 2] = create_random_player(POS_LW);
        t->skaters[LINE_SIZE * i + 3] = create_random_player(POS_RW);
        t->skaters[LINE_SIZE * i + 4] = create_random_player(POS_C);
    }

    t->goalie = create_random_player(POS_G);
    return t;
}
