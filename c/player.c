#include "player.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


#define ATTR_VAL_MIN 60
#define ATTR_VAL_MAX 80
#define HEIGHT_MIN 170
#define HEIGHT_MAX 200
#define NUM_ATTRS_G 2
#define NUM_ATTRS_S 7


int last_id = 0;


uint8_t
get_total_rating(Player_t *player) {
    if (player->pos == POS_G) {
        GoalieAttrs_t g = player->goalie;
        return (uint8_t) ((g.positioning + g.reflexes) / NUM_ATTRS_G);
    } 

    SkaterAttrs_t s = player->skater;
    return (uint8_t) ((s.body_check + s.d_awareness + s.o_awareness +
                      s.passing + s.shooting + s.speed +
                      s.stick_check) / NUM_ATTRS_S);
}


/* Return random uint8_t in range [min_val, max_val]. */
static uint8_t
random_choice(uint8_t min_val, uint8_t max_val) {
    if (min_val == max_val)
        return min_val;

    if (min_val > max_val) {
        /* No worries if the range is fucked, just reverse it.
         * Should not happen but you never know lol. */
        uint8_t tmp = min_val;
        min_val = max_val;
        max_val = tmp;
    }
    
    int rn = rand();
    return (uint8_t) (rn % (max_val - min_val + 1) + min_val);
}


/* This is a basic implementation of random handedness assignment.
 * In reality, we want to have a weighted random choice based on
 * how common lefties and righties are IRL. However, for now we
 * just use 50/50. */
static char
random_handedness(void) {
    uint8_t c = random_choice(0, 1);
    if (c == 0)
        return 'L';
    
    return 'R';
}


/* Give the player a random weight based on his height.
 * This is to prevent players from getting weird builds
 * like 200cm and 70kg (which would not make a good hockey player
 * in my opinion). */
static uint8_t
random_weight(uint8_t height) {
    /* "Hockey weight" is height - 100 kg. */
    uint8_t hw = height - 100;
    uint8_t delta = 10;
    return random_choice(hw - delta, hw + delta);
}


/* Creates a random player with random attributes. */
Player_t *
create_random_player(Position_t pos) {
    
    Player_t *p = malloc(sizeof(Player_t));
    
    /* Start by adding the general info. */
    p->id = ++last_id;
    
    const char *name = "Test Nameson";
    strncpy(p->name, name, NAME_LEN_MAX - 1);  /* TODO: Get random name from list of common names. */
    
    p->handed = random_handedness();
    p->height = random_choice(HEIGHT_MIN, HEIGHT_MAX);
    p->weight = random_weight(p->height);
    
    /* Now add skater/goalie specific attributes. */
    switch (pos) {
        case POS_G:    
            p->pos = pos;
            p->goalie.positioning = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->goalie.reflexes = random_choice(ATTR_VAL_MIN, ATTR_VAL_MIN);
            break;
        case POS_LD:
        case POS_RD:
        case POS_LW:
        case POS_RW:
        case POS_C:
            p->pos = pos;
            p->skater.shooting = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.passing = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.o_awareness = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.body_check = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.stick_check = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.d_awareness = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            p->skater.speed = random_choice(ATTR_VAL_MIN, ATTR_VAL_MAX);
            break;
        default:
            printf("Error: unknown position: %d\n", pos);
            exit(EXIT_FAILURE);
            break;
    }
    
    return p; 
}

static char *
pos_to_str(Position_t pos) {
    switch(pos) {
        case POS_G:
            return "G";
        case POS_LD:
            return "LD";
        case POS_RD:
            return "RD";
        case POS_LW:
            return "LW";
        case POS_RW:
            return "RW";
        case POS_C:
            return "C";
        default:
            printf("Error: unknown position: %d\n", pos);
            exit(EXIT_FAILURE);
    }
}


void
print_goalie_attrs(GoalieAttrs_t *ga) {
    printf("Reflexes:    %d\n", ga->reflexes);
    printf("Positioning: %d\n", ga->positioning);
}


void
print_skater_attrs(SkaterAttrs_t *sa) {
    printf("OAwareness:  %d\n", sa->o_awareness);
    printf("Passing:     %d\n", sa->passing);
    printf("Shooting:    %d\n", sa->shooting);
    printf("Bodycheck:   %d\n", sa->body_check);
    printf("DAwareness:  %d\n", sa->d_awareness);
    printf("Stickcheck:  %d\n", sa->stick_check);
    printf("Speed:       %d\n", sa->speed);
}


void
print_player(Player_t *player) {
    printf("Id:          %d\n", player->id);
    printf("Name:        %s\n", player->name);
    printf("Handedness:  %c\n", player->handed);
    printf("Height:      %d cm\n", player->height);
    printf("Weight:      %d kg\n", player->weight);
    printf("Position:    %s\n", pos_to_str(player->pos));
    
    if (player->pos == POS_G)
        print_goalie_attrs(&player->goalie);
    else
        print_skater_attrs(&player->skater);
    
    printf("Total:       %d\n", get_total_rating(player));
}

