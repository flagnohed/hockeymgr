#ifndef PLAYER_H
#define PLAYER_H


#include <stdint.h>


#define NAME_LEN_MAX 50


typedef enum {
    POS_G,
    POS_LD,
    POS_RD,
    POS_LW,
    POS_RW,
    POS_C,
}   Position_t;



typedef struct {
    /* Offensive attributes. */
    uint8_t shooting;
    uint8_t passing;
    uint8_t o_awareness;
    /* Defensive attributes. */
    uint8_t body_check;
    uint8_t stick_check;
    uint8_t d_awareness;
    /* Neutral attributes (used both in offence and defence). */
    uint8_t speed;
}   SkaterAttrs_t;


typedef struct {
    uint8_t reflexes;
    uint8_t positioning;
}   GoalieAttrs_t;


typedef struct {
    int id;      /* Unique per player. */
    char name[NAME_LEN_MAX];
    char handed;     /* Handedness, 'L' or 'R'. */
    uint8_t height;
    uint8_t weight;
    Position_t pos;
    union {
        SkaterAttrs_t skater; 
        GoalieAttrs_t goalie;
    };
}   Player_t;


Player_t *create_random_player(Position_t pos);
void print_player(Player_t *player);

#endif
