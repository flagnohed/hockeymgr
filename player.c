#include "player.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define PI 3.14159265358979323846
#define ATTR_MEAN 80.0
#define ATTR_STDDEV 5.0

static char *pos_to_str(Position_t position) {
    switch (position) {
        case POS_GOALIE:
            return "Goalie";
        case POS_DEFENSEMAN:
            return "Defenseman";
        case POS_FORWARD:
            return "Forward";
        default:
            return "Unknown";
    }
}

static double rand_normal(double mean, double stddev) {
    /* I just made some BULLSHIT! This is like a poor-mans
     * version of the Box-Muller transform, scaled and
     * translated to the given mean and standard deviation.
     * Don't know why or how good it works, but it works!
     * Looks random at least! */
    double x = (double) rand() / RAND_MAX;
    double y = (double) rand() / RAND_MAX;
    return sqrt(-2 * log(x)) * cos(2 * PI * y) * stddev + mean;
}

void player_set_random_attrs(Attributes_t *attrs) {
    attrs->defense =  (unsigned int) rand_normal(ATTR_MEAN, ATTR_STDDEV);
    attrs->hitting =  (unsigned int) rand_normal(ATTR_MEAN, ATTR_STDDEV);
    attrs->passing =  (unsigned int) rand_normal(ATTR_MEAN, ATTR_STDDEV);
    attrs->skating =  (unsigned int) rand_normal(ATTR_MEAN, ATTR_STDDEV);
    attrs->shooting = (unsigned int) rand_normal(ATTR_MEAN, ATTR_STDDEV);
    attrs->total = (unsigned int) ((attrs->defense + attrs->hitting +
                attrs->passing + attrs->skating + attrs->shooting) / NUM_ATTRS);
}

void player_print(Player_t *player, bool skip_attrs) {
    printf("%s, %u\n", player->name, player->age);
    printf("Height:   %u cm\n", player->height);
    printf("Weight:   %u kg\n", player->weight);
    printf("Position: %s\n", pos_to_str(player->position));
    printf("Handed:   %s\n", (player->hand == 'L' ? "Left" : "Right"));
    if (skip_attrs) return;
    printf("Shooting: %u\n", player->attrs->shooting);
    printf("Skating:  %u\n", player->attrs->skating);
    printf("Passing:  %u\n", player->attrs->passing);
    printf("Hitting:  %u\n", player->attrs->hitting);
    printf("Defense:  %u\n", player->attrs->defense);
    printf("Total:    %u\n", player->attrs->total);
}
